import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        s = Submission()
        s._inputs = [{'type': 'text', 'placeholder': 'First Name', 'name': 'fname'},
                     {'type': 'text', 'placeholder': 'Last Name', 'name': 'lname'},
                     {'type': 'text', 'placeholder': 'Email', 'name': 'email'},
                     {'type': 'submit', 'name': 'submit', 'value': 'Go'}]
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


class Submission(Display):
    _inputs = ''
    form_start = "<form method=\"GET\" action=""/>"
    form_end="</form>"

    def __init__(self):
        Display.__init__(self)



    def inputinfo(self):
        _inputs=''
        for i in self._inputs:
            # for each item in our array
            _inputs += '<input type="' +i['type']+ '" name="'+i['name']+'" '
            if 'placeholder' in i:
                _inputs += ' placeholder="' + i['placeholder']+ '"'
            if 'value' in i:
                _inputs += ' value="'+i['value']+'"'
            _inputs += '/>'
        return _inputs

    def print_out(self):
        return self._head + self.form_start + self.inputinfo(self) + \
            self.form_end + self._close


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
