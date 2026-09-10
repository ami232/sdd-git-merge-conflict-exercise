"""Simple checkout calculator for an online store.

TODO(team): implement the pricing rule(s) assigned to you in the README.
"""


def calculate_total(
    subtotal, apply_discount=False, apply_tax=False, apply_shipping=False
):
    """Calculate the final total a customer pays for their cart."""
    total = subtotal
    shipping = 5
    # TODO: apply your assigned feature's pricing rule here, gated behind
    # its argument (apply_discount, apply_tax, or apply_shipping)
    if apply_discount and total > 50:
        total -= (total * 0.10)
    # Edit for pull request
    if apply_tax:
        total += total * 0.08
    # edit for pull request
    if apply_shipping:
        total += shipping
    return total


if __name__ == "__main__":
    example_subtotal = 100.0

    print(
        f"Total for a ${example_subtotal:.2f} cart: "
        f"${calculate_total(example_subtotal):.2f}"
    )

    print(
        f"Total for a ${example_subtotal:.2f} cart with discount: "
        f"${calculate_total(example_subtotal, True, False):.2f}"
    )

    print(
        f"Total for a ${example_subtotal:.2f} cart with tax: "
        f"${calculate_total(example_subtotal, False, True):.2f}"
    )

    print(
        f"Total for a ${example_subtotal:.2f} cart with discount and tax: "
        f"${calculate_total(example_subtotal, True, True):.2f}"
    )