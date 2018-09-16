def get_user_word():
    return input("Please enter a word: ")


def print_length_word(user_word):
    if len(user_word) < 5:
        print("Your word is less than 5 characters")
    elif len(user_word) > 5:
        print("Your word is greater than 5 characters")
    else:
        print("Your word is equal to 5 characters")


word = get_user_word()
print_length_word(word)
