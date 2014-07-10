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

# here im asking for the number for children you have

children = raw_input("How many children do you have? ")


print "Your name is " + first_name + " " + last_name + " and you are " + str(age) + " " + \
      "years old" + " and you have" + " " + children + " children"
# Here I have an if statement where if your said you have 0 children a message appears and if you said you
# did have children another message appeared
if int(children) == 0:
    print "Lucky you!!"
else:
    print "Lucky you"
