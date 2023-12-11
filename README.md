# phase-3-Toy_problem

Challenge 1: Converting 12-hour time to 24-hour time
Problem Description
Converting a 12-hour time to 24-hour time involves taking an input in the format of "hour:minute am/pm" and transforming it into a four-digit string representing the time in the 24-hour format. This README provides information about the challenge and instructions on how to implement the solution.

Task
Define a function that takes an hour (in the range of 1 to 12, inclusive), a minute (in the range of 0 to 59, inclusive), and a period ("am" or "pm") as input and returns a four-digit string representing the time in 24-hour format.

Examples
python
Copy code
convert_to_24_hour(8, 30, "am")  # Returns "0830"
convert_to_24_hour(8, 30, "pm")  # Returns "2030"
convert_to_24_hour(12, 0, "pm")  # Returns "1200"
Notes
Noon is represented as 12:00 pm, and midnight is represented as 12:00 am.
There is no 0 hour on the 12-hour clock.
Times just after midnight are denoted as, for example, 12:15 am, which translates to 0015 on the 24-hour clock.
Challenge 2: Two numbers are positive.
Problem Description
The task is to write a function that takes three integers (a, b, and c) as arguments and returns True if exactly two of the three integers are positive numbers (greater than zero), and False otherwise.

Examples
python
Copy code
two_positive_numbers(2, 4, -3)  # Returns True
two_positive_numbers(-4, 6, 8)  # Returns True
two_positive_numbers(4, -6, 9)  # Returns True
two_positive_numbers(-4, 6, 0)  # Returns False
two_positive_numbers(4, 6, 10)  # Returns False
two_positive_numbers(-14, -3, -4)  # Returns False
Challenge 3: Consonant value
Problem Description
Given a lowercase string with alphabetic characters only and no spaces, the task is to return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou". Each consonant is assigned a value: a = 1, b = 2, c = 3, ..., z = 26.

Examples
python
Copy code
highest_consonant_value("zodiacs")  # Returns 26
highest_consonant_value("strength")  # Returns 57
Explanation
For the word "zodiacs," the consonant substrings are "z," "d," and "cs" with values 26, 4, and 22, respectively. The highest value is 26.

For the word "strength," the consonant substrings are "str" and "ngth" with values 57 and 49, respectively. The highest value is 57.