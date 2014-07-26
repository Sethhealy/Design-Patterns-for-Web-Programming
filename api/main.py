import webapp2
from urllib2 import Request, urlopen
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        headers = {
            'Accept': 'application/json'
        }
        request = Request('https://api.themoviedb.org/3/movie/550?api_key=9ada58564fcdacbd21d0aca3ec33f0f1',
                          headers=headers)

        response_body = urlopen(request)

        jsondoc = json.load(response_body)

        print jsondoc['genres'][0]['id']

class MovieView(object):
    def __init__(self):
        self.__dos = []
        self.content = ''

    @property
    def dos(self):
        pass

    @dos.setter
    def dos(self, arr):
        self.__dos = arr
        self.create_display()


    def create_display(self):
        for do in self.__dos:
            self.content += "Title: " + do.title
            self.content += "(" + do.release_date + ')'
            self.content += "Overview: " + do.overview
            self.content += "<img src=\"images/" + do.backdrop_path + '.png" />'
            self.content += "<br />"
            self.content += "Day: " + do.day
            self.content += "(" + do.date + ')'
            self.content += "High: " + do.high + '   Low: ' + do.low
            self.content += "<img src=\"images/" + do.code + '.png" />'
            self.content += "<br />"
            self.content += "Day: " + do.day
            self.content += "(" + do.date + ')'
            self.content += "High: " + do.high + '   Low: ' + do.low
            self.content += "<img src=\"images/" + do.code + '.png" />'
            self.content += "<br />"

        print self.content

class Moviemodel(object):
    """THis is the model class. it is sending a request to the yahoo api and getting
    xml from the api. It the sorts it into a data object"""

    def __init__(self):
        self.url = "https://api.themoviedb.org/3/movie/550?api_key=9ada58564fcdacbd21d0aca3ec33f0f1"



class MovieDataObject(object):


    def __init__(self):
        self.adult = ""
        self.backdrop_path = ""
        self.belongs_to_collection = ""
        self.budget = 0
        self.genres = []
        self.homepage = ""
        self.id = 0
        self.imdb_id = ""
        self.original_title = ""
        self.overview = ""
        self.popularity = 0
        self.poster_path = ""
        self.production_companies = []
        self.production_countries = []
        self.release_date = ""
        self.revenue = 0
        self.runtime = 0
        self.spoken_languages = []
        self.status = ""
        self.tagline = ""
        self.title = ""
        self.vote_average = 0
        self.vote_count = 0




class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>BestMovies</title>
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
