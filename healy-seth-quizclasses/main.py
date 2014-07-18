import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class Students(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>Inheritance</title>
</head>
<body>"""
    _content = ''

    _close = """
</body>
</html>"""

    def __init__(self):
        pass

    def print_out(self):
        return self._head + self._content + self._close


class Solider(Students):
    def chances(self):
        if 




app = webapp2.WSGIApplication([
                       ('/', MainHandler)
                  ], debug=True)
