#!/usr/bin/env python3
"""Live route verification for the deployed StrongAvatar.com launch set.

Checks every route registered in site/data/launch_set.json against the
production domain: HTTP status, canonical URL correctness, title presence,
robots meta, live sitemap parity with output/sitemap.xml, and 404 behavior
for an unregistered route.

This script requires network access to the production domain and is
therefore NOT part of site/scripts/quality_gate.py, which must remain
deterministic and offline. Run it manually after any deployment, and
record results in a dated report under site/reports/ per DECISION_LOG.md
practice.

Exit code 0 = all checks pass; 1 = one or more failures.
"""

import json
import os
import re
import subprocess
import sys

BASE = "https://strongavatar.com"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UNREGISTERED_PROBE = "/not-a-page/"


def fetch(url):
    proc = subprocess.run(
        ["curl", "-sS", "--max-time", "20", "-w", "\n%{http_code}", url],
        capture_output=True, text=True,
    )
    body, _, code = proc.stdout.rpartition("\n")
    return code.strip(), body


def main():
    launch_set_path = os.path.join(REPO_ROOT, "site", "data", "launch_set.json")
    with open(launch_set_path, "r", encoding="utf-8") as handle:
        routes = json.load(handle)["allowed_routes"]

    failures = []

    for route in routes:
        url = BASE + route
        code, body = fetch(url)
        if code != "200":
            failures.append("%s returned HTTP %s" % (route, code))
            continue
        canonical = re.search(r'<link rel="canonical" href="([^"]+)"', body)
        if not canonical or canonical.group(1) != url:
            failures.append(
                "%s canonical is %r, expected %r"
                % (route, canonical.group(1) if canonical else None, url)
            )
        if not re.search(r"<title>[^<]+</title>", body):
            failures.append("%s has no title" % route)
        robots_meta = re.search(r'<meta name="robots" content="([^"]+)"', body)
        if not robots_meta or robots_meta.group(1) != "index, follow":
            failures.append(
                "%s robots meta is %r, expected 'index, follow'"
                % (route, robots_meta.group(1) if robots_meta else None)
            )

    code, _ = fetch(BASE + UNREGISTERED_PROBE)
    if code != "404":
        failures.append(
            "unregistered route %s returned HTTP %s, expected 404 (soft-404 risk)"
            % (UNREGISTERED_PROBE, code)
        )

    code, live_sitemap = fetch(BASE + "/sitemap.xml")
    if code != "200":
        failures.append("/sitemap.xml returned HTTP %s" % code)
    else:
        with open(os.path.join(REPO_ROOT, "output", "sitemap.xml"), encoding="utf-8") as handle:
            if live_sitemap.strip() != handle.read().strip():
                failures.append("live sitemap.xml differs from output/sitemap.xml")

    code, live_robots = fetch(BASE + "/robots.txt")
    if code != "200":
        failures.append("/robots.txt returned HTTP %s" % code)
    else:
        with open(os.path.join(REPO_ROOT, "output", "robots.txt"), encoding="utf-8") as handle:
            repo_robots = handle.read().strip()
        # The CDN may prepend managed content (e.g. Cloudflare content
        # signals); the repo-governed section must still be present intact.
        if repo_robots not in live_robots:
            failures.append("repo-governed robots.txt section missing from live robots.txt")

    if failures:
        for failure in failures:
            print("FAIL: %s" % failure)
        print("\n%d failure(s) across %d routes" % (len(failures), len(routes)))
        return 1

    print("PASS: %d live routes verified — 200, canonical, title, robots meta;" % len(routes))
    print("PASS: unregistered route returns 404; sitemap parity; robots section intact")
    return 0


if __name__ == "__main__":
    sys.exit(main())
