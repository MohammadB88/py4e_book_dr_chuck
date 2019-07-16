# This function counts the number of a specified letter is repeated in a word/text.
def letter_count(inp_string, inp_letter):
    text = inp_string
    count = 0
    for lett in text:
        if lett == inp_letter:
            count = count + 1
    # COUNT is a built in function counting the number of a specific letter/word which is repeated in a word/text.
    print(text.count(inp_letter))
    return count


inp_string = input('Please write down a word or a text:')
inp_letter = input('Which letter do you want me to count in this word/text?')

print(letter_count(inp_string, inp_letter))
