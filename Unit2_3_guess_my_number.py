max_number = 100
min_number = 0
answer_number = 50
got_number = 'h'
ask_phrase = 'Please think of a number between 0 and 100!'
guess_phrase = 'Is your secret number '
rule = "Enter 'h' to indicate the guess is too high. Enter " \
       "'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
end_phrase = 'Game over. Your secret number was:'

print(ask_phrase)
while got_number != 'c':
    print(guess_phrase, answer_number, '?', sep='')
    got_number = input(rule)
    if got_number == 'l':
        min_number = answer_number
        answer_number = (max_number + answer_number) // 2
    elif got_number == 'h':
        max_number = answer_number
        answer_number = (min_number + answer_number) // 2
    elif got_number == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
        continue


print(end_phrase, answer_number)


