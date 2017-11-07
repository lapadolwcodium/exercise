def is_anagram(word, eachword):
    if word.lower() == eachword.lower():
        return None

    str1_list = list(word.lower())
    str1_list.sort()
    str2_list = list(eachword.lower())
    str2_list.sort()

    if str1_list == str2_list:
        return eachword


def detect_anagrams(word, candidates):
    return_word = filter(lambda w: is_anagram(word, w), candidates)
    # print (return_word)
    return return_word
