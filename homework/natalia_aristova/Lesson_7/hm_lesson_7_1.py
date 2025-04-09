number = 22
while True:
    user_input = int(input('Enter an integer: '))
    if user_input == number:
        print('Congratulations! You guessed it!')
        break
    else:
        print('Try again.')
        continue      # добавила continue, чтобы после сообщения "Try again" программа сразу просила ввести число.
