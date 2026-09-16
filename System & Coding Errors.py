
#There are many types of errors in technology. 

#1. Errors (System Level): These are usually fatal problems that the computer cannot easily recover from. 
#2. Exceptions (Application Level): These are errors that happen within your code's logic. 

#Types of Errors:

#1. Syntax Errors
#2. Runtime Errors (Exceptions)
#3. Semanitc Errors (Logical Errors)




# Syntax Errors: They occur when you violate the grammatical rules of the Python language.

#if True: 
    #print("Hello!")

# Runtime Errors: This would happen when a piece of code is syntactically correct but something goes wrong while 
# the program runs.

# Errors under Runtime:
# > ZeroDivision
# > TypeError
# > ValueError
# > IndexError
# > KeyError

#Index Error
#my_list = [1, 2]
#print(my_list[5])

#Zero Division
#result = 10 / 0

#Type Error
#statement = 'apple' + 5 

#ValueError
#int("Hello!")

#Key Error
#my_dict = {'a': 1}
#print(my_dict['b'])



# Semantic Errors (Logical Errors): The code is grammatically perfect and runs without crashing, 
# but the underlying logic is flawed, causing the program to output an incorrect result.

# The Scenario: Intending to calculate the mathematical average of two test scores (80 and 90).
# The expected result is 85.
score1 = 80
score2 = 90

# Semantic Error: Missing parentheses around the addition operation.
# Because of operator precedence (PEMDAS), division happens before addition.
average = score1 + score2 / 2

# How it manifests: The code executes smoothly, but outputs 125.0 instead of 85.
print("The average score is:", average)

#To fix this:
# Parentheses must be explicitly added to override the default operator precedence (PEMDAS). This forces Python to 
# execute the addition BEFORE the division.

# Corrected Code:
average = (score1 + score2) / 2

# How it manifests now: The logic is corrected, and it prints the expected result: 85.0
print("The corrected average score is:", average)