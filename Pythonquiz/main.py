"""
Seth Healy
07/10/14
Python Quiz
"""

width = raw_input("What is the Width of the equation? ")

height = raw_input("What is the Height of the equation? ")

def calc_area(h, w):
    square =  w * w
    return square
square = calc_area(width, height)
def calc_area1(h, w):
    rectangle = h * w
    return rectangle

if width == height:
    print "You must be a square" + " Your answer is" + int(calc_area)

else:
    print "You must be a rectangle" + " Your answer is" + int(calc_area1)


