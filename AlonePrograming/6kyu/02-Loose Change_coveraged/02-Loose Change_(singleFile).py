def loose_change(cents):
    change_value = {'Pennies': 1, 'Nickels': 5, 'Dimes': 10, 'Quarters': 25}
    change_dict = {'Pennies': 0, 'Nickels': 0, 'Dimes': 0, 'Quarters': 0}
    cents = int(cents)
    if cents <= 0:
        return change_dict
    else:
        pass
    while cents > 0:
        if cents >= change_value['Quarters']:
            change_dict['Quarters'] += 1
            cents -= change_value['Quarters']
            continue
        elif cents >= change_value['Dimes']:
            change_dict['Dimes'] += 1
            cents -= change_value['Dimes']
            continue
        elif cents >= change_value['Nickels']:
            change_dict['Nickels'] += 1
            cents -= change_value['Nickels']
            continue
        elif cents >= change_value['Pennies']:
            change_dict['Pennies'] += 1
            cents -= change_value['Pennies']
            continue
    return change_dict

#Test with assertions:
def assertions_test():
    #Test in the example codewars functionality
    assert loose_change(56) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
    assert loose_change(-435) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(4.935) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
    #The tests of the proof of the function functionality
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    print("All tests passed")
assertions_test()
