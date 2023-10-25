def disemvowel(string_):
    for character in string_:
        if character == 'a' or character == 'A' or character == 'e' or character == 'E' or character == 'i' or character == 'I' or character == 'o' or character == 'O' or character == 'u' or character == 'U':
            string_ = string_.replace(character , '')
        else:
            continue
    return string_

print(disemvowel('This website is for losers LOL!'))



#I didn't manage to do with "replace":
'''
#    i = ['a' , 'e' , 'i' , 'o' , 'u']
    i = 'aeiou'
    string_ = string_.replace( list(i) , '')
    return string_
print(disemvowel('This website is for losers LOL!'))'''