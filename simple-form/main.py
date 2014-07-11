import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # you cannot use self.response or self.request
        #both attributes of your mainhandler class
        p = Page()  #creating an instance "p" of class page


        if self.request.GET: #only do this is the form has been filled
           p.content ="First name: "+ self.request.GET['fname']
           p.content += "<br />Last name: "+ self.request.GET['lname']
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
    content = '''Hello there'''
    form_content = '''
        <form method="GET">
            <input type="text" placeholder ="First Name" name= "fname" />
            <input type="text" placeholder ="Last Name"  name= "lname"/>
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
