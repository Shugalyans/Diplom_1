from data import MockIngredient1

class TestIngredient:

    def test_get_name_return_name(self, mok_ingredient_1):
        assert mok_ingredient_1.get_name() == MockIngredient1.NAME

    def test_get_price_return_price(self, mok_ingredient_1):
        assert mok_ingredient_1.get_price() == MockIngredient1.PRICE

    def test_get_type_return_type(self, mok_ingredient_1):
        assert mok_ingredient_1.get_type() == MockIngredient1.TYPE