from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, ensure_keys, fail, load_json, pass_message


REQUIRED_PRODUCT_KEYS = [
    "product_id",
    "title",
    "type",
    "status",
    "active",
    "authority_impact",
    "buyer_logic_support",
    "activation_conditions",
    "prohibited_shortcuts",
]


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []

    site = load_json("site/data/site.json")
    if site.get("monetization_status") != "principle_only_non_active":
        errors.append("site monetization_status must be principle_only_non_active")

    registry = load_json("site/data/monetization_products.json")
    if registry.get("monetization_active") is not False:
        errors.append("monetization_active must be false")

    products = registry.get("products")
    if not isinstance(products, list):
        errors.append("monetization_products.json must contain a products array")
    else:
        for product in products:
            context = f"product {product.get('product_id', '<missing product_id>')}"
            errors.extend(ensure_keys(product, REQUIRED_PRODUCT_KEYS, context))
            if product.get("active") is not False:
                errors.append(f"{context} has active monetization")
            if product.get("status") != "planned":
                errors.append(f"{context} status must be planned")

    if errors:
        fail("; ".join(errors))

    pass_message("monetization registry remains planned and inactive")


if __name__ == "__main__":
    main()
