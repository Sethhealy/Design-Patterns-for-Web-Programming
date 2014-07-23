import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        s = Submission()
        s.inputs=[{'type':'text', 'placeholder':'First Name', 'name':'fname'},
                  {'type':'text', 'placeholder':'Last Name', 'name':'lname'},
                {'type':'text','placeholder':'Email','name':'email'},
                {'type':'submit', 'name':'submit', 'value':'Go'}]
        self.response.write(s.print_out())




class Display(object):
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


class Submission(Display):










app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
