import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')






class Character(object):

   



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
