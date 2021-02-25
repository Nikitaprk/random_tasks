# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
# untouched.

def pig_it(text):
    text = text.split(' ')
    new_string = ''
    for word in text:
        new_string = new_string + word[1:] + word[0] + 'ay' + ' '
    if new_string[-4] == "?" or new_string[-4] == "!":
        new_string = new_string[:-3]
    return new_string.strip()


print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
print(pig_it('Quis custodiet ipsos custodes ?'))  # uisQay ustodietcay psosiay ustodescay ?
print(pig_it(('O tempora o mores !')))  # Oay emporatay oay oresmay !
