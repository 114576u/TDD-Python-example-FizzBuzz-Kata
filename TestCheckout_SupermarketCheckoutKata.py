
import pytest

from Checkout import Checkout

def test_AssertTrue():
    assert True

# Can create an instance of the Chckout class
def test_CanInstantiateCheckout():
    co = Checkout()

# Can add an item price
@pytest.mark.skip
def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)


# Can add an item
@pytest.mark.skip
def test_CanAddItem():
    co = Checkout()
    co.addItem("a")


# Can calculate the current total
def test_CanCalculateCurrentTotal():
    pass

# Can add multiple items and get correct total
# Can add discount rules
# Can apply discount rules to the total
# Exception is Trhwon for item Added without a Price