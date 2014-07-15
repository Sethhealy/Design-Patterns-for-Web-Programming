import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):






class Page(object):
    header = """<!DOCTYPE>
    <html>
        <head>
            <link rel="stylesheet" href="styles/style.css" type="text/css"/>
            <title>Welcome to my page </title>
        </head>
        <body>


    """
    content = '''Please Work'''
    form_content = '''
        <form method="GET">
            <input type="text" placeholder ="First Name" name= "fname" />
            <input type="text" placeholder ="Last Name"  name= "lname"/>
            <input type="text" placeholder ="Email"  name= "ename"/>
            <input type="text" placeholder ="City"  name= "city"/>
            <input type="text" placeholder ="State"  name= "state"/>
            <input type="text" placeholder ="Country"  name= "country"/>
            <input type="submit" value ="submit info" />
        </form>
    '''
    closer = '''
     </body>
     </html>'''

    def __init__(self):
        pass

    def print_out_page(self):
        return self.header + self.content + self.closer

    def print_out_form(self):
        return self.header + self.form_content + self.closer

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
