
def check_message(message, to_check):
    split_word = message.lower().split("-")
    print(split_word)
    if split_word[1] == to_check.lower():
        return True
    elif split_word[0] == '':
        return False


print(check_message("-world", "World"))

