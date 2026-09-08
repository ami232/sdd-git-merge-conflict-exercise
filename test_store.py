"""Tests for store.py.

Which tests pass depends on how many features have been merged into
calculate_total so far. That's expected, not a bug:

- Nobody's feature merged yet -> only test_no_feature_yet passes.
- Only Feature A (discount) merged -> only test_discount_feature_alone passes.
- Only Feature B (tax) merged -> only test_tax_feature_alone passes.
- Only Feature C (shipping) merged -> only test_shipping_feature_alone passes.
- All of your group's features merged and the conflict resolved correctly
  -> test_all_features_combined (and only that one, plus test_no_feature_yet
  will now fail, which is also expected) passes.

Use test_all_features_combined as the final check once your trunk owner has
resolved the merge conflict and combined everyone's work.
"""

from store import calculate_total


def test_no_feature_yet():
    assert calculate_total(100.0) == 100.0


def test_discount_feature_alone():
    # Feature A: 10% discount on carts over $50
    assert calculate_total(100.0) == 90.0


def test_tax_feature_alone():
    # Feature B: 8% sales tax on every order
    assert calculate_total(100.0) == 108.0


def test_shipping_feature_alone():
    # Feature C (3-person groups only): flat $5 shipping fee
    assert calculate_total(100.0) == 105.0


def test_all_features_combined():
    # Final check for a 2-person group (discount, then tax):
    #   100 -> 90 (10% discount) -> 97.2 (8% tax)
    # Final check for a 3-person group (discount, then tax, then shipping):
    #   100 -> 90 -> 97.2 -> 102.2 (flat $5 shipping)
    # Only one of these applies to your group. See the README.
    result = calculate_total(100.0)
    assert result in (97.2, 102.2), (
        f"Expected 97.2 (2-person group) or 102.2 (3-person group), got {result}. "
        "Did you combine the features in the right order? See the README."
    )
