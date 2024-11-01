def word_count(string):
    if len(string) != 0:
        word_list = string.split(' ')
        return len(word_list)
    else:
        return 0
