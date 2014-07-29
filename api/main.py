import webapp2
from urllib2 import Request, urlopen, build_opener
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

        f = Page()
        f.inputs = [{'type': 'text', 'placeholder': 'Movies', 'name': 'movie'},
                    {'type': 'submit', 'name': 'submit', 'value': 'Get Your Movie'}]

        if self.request.GET:
            movie = self.request.GET['movie']
            mm = Moviemodel(movie)

            wv = MovieView()

        moviemodel = Moviemodel()
        movie = moviemodel.movie('title')

        print movie.title

        page = Page()

        movieview = MovieView()
        movieview.movie = movie

        page._content = movieview.content

        self.response.write(page.print_out())


class MovieView(object):
    def __init__(self):
        self.__movie
        self.content = ''

    @property
    def movie(self):
        pass

    @movie.setter
    def __movie(self, movie):
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
        self.content += "<a href=" + self.__movie.homepage + '</a>'

        print self.content

    @movie.setter
    def movie(self, value):
        self._movie = value


class Moviemodel(object):
    """THis is the model class. it is sending a request to the yahoo api and getting
    xml from the api. It the sorts it into a data object"""

    def __init__(self):
        self.__movie = MovieDataObject()

    def movie(self, title):

        headers = {
            'Accept': 'application/json'
        }

        # search

        searchRequest = Request('http://api.themoviedb.org/3/search/movie?api_key=9ada58564fcdacbd21d0aca3ec33f0f1&query=matrix', headers=headers)

        searchResponse = urlopen(searchRequest)

        searchObject = json.load(searchResponse)

        movieId = searchObject['results'][0]['id']

        # movie

        movieRequest = Request('https://api.themoviedb.org/3/search/' + 'movieId' + '?api_key=9ada58564fcdacbd21d0aca3ec33f0f1', headers=headers)

        movieResponse = urlopen(movieRequest)

        movieObject = json.load(movieResponse)

        # parse

        do = MovieDataObject()
        do.title = movieObject['title']
        do.vote_average = movieObject['vote_average']
        do.vote_count = movieObject['vote_count']
        do.release_date = movieObject['release_date']
        do.overview = movieObject['overview']
        do.backdrop_path = movieObject['backdrop_path']
        do.tagline = movieObject['tagline']
        do.budget = movieObject['budget']
        do.runtime = movieObject['runtime']
        do.poster_path = movieObject['poster_path']
        do.adult = movieObject['adult']
        do.revenue = movieObject['revenue']
        do.status = movieObject['status']
        do.belongs_to_collection = movieObject['belongs_to_collection']
        do.popularity = movieObject['popularity']
        do.spoken_language = movieObject['spoken_language']
        do.production_companies = movieObject['production_companies']
        do.production_countries = movieObject['production_countries']
        do.homepage = movieObject['homepage']

        return do


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
