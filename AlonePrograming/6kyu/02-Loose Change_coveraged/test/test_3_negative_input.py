from src.loose_change import loose_change
def test_negative_input():
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-435) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
