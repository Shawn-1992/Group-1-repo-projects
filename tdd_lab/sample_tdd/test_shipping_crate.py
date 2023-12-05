from unittest.mock import Mock
from tdd_database import ProductDatabase
from shipping_crate import ShippingCrate
import pytest


# The following is an example of how the TDD program you create can be structured.
# The test outlines a program designed to simulate a
# shipping crate containing products of varying costs.

# Pytest fixture for establishing consistent data used across tests.
@pytest.fixture
def crate():
    return ShippingCrate(5)


# Test that products can be added to a list.
def test_can_add_product_to_crate(crate):
    crate.add("Coal")
    assert crate.quantity() == 1


# Test that ensures products are stored within a list.
def test_when_item_added_then_crate_contains_product(crate):
    crate.add("Coal")
    assert "Coal" in crate.get_products()


# Test that product capacity cannot exceed max.
def test_when_add_more_than_max_products_fail(crate):
    for i in range(5):
        crate.add("Coal")

    with pytest.raises(OverflowError):
        crate.add("Coal")


# Test that total cost is calculated correctly.
def test_can_get_total_cost(crate):
    crate.add("Coal")
    crate.add("Lumber")
    product_database = ProductDatabase()

    # Test using mock values for cost when database cannot be reached.
    def mock_get_product(product: str):
        if product == "Coal":
            return 1.0
        if product == "Lumber":
            return 2.0

    product_database.get = Mock(side_effect=mock_get_product)
    assert crate.get_total_cost(product_database) == 3.0
