import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.content = "Start the Counter"
        self.response.write(p.printout())


class Page(object):
    title = ""
    header = """ <!DOCTYPE HTML>
<head><title>Counter</title>
</head>
<body>
"""


__counter = """
<button> Counter Clicker </button>
"""

__content = "Counter starts"
closer = """
    </body>
</html>"""


def print_out(self):
    return self.header + self.__content + self.closer + self.__counter


@__content.setter
def content(self, c):
    self.__content = c


class Counter(Page):
    def counter(count):
        count= 0

    def button(self):
        counting = count + 1



app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
