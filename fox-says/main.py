import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hi!')




class Page(object):
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




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
