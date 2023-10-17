def elim_char(string_source , string_elim , pos_string_tarjet):
    if pos_string_tarjet == 1:
        index_s = string_source.find(string_elim)
        return string_source[ : index_s] + string_source[index_s + 1 : ]
    elif pos_string_tarjet == 2:
        index_s = string_source.find(string_elim)
        index_s = string_source.find(string_elim , index_s + 1)
        return string_source[ : index_s] + string_source[index_s + 1 : ]
    else:
        return 'Error, need number of same character to eliminate'

print(elim_char('cosaos' , 'o' , 1))
print(elim_char('cosaos' , 'o' , 2))
print(elim_char('cosaos' , 'o' , 5))
print('\n')



def num_char_repeat_elim(string_source , pos_last_character , character , counter_last_string_tarjet):
    if string_source[ : pos_last_character].find(character) != -1:
        counter_last_string_tarjet += character
        result = string_source[ : pos_last_character +1].count(character)
    return result



def comp_anagrams(s1 , s2):
    j = -2
    last_pos = 0
    counter_last_string_tarjet = ''
    for character in s1:
        j += 1
        i = s2.find(character , last_pos)
#        last_character = s1[j]
        pos_last_character = j








        #COMO PUEDO HACER; PARA QUE EN LA 2º LINEA CONTANDO DESDE ESTA, SE EJECUTE, SIN QUE ESTÉ EN UN IF, PARA QUE SI SEA FALSO, QUE AÚN ASÍ SIGA EJECUTANDO EL CÓDIGO DE DEJABO?
        if j >= 0:
            pos_string_tarjet = num_char_repeat_elim(s1 , pos_last_character , character , counter_last_string_tarjet)








        s2 = elim_char(s2 , character , pos_string_tarjet)

        if i != -1:
            j += 1
            continue
        else:
            break
    if s2 == '':
        return True
    else:
        return False

print(comp_anagrams('abba' , 'bbaa'))
'''
#test:
a = 'cosaos'
index_a = a.find('o')
index_a = a.find('o' , index_a + 1)
result = a[ : index_a] + a[index_a + 1 : ]
print(result)
'''

a = 'abbab'





#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------











"""
def comp_anagrams(s1 , s2):
    j = 0
    for character in s1:
        i = s2.find(character)
        
        if i != -1:
            j += 1
            continue
        else:
            break
    if j == len(s1):
        return True
    else:
        return False

print(comp_anagrams('abba' , 'bbaa'))









def anagrams(word, words):
    def compare_anagrams(word1 , word2):
        for character in word1:



def compare_anagrams(word1 , word2):
    pos = 0
    counter = 0
    while counter <= len(word1):
        if word2.find(word1[pos]) != -1:
            print('eeeo')
            counter += 1
            pos += 1
        else:
            break
#    if counter == len(word1):
#        return 'is-anagram'
#    else:
#        return 'not-anagram'
#
print(compare_anagrams('aabb' , 'abba'))

'''
a = 'aabb'
b = 'abba'
i = 1
while b.find(a[0]) != -1 and i < 2:
    i += 1
    print('yes it is')
'''
'''
def compare_anagrams(word1 , word2):
    counter = 0
    pos = 0
    for character in word1:
        if word2.find(character) != -1:
            counter += 1
            continue
        else:
            return 'is-not-preanagram'
    if counter == len(word1):
        return 'is-anagram' , counter
    else:
        return 'not-anagram' , counter

print(compare_anagrams('bbaa' , 'abdnisj'))'''
"""