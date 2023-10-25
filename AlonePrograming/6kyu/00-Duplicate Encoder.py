def duplicate_encode(word):
    string_result = ''
    for character in (word.lower()):
        if word.lower().count(character) > 1:
            string_result += ')'
        else:
            string_result += '('
    return string_result
print(duplicate_encode('pin'))
print(duplicate_encode('pinp'))