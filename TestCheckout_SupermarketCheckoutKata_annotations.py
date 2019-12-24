
import pytest
from Checkout import Checkout

def test_AssertTrue():
    assert True

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

# Can create an instance of the Checkout class
def test_CanInstantiateCheckout():
    co = Checkout()


# Can add an item price
def test_CanAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)


# Can add an item
def test_CanAddItem(checkout):
    checkout.addItem("a")


# Can calculate the current total
def test_CanCalculateTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


# Can add multiple items and get correct total
def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3


# Can add discount rules
def test_CanAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)


# Can apply discount rules to the total
@pytest.mark.skip
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2


# Exception is Trhwon for item Added without a Price
