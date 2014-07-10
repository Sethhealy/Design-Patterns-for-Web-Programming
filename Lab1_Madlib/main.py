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

# Here im having the user pick a number for there hipster name
number = raw_input("Pick a number between 0-2 for your hipster name: ")

# Here im outputting the hipster name from the number the user chose.
name = ["smooth", "sparkly", "Funky fresh"]

print "Your hipster name is " + name[int(number)] + ' ' + first_name
# I made a dictionary and named it obj where i am pulling my variable first_name and my variable name with another
# variable for number pulling it into a string naming your hipster name so you can know how cool you are.

obj = {
    "first_name": first_name,
    "name": name[int(number)]
}

print "Or maybe it is " + obj["first_name"] + " " + obj["name"]

# This starts my loop where im looping a never ending song 6 times and outputting it.
song = '''
Welcome {user} To the sentence that never ends
It goes on and on my friend
ok well not forever
'''

output_sting = ''
user = last_name
for i in range(0, 6):
    output_sting += song

print output_sting.format(**locals())
