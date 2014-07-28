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


        movieModel = Moviemodel()
        movie = movieModel.movie('title')

        page = Page()

        movieView = MovieView()
        movieView.movie = movie

        page._content = movieView.content

        self.response.write(page.print_out())


class MovieView(object):
    def __init__(self):
        self.__movie
        self.content = ''

    @property
    def movie(self):
        pass

    @movie.setter
    def movie(self, movie):
        self.__movie = movie
        self.create_display()


    def create_display(self):
        self.content += "Title: " + self.__movie.title
        self.content += "Vote average: " + self.__movie.vote_average
        self.content += "Vote count: " + self.__movie.vote_count
        self.content += "(" + self.__movie.release_date + ')'
        self.content += "Overview: " + self.__movie.overview
        self.content += "<img src=\"images/" + self.__movie.backdrop_path + '.jpg" />'
        self.content += "<br />"
        self.content += "Tagline: " + self.__movie.tagline
        self.content += "(" + self.__movie.budget + ')'
        self.content += "High: " + self.__movie.runtime
        self.content += "<img src=\"images/" + self.__movie.poster_path + '.jpg" />'
        self.content += "<br />"
        self.content += "Adult: " + self.__movie.adult
        self.content += "(" + self.__movie.revenue + ')'
        self.content += "Status: " + self.__movie.status
        self.content += "Status: " + self.__movie.belongs_to_collection
        self.content += "<br />"
        self.content += "Popularity: " + self.__movie.popularity
        self.content += "Spoken Language: " + self.__movie.spoken_language
        self.content += "Production Companies: " + self.__movie.production_companies
        self.content += "Production countries: " + self.__movie.production_countries
        self.content += "Status: " + self.__movie.status
        self.content += "<a href=" + self.__movie.homepage + '</a>'

        print self.content


class Moviemodel(object):
    """THis is the model class. it is sending a request to the yahoo api and getting
    xml from the api. It the sorts it into a data object"""

    def __init__(self):
        self.url = "https://api.themoviedb.org/3/movie/550?api_key=9ada58564fcdacbd21d0aca3ec33f0f1"

    # create a request to send to server
        request = urllib2.Request(self.url)
        opener = urllib2.build_opener()
        # sends the request and gets response
        self.data = opener.open(request)


    def movie(self, title):
        pass


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
