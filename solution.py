def convert_to_24_hour(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    print(f'{hour:02d}{minute:02d}')
convert_to_24_hour(2,30,'pm')

def two_positive(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    print(positive_count == 2)
two_positive(2,3,5)

def solve(word):
    vowels = 'aeiou'
    max_value = 0
    consonants = [ord(letter) - ord('a') + 1 for letter in word if letter not in vowels]
    i = 0
    while i < len(consonants):
        j = i
        current_value = 0
        while j < len(consonants) and consonants[j] > 0:
            current_value += consonants[j]
            j += 1
        max_value = max(max_value, current_value)
        i = j + 1
    print(max_value)def solve(word):
    vowels = 'aeiou'
    max_value = 0
    consonants = [ord(letter) - ord('a') + 1 for letter in word if letter not in vowels]
    i = 0
    while i < len(consonants):
        j = i
        current_value = 0
        while j < len(consonants) and consonants[j] > 0:
            current_value += consonants[j]
            j += 1
        max_value = max(max_value, current_value)
        i = j + 1
    print(max_value)
solve(' qwerty')
solve(' qwerty')