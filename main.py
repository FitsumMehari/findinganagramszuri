# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    list_of_word = list(word)
    list_of_anagram = list(anagram)

    for letter in list_of_word:
        if letter not in list_of_anagram:
            return False
    
    for letter in list_of_anagram:
        if letter not in list_of_word:
            return False

    return True