text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
words = text.split()
new_text = []
for word in words:
    if word.endswith('.'):
        new_text.append(word.replace('.', 'ing.'))
    elif word.endswith(','):
        new_text.append(word.replace(',', 'ing,'))
    else:
        new_text.append(word + 'ing')
print(' '.join(new_text))
