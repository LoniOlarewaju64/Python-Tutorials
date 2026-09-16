"""
In Python, error handling is done using try, except, else, raise and assert statements.

TRY: 
This block contains the code that may cause an exception. 

EXCEPT:
This block catches and handles exceptions.

ELSE: 
This block runs only if no exception occurs.

FINALLY:
This block always executes whether an exception occurs or not. 

RAISE: 
This statement is used to intentionally generate an exception. 

ASSERT: 
This is used for debugging. 

"""

# Examples

# Catching a Specific Exception 
#try: 
   # x = 10/0 
# except ZeroDivisionError:
    #print("Cannot divide by zero.")


# Catching multiple exceptions 

#try: 
   # number = int(input("Enter any number:")) 
#except ValueError:
   # print("Invald number...")
#except KeyboardInterrupt:
 #   print("Program interrupted!")


# Catching all exceptions

#try: 
#    list = [1, 2, 3]
#    print(list[4])
#except Exception as error: 
#    print("Error:", error)

# ELSE
#try: 
#    x = int(input("Enter a number:")) ValueError, KeyboardInterrupt
#except ValueError: 
#    print("Invalid input.")
#else: 
#    print(f"You entered {x}")#

# Finally...

#error = False #

#try:
#    x = int(input("Enter a number:"))
#except ValueError:
#    error = True 
#    print("Invalid input. Try again.")

#finally:
 #   print(error)


# Raise Statement 

#def withdraw(balance, amount):
 #   if amount <= 0:
  #      raise ValueError("Withdrawl amount must be greater than 0.")
   # if amount > balance:
    #    raise ValueError("Insufficient funds for this withdrawl.")
   # return balance - amount

#balance = withdraw(5000, 0)
#print(balance)

# SYNTAX 
# ASSERT Condition, "Error message if the condition is false."

#def calculate_discount(price, discount_percentage):
 #   assert 0 <= discount_percentage <= "Discount percentage is out of valid range."
  #  return price * (1 - (discount_percentage/100))

#new_price = calculate_discount(1000, 20)
#print(new_price)


# Exercise: Writing function 'divide_numbers(a, b). 

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
divide_numbers(10, 0) 
