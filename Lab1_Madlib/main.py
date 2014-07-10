"""
Seth Healy
07/08/14
Lab 1 Madlib
ALWAYS AT THE TOP
"""
# Here im asking the user to input their first name

first_name = raw_input("Type your First Name: ")

# Here i am asking the user to input their last name

last_name = raw_input("Type your Last Name: ")

# Here im asking for the user to input the year they were born

year = raw_input("What year were you born ")

# Here im using a function to calculate your age from the output of the previous input field


def age_calc(y, b):
    a = b - y
    return a

#here im calculating the information
age = age_calc(int(year), 2014)
