from src.loose_change import loose_change
def test_float_input():
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(4.935) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
