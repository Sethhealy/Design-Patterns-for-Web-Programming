import webapp2
from views import Page #you can use * for wildcard but is bad practice

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        #send in content we want
        p.content = "Sign the form:"
        p.css = "css/styles.css"
        p.title = "HI"
        #print out the content
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
