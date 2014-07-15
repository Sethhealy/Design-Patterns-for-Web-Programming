import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()

        if self.request.GET:
            p.content = "First name: " + self.request.GET['fname']
            p.content += "<br />Last name: " + self.request.GET['lname']
            p.content += "<br />Email: " + self.request.GET['ename']
            p.content += "<br />City: " + self.request.GET['city']
            p.content += "<br />State: " + self.request.GET['state']
            p.content += "<br />Country: " + self.request.GET['country']


            self.response.write(p.print_out_page())

        else:
            self.response.write(p.print_out_form())


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
            <input type="checkbox" name="ps4" value="ps4">PS4<br>
            <input type="checkbox" name="xbox" value="xbox">Xbox1<br>
            <input type="checkbox" name="wiiu" value="wiiu">Wii U<br>
            <input type="checkbox" name="pc" value="pc">PC<br>

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
