#WAP to input a letter and check vowel/consonant
Letter=input('Enter a letter ')
letter =Letter.lower()
match letter:
    case 'a'|'e'|'i'|'o'|'u':
        print('vowel')
    case other:
        print('consonant')  