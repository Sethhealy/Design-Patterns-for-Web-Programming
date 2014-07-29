import webapp2
from urllib import quote
from urllib2 import Request, urlopen
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):

        f = Page()
        f.inputs = [{'type': 'text', 'placeholder': 'Movies', 'name': 'movie'},
                    {'type': 'submit', 'name': 'submit', 'value': 'Get Your Movie'}]

        if self.request.GET:
            movie = self.request.GET['movie']
            mm = Moviemodel(movie)

            wv = MovieView()

        moviemodel = Moviemodel()
        movie = moviemodel.movie('iron man')

        page = Page()

        movieview = MovieView()
        movieview.movie = movie

        page._content = movieview.content

        self.response.write(page.print_out())


class MovieView(object):
    def __init__(self):
        self.__movie = MovieDataObject()
        self.content = ''

    @property
    def movie(self):
        pass

    @movie.setter
    def movie(self, movie):
        self.__movie = movie
        self.create_display()


    def create_display(self):
        self.content += self.__movie.title
        self.content += "Vote average: " + str(self.__movie.vote_average)
        self.content += "Vote count: " + str(self.__movie.vote_count)
        self.content += "(" + self.__movie.release_date + ')'
        self.content += "Overview: " + self.__movie.overview
        self.content += "<img src=https://image.tmdb.org/t/p/w300" + self.__movie.backdrop_path + '" />'
        self.content += "<br />"
        self.content += "Tagline: " + self.__movie.tagline
        self.content += "(" + str(self.__movie.budget) + ')'
        self.content += "High: " + str(self.__movie.runtime)
        self.content += '<img src="https://image.tmdb.org/t/p/w185' + self.__movie.poster_path + '" />'
        self.content += "<br />"
        self.content += "Adult: " + str(self.__movie.adult)
        self.content += "(" + str(self.__movie.revenue) + ')'
        self.content += "Status: " + self.__movie.status
        # self.content += "Collections: " + self.__movie.belongs_to_collection[1]
        self.content += "<br />"
        self.content += "Popularity: " + str(self.__movie.popularity)
        # self.content += "Spoken Language: " + self.__movie.spoken_language
        # self.content += "Production Companies: " + self.__movie.production_companies
        # self.content += "Production Countries: " + self.__movie.production_countries
        self.content += "<a href=" + self.__movie.homepage + '</a>'

        print self.content


class Moviemodel(object):


    def movie(self, title):
        headers = {
            'Accept': 'application/json'
        }

        # search

        safeTitle = quote(title, safe="%/:=&?~#+!$,;'@()*[]")

        print safeTitle

        searchRequest = Request(
            'http://api.themoviedb.org/3/search/movie?api_key=9ada58564fcdacbd21d0aca3ec33f0f1&query=' + safeTitle,
            headers=headers)

        searchResponse = urlopen(searchRequest)

        searchObject = json.load(searchResponse)

        movieId = searchObject['results'][0]['id']

        # movie

        movieRequest = Request('https://api.themoviedb.org/3/movie/' + str(movieId) + '?api_key=9ada58564fcdacbd21d0aca3ec33f0f1',
            headers=headers)

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
        do.spoken_languages = movieObject['spoken_languages']
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
    _content = '''

    <input type="search"><br>
    <input type="submit">

    <h1> {self.title} </h1>
    <p> {self.vote_count} {self.vote_average} </p>

'''
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
