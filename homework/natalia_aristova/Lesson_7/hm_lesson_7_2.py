words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for item in words.items():
    words_key, words_value = item
    print(words_key * int(words_value))
