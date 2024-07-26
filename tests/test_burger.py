import pytest
from praktikum.burger import Burger
from data import MockBun, ingredient_set, MockIngredient1, MockIngredient2


class TestBurger:
    def test_set_buns(self, mok_bun):
        burger = Burger()
        burger.set_buns(mok_bun)

        assert burger.bun.get_name() == MockBun.NAME and burger.bun.get_price() == MockBun.PRICE

    @pytest.mark.parametrize('ingredient_name, ingredient_price, ingredient_type', ingredient_set)
    def test_add_ingredient(self, mok_ingredient_1, mok_ingredient_2, ingredient_name, ingredient_price, ingredient_type):
        burger = Burger()

        burger.add_ingredient(mok_ingredient_1)
        burger.add_ingredient(mok_ingredient_2)

        assert burger.ingredients == [mok_ingredient_1, mok_ingredient_2]

    def test_remove_ingredient(self, mok_ingredient_1, mok_ingredient_2):
        burger = Burger()

        burger.add_ingredient(mok_ingredient_1)
        burger.add_ingredient(mok_ingredient_2)

        burger.remove_ingredient(0)

        assert burger.ingredients == [mok_ingredient_2]

    def test_move_ingredient(self, mok_ingredient_1, mok_ingredient_2):
        burger = Burger()

        burger.add_ingredient(mok_ingredient_1)
        burger.add_ingredient(mok_ingredient_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mok_ingredient_2, mok_ingredient_1]

    def test_get_price(self, mok_bun, mok_ingredient_1, mok_ingredient_2):
        burger = Burger()

        burger.set_buns(mok_bun)
        burger.add_ingredient(mok_ingredient_1)
        burger.add_ingredient(mok_ingredient_2)

        total_price = burger.get_price()

        assert total_price == MockBun.PRICE * 2 + MockIngredient1.PRICE + MockIngredient2.PRICE

    def test_get_receipt(self, mok_bun, mok_ingredient_1, mok_ingredient_2):
        burger = Burger()

        burger.set_buns(mok_bun)
        burger.add_ingredient(mok_ingredient_1)
        burger.add_ingredient(mok_ingredient_2)

        receipt = (f'(==== {MockBun.NAME} ====)\n'
                   f'= начинка {MockIngredient1.NAME} =\n'
                   f'= соус {MockIngredient2.NAME} =\n'
                   f'(==== {MockBun.NAME} ====)\n'
                   '\n'
                   f'Price: {MockBun.PRICE*2+MockIngredient1.PRICE+MockIngredient2.PRICE}')

        assert burger.get_receipt() == receipt