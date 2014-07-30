import webapp2
from urllib import quote
from urllib2 import Request, urlopen
import json


class MainHandler(webapp2.RequestHandler):
    # calling the function for my pulling the data
    def get(self):
        # Calling my page function and naming it page so i can use it later
        page = Page()
        #here i am using an if statement for my GET request.
        if self.request.GET:
            queryMovie = self.request.GET['movie']
            #I named my movieModel mm for later usage
            mm = Moviemodel()
            #im adding a variable dataMovie and making it equal to mm.movie(queryMovie) for my searching
            dataMovie = mm.movie(queryMovie)
            # Im using mv for movieView function so i can use it later
            mv = MovieView()
            # im using mv.movie=dataMovie for viewing of the data
            mv.movie = dataMovie

            #calling my page content to add my movie view content
            page._content += mv.content
        # my else is  set in place for my new view for all my added content
        else:
            #Im naming homepage= HomeView function that im using later
            homePage = HomeView()
            page._content = homePage.content

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
        self.content += "<br />"
        if self.__movie.poster_path:
            self.content += "<div class='poster'>" + '<img src="https://image.tmdb.org/t/p/w185' + self.__movie.poster_path + '" />' \
                            + '</div>'
        self.content += "<div class='information'>" + "<div class='title'>" + self.__movie.title
        self.content += '<div class="space">' "</div>" "(" + self.__movie.release_date + ')' + '</div>'
        self.content += "<div class='large'>" "Vote average: " + str(self.__movie.vote_average) + '</div>'
        self.content += '<div class="large">' "Vote count: " + str(self.__movie.vote_count) + '</div>'+ "</div>"
        self.content += "<br />"
        self.content += '<div class="overview">' + "Overview: " \
                        + self.__movie.overview + '</div>'
        self.content += '<div class="tag">' + "Tagline: " + self.__movie.tagline + '</div>'


        self.content += "<br />"

        self.content += "<div class='money'>" + '<div class="budget">' + "Budget:" + " (" + str(self.__movie.budget) + ')' + '</div>'
        self.content += '<div class="runtime">' + "Runtime:" + str(self.__movie.runtime) + " Minutes" + "</div>"
        self.content += "<br />"
        if self.__movie.adult:
            self.content += "<div class='adult'>" + "Adult: " + str(self.__movie.adult) + '</div>'
        self.content += '<div class="revenue">' + 'Revenue: ' + "(" + str(self.__movie.revenue) + ')' + '</div>'
        self.content += "<div class= 'status'>" + "Status: " + self.__movie.status + '</div>'
        self.content += "Popularity: " + str(self.__movie.popularity)
        self.content += "<a href=" + self.__movie.homepage + '</a>' + "</div>"
        if self.__movie.backdrop_path:
                    self.content += '<div class="backdrop">' "<img src=https://image.tmdb.org/t/p/w300" + self.__movie.backdrop_path + '" />' \
                                    + '</div>'
        print self.content


class Moviemodel(object):
    def movie(self, title):
        headers = {
            'Accept': 'application/json'
        }

        # search

        safetitle = quote(title, safe="%/:=&?~#+!$,;'@()*[]")

        print safetitle

        searchrequest = Request(
            'http://api.themoviedb.org/3/search/movie?api_key=9ada58564fcdacbd21d0aca3ec33f0f1&query=' + safetitle,
            headers=headers)

        searchresponse = urlopen(searchrequest)

        searchobject = json.load(searchresponse)

        movieid = searchobject['results'][0]['id']

        # movie

        movierequest = Request(
            'https://api.themoviedb.org/3/movie/' + str(movieid) + '?api_key=9ada58564fcdacbd21d0aca3ec33f0f1',
            headers=headers)

        movieresponse = urlopen(movierequest)

        movieObject = json.load(movieresponse)

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
        do.popularity = movieObject['popularity']
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


class HomeView(object):
    def __init__(self):
        self.content = ''



class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>BestMovies</title>
    <link rel="stylesheet" href="styles/styles.css" type="text/css"/>
</head>
<body>
<div class="wrapper">
    <header>Welcome to where the best movies gather</header>


    <div class="form"><form action="/">
        <input type="search" name="movie" required>
        <input type="submit">
    </form></div>
<div class="clear"></div>
"""
    _content = ''
    _close = """
    </div>
</body>
</html>"""

    def __init__(self):
        pass

    def print_out(self):
        return self._head + self._content + self._close


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
