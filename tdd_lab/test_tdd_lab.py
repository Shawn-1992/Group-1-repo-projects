# from tdd_lab import ShippingCrate
# import pytest

# There are three rules in test-driven development:
# Rule 1: Write a failing test first.
# Rule 2: Write the minimal amount of test code to fail.
# Rule 3: Write the minimal amount of code for the test to pass.

# Reminder: Like the filename, In order for pytest to detect tests,
# test functions require the 'test_' prefix.

# Writing a failing test:
# The following test outlines a necessary feature for adding a product to a list.
# def test_can_add_product():
#    crate = ShippingCrate()
#    crate.add("product")
#    assert crate.quantity() == 1

# The test fails due to having unresolved references.
# The failing test indicates a need for code that will pass the test.

# Writing code to pass the test:
# In the tdd_lab.py file under the ShippingCrate class define the following:

# placeholder1 should store the products we want to add to a list.
# def __init__() -> None:
#     self.products: List[str] = []


# placeholder2 should append the products to the list.
# def add(self, product: str):
#     self.products.append(product)


# placeholder3 should track the number of products in the list
# def quantity(self) -> int:
#     return len(self.products)

# placeholder4 should return the products in a list.
# def get_products(self) -> List[str]:
#    return self.products

# Refactoring the code:
# Edit the test code to be more modular.

# Pytest fixtures are a convenient way to define data to be reused across tests.
# Define crate to be reusable in subsequent tests using a pytest fixture:

# @pytest fixture
# def crate():
#     return ShippingCrate(5)

# Ensure crate is then passed to the test.
# def test_can_add_product(crate)
#     crate.add("product")
#     assert crate.quantity() == 1


# The outlined process above applies to every subsequent test.
# The program still needs a test that will outline the maximum
# amount of products that can be stored.

# Recall:
# def crate():
#     return ShippingCrate(5)

# In this instance the maximum number of products that can be stored
# will be five.

# def test_when_add_more_than_max_fail(crate):
#    for i in range(6)
#        crate.add("product")

# The test needs an exception using pytest.raises to pass the test
# when it fails.

#    with pytest.raises(OverflowError)
#        for i in range(6)
#            crate.add("product")

# The following test will fail and subsequently guide the creation
# of the necessary production code to make the test pass.

# placeholder1 should now implement a defined maximum.
# def __init__() -> None:
#     self.products: List[str] = []
#     self.max_quantity = max_quantity

# placeholder2 should now raise the necessary error to pass the test.
# def add(self, product: str):
#     if self.quantity() == self.max_quantity
#         raise OverflowError("No additional products can be added")
#     self.products.append(product)

# Now we refactor the code to be more maintainable by considering the changes
# one might make to the max quantity.

# def test_when_add_more_than_max_fail(crate):
#     for i in range(5)
#         crate.add("product")
#     with pytest.raises(OverflowError)
#         crate.add("product")

# The following code begins by initializing the maximum amount of products
# and adds one additional product to exceed that maximum and raise the error.


# Now the program requires a feature for calculating total cost
# We can use unittest mock values to assign varying costs to the products.

# cost_map is a dictionary that will assign costs to the products using
# a get method.

# def test_can_get_total_cost(crate):
#    crate.add("product")
#    crate.add("product2")
#    cost_map = {
#    "product1": 1.0,
#    "product2": 2.0
#    }
#    assert crate.get_total_cost(cost_map) == 3.0

# The test fails because there is no total_cost variable to reference.

# placeholder5 should now define the necessary variable to pass the test.
# def get_total_cost(self) -> int:
#     total_cost = 0
#     for product in self.products:
#         total_cost += cost_map.get(product)
#     return total_cost

# Now we refactor the code to be more scalable by considering the
# possible implementation of a database.

# class ProductDatabase:
#     def __init__(self) -> None:
#         pass

#     def get(self, product: str) -> float:
#         pass

# We can mock the behavior of the unimplemented database by using
# the unittest.mock library.

# def test_can_get_total_cost(crate):
#     crate.add("product1")
#     crate.add("product2")
#     crate.add("product3")
#     product_database = ProductDatabase()

# Implementing a mock method:

#     product_database.get = Mock(return_value=1.0)
#     assert crate.get_total_cost(product_database) == 3.0

# The test passes because each product is valued at a cost of one.
# However, we need to consider that products might have varying costs
# and refactor accordingly.

# Implementing a side_effect argument allows different values for different products.

#    def mock_get_product(product: str):
#       if product == "product1":
#           return 1.0
#       if product == "product2":
#           return 2.0

# You can find more information on using side effects in mock unit tests
# in the additional resources section of the documentation.

#       product_database.get = Mock(side_effect=mock_get_product)
#       assert crate.get_total_cost(product_database) == 3.0

# Continue in tdd_template.py and create a program using TDD cycles.
