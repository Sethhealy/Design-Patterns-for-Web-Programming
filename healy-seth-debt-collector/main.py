import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Person()
        #send in content we want
        p.content = "Sign the form:"
        p.css = "css/styles.css"
        p.title = "HI"
        #print out the content
        self.response.write(p.print_out())






class Person(object):

    title =""
    __css ="css/styles.css"
    header = """ <!DOCTYPE HTML>
<head><title></title>
<link rel="stylesheet" type="text/css" href="{self.css}" />
</head>
<body>
"""
    __content = "welcome peasants"
    closer = """
    </body>
</html>"""

    def __init__(self):
        self.name = ""
        self.age = 0
        self.degree = ""
        self.grad = ""
        self.cost = ""

    def print_out(self):
        return self.name + str(self.age) + self.degree + self.grad + self.cost





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
