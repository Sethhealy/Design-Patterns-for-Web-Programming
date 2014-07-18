import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>Inheritance</title>
</head>
<body>"""
    __content = ''

    close = """
</body>
</html>"""


class Custodian(Page):
    def odds(self):
        return 4 + 0


    def __init__(self):
        pass

    def print_out(self):
        return self._head + self.__content + self.close

    @content.setter
    def content(self, c):
        self.__content = c


class Solider(Page):
    def chances(self):
        return 4 + 4


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
