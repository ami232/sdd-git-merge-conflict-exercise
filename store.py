"""Simple checkout calculator for an online store.

TODO(team): implement the pricing rule(s) assigned to you in the README.
"""


def calculate_total(
    subtotal, apply_discount=False, apply_tax=False, apply_shipping=False
):
    """Calculate the final total a customer pays for their cart."""
    total = subtotal

    if apply_discount and subtotal >= 50:
        total *= 0.9

    return total


if __name__ == "__main__":
    example_subtotal = 100.0
    print(
        f"Total for a ${example_subtotal:.2f} cart: ${calculate_total(example_subtotal):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with discount: ${calculate_total(example_subtotal, True, False):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with tax: ${calculate_total(example_subtotal, False, True):.2f}"
    )
    print(
        f"Total for a ${example_subtotal:.2f} cart with discount and tax: ${calculate_total(example_subtotal, True, True):.2f}"
    )
