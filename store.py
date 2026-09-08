"""Simple checkout calculator for the TechMart online store.

TODO(team): implement the pricing rule(s) assigned to you in the README.
"""


def calculate_total(subtotal):
    """Calculate the final total a customer pays for their cart.

    Right now this just returns the subtotal unmodified. Each teammate's
    feature adds one pricing rule here. That is intentional, and it is
    exactly what will cause your merge conflict later.
    """
    total = subtotal

    # TODO: apply your assigned feature's pricing rule here

    return total


if __name__ == "__main__":
    example_subtotal = 100.0
    print(f"Total for a ${example_subtotal:.2f} cart: ${calculate_total(example_subtotal):.2f}")
