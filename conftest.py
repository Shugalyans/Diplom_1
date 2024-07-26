import pytest
from unittest.mock import Mock
from praktikum.database import Database
from tests.data import MockBun, MockIngredient1, MockIngredient2


@pytest.fixture
def mok_bun():
    bun = Mock()
    bun.get_name.return_value = MockBun.NAME
    bun.get_price.return_value = MockBun.PRICE

    return bun


@pytest.fixture
def mok_ingredient_1():
    ingredient = Mock()
    ingredient.get_name.return_value = MockIngredient1.NAME
    ingredient.get_price.return_value = MockIngredient1.PRICE
    ingredient.get_type.return_value = MockIngredient1.TYPE
    return ingredient


@pytest.fixture
def mok_ingredient_2():
    ingredient = Mock()
    ingredient.get_name.return_value = MockIngredient2.NAME
    ingredient.get_price.return_value = MockIngredient2.PRICE
    ingredient.get_type.return_value = MockIngredient2.TYPE
    return ingredient


@pytest.fixture
def database():
    database = Database()
    return database