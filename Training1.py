#The goal of this exercise is to convert a string to a new string where each character in the
# new string is "(" if that character appears only once in the original string, or ")" 
#if that character appears more than once in the original string. 
#Ignore capitalization when determining if a character is a duplicate.
def duplicate_encode(word):

    iter_word = str(word.lower())
    check_list = []
    formatted_list = []
    position = 0
    print('Checking word: {}'.format(iter_word))
    for i in iter_word:
        position += 1
        print('Checking item: {}'.format(i))
        if i not in check_list and i not in (iter_word[position:]):
            print('{} not found in the list[], so using ")" symbol'.format(i))
            check_list.append(i)
            i = '('
            formatted_list.append(i)
        else:
            print('{} found in the list[], so using "(" symbol'.format(i))
            check_list.append(i)
            i = ')'
            formatted_list.append(i)
    print('Result: {}'.format(''.join(map(str, formatted_list))))
    return ''.join(map(str, formatted_list))   
duplicate_encode('recede')