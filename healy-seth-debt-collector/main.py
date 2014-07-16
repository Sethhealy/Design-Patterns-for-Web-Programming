import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Person()

        if self.request.GET:
            p.content = "<div class=\"wrapper\">"
            p.content += "Name: " + self.request.GET['name']
            p.content += "Age: " + self.request.GET['age']
            p.content += "Degree: " + self.request.GET['degree']
            p.content += "Grad: " + self.request.GET['grad']
            p.content += "Cost: " + self.request.GET['cost']
            p.content += "Interest after 5 years: " + self.request.GET['five']
            p.content += "Interest after 10 years: " + self.request.GET['ten']
            p.content += "Interest after 15 years: " + self.request.GET['fifteen']
            p.content += "</div>"


class Person(object):
    title = ""
    __css = "css/styles.css"
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
