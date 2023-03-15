import pandas as pd
import matplotlib as plt
# Returns the count of how many uppercase letters are in the user's phrase.
def upper(phrase):
    count = 0
    for char in phrase:
        if char.isupper():
            count += 1
    return count
# Returns the count of how many lowercase letters are in the user's phrase
def lower(phrase):
    count = 0
    for char in phrase:
        if char.islower():
            count += 1
    return count
# Returns the count of how many digits are in the user's phrase
def digits(phrase):
    count = 0
    for char in phrase:
        if char.isdigit():
            count += 1
    return count
# Returns the count of how many whitespaces the user's phrase has.
def white_space(phrase):
    count = 0
    for char in phrase:
        if char == " ":
            count += 1
    return count
# Returns the count of how many other characters that aren't digit, alpha, and whitespace in the user's phrase.
def other(phrase):
    count = 0
    for char in phrase:
        if char.isdigit():
            count += 1
        if char.isalpha():
            count += 1
        if char == ' ':
            count += 1
    total = len(phrase) - count
    return total
# Returns the letter the user choose to look through the phrase and the count of how many times is in the phrase.
def letter_finder(phrase):
    count = 0
    letter = input('Enter a letter to find in your phrase: ').lower()
    for char in phrase:
        if letter == char.lower():
            count += 1
    print(f'The letter "{letter}" occurs {count} time(s)')
# Returns the word the user choose to look through the phrase and the count of how many times is in the phrase.
def word_finder(phrase):
    count = 0
    lower_case = phrase.lower()
    word = input('Enter a word to find in your phrase: ').lower()
    words = lower_case.split()
    for char in words:
        if char == word.lower():
            count += 1
    print(f'The word "{word}" occurs {count} time(s)')
# Runs throught the phase to see which words begin with vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') to convert the word to all uppercase.
# and converts words begin with vowels ('r', 's', 't', 'l', 'n', 'R', 'S', 'T', 'L', 'N') to be converted to lowercase.
def phrase_conversion(phrase):
    phrase = phrase.lower()
    words = phrase.split()
    for i in range(len(words)):
        if words[i].startswith('a'):
            words[i] = words[i].upper()
        if words[i].startswith('e'):
            words[i] = words[i].upper()
        if words[i].startswith('i'):
            words[i] = words[i].upper()
        if words[i].startswith('o'):
            words[i] = words[i].upper()
        if words[i].startswith('u'):
            words[i] = words[i].upper()
        if words[i].startswith('r'):
            words[i] = words[i].lower()
        if words[i].startswith('s'):
            words[i] = words[i].lower()
        if words[i].startswith('t'):
            words[i] = words[i].lower()
        if words[i].startswith('l'):
            words[i] = words[i].lower()
        if words[i].startswith('n'):
            words[i] = words[i].lower()
    new_phrase = " ".join(words)
    print(new_phrase)


def main():
    print()
    phrase = input('Enter a phrase: ')
    print()
    upper_count = upper(phrase)
    lower_count = lower(phrase)
    digit_count = digits(phrase)
    whitespace_count = white_space(phrase)
    other_count = other(phrase)
    total_count = len(phrase)

# Using pandas to give me a table view of the data from my text analysis.
    df = pd.DataFrame({
    'Char Type': ['Uppercase', 'Lowercase', 'Digits', 'White Space', 'Other', 'Total'],
    'Count': [upper_count, lower_count, digit_count, whitespace_count, other_count, total_count]})

# Plot chart
    ax = df.plot(kind='bar', x='Char Type', y='Count', legend=False)
    ax.set_ylabel('Count')
    ax.set_ylim(0, max(df['Count']) * 1.1) 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='x', length=0)
    print('---Text Analysis---')
    print(df.to_string(index=False))
    print()
    letter_finder(phrase)
    print()
    word_finder(phrase)
    print()
    phrase_conversion(phrase)

main()