from typing import List


# typing is a Python standard library for assigning set variable types to list items.

# The following program is a sample program designed to simulate a
# shipping crate containing products of varying costs.

# Class for storing products in:
class ShippingCrate:
    # initializes a list to store products.
    def __init__(self, max_quantity: int) -> None:
        self.products: List[str] = []
        self.max_quantity = max_quantity


    # Function for adding products to a list.
    def add(self, product: str):
        if self.quantity() == self.max_quantity:
            raise OverflowError("No additional products can be added")
        self.products.append(product)

    # Function for storing products to a list.
    def quantity(self) -> int:
        return len(self.products)

    # Function for returning products in a list.
    def get_products(self) -> List[str]:
        return self.products

    # Function for calculating total cost of products in a list.
    def get_total_cost(self, cost_map):
        total_cost = 0
        for product in self.products:
            total_cost += cost_map.get(product)
        return total_cost


