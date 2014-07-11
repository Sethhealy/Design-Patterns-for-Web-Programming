"""
Seth Healy
07/10/14
Python Quiz
"""

width = raw_input("What is the Width of the equation? ")

height = raw_input("What is the Height of the equation? ")


def calc_area(h, w):
    if w == h:
        print "the Width and Height are the same making it a square " + str(w * h)
    else:
        print "this is a rectangle with " + str(w * h)


# mysong = '''
# {beer} Bottles of Beer on the Wall,  {beer} Bottles of Beer.. take one down and pass it around. Now you have
# {minus} bottles of beer on the wall!
# '''
#
# beer = 99
# minus = beer - 1
#
# for i in range(1, 99, -1):
#     minus -= beer
#
#     beer = minus
# output_string = ''
# for i in range(1, 99):
#     output_string += mysong
#
# print output_string.format(**locals())