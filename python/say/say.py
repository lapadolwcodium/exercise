import inflect


def say(number):
    if number > 999999999999 or number < 0:
        raise AttributeError
    num_word = inflect.engine().number_to_words(int(number))
    # print(number, num_word.replace(",", ""))
    return num_word.replace(",", "")
