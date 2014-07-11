"""
Seth Healy
07/10/14
Python Quiz
"""

width = raw_input("What is the Width of the equation? ")

height = raw_input("What is the Height of the equation? ")

# i called the function here to make the calculations for the square and rectangle
def calc_area(h, w):
    if w == h:
        print "the Width and Height are the same making it a square " + str(w * h)
    else:
        print "this is a rectangle with " + str(w * h)

calc_area(14.1421, 14.1421)
calc_area(14.1421, 1.4142)


def beer(count):
    for i in range(count):
        print str(count) + " Bottles of Beer on the Wall, " + str(count) + ' ' + "Bottles of Beer.. " \
                           "take one down and pass it around. Now you have " + str(count-1) + ' ' +\
                           "bottles of beer on the wall!"
        count -= 1

beer(10)