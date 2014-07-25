import webapp2
from urllib2 import Request, urlopen


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')




        headers = {
          'Accept': 'application/json'
        }
        request = Request('https://api.themoviedb.org/3/movie/550?api_key=9ada58564fcdacbd21d0aca3ec33f0f1', headers=headers)

        response_body = urlopen(request).read()
        print response_body






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
