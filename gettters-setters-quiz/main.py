import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())


class Page(object):
    title = ""
    header = """ <!DOCTYPE HTML>
<head><title>Counter</title>
</head>
<body>
"""


    counter = """
<button> Counter Clicker </button><br/>
"""

    counting = 0
    closer = """
    </body>
</html>"""


    def __init__(self):
        self.count = 0

    def print_out(self):
        return str(self.counter) + str(self.counting) + self.closer


class Counter(Page):
    def counter(self):
        self.count= 0

    def button(self):
        self.counting = self.count + 1



app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
