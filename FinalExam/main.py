"""
Seth Healy
Final Exam
07/31/14
"""

import json
import webapp2
from urllib2 import urlopen, Request, build_opener


class MainHandler(webapp2.RequestHandler):
    # im getting my requests so that i can display the information
    def get(self):
        if self.request.GET:
            p = Page()

            musical = self.request.GET['music']

            mm = musicModel()
            searchdata = mm.songs(self, musical)
            mv = musicView()
            mv.music = searchdata



# this is where all my viewable data is contained
class musicView(object):
    def __init__(self):
        self.__music = musicDataObject()


# this is my model where all my data is contained.
class musicModel(object):
    def __init__(self, songs):
        self.__music = songs

        def song(self):
            musicrequest = Request('http://rebeccacarroll.com/api/music/music.json')
            #build the request
            request = Request("http://rebeccacarroll.com/api/music/music.json")

            # create an object that fetches pages for us
            opener = build_opener()

            #tell object what to fetch
            music = opener.open(request)
            musicresponse = urlopen(musicrequest)
            musicObject = json.load(musicresponse)

            #calling my dataobject using these.
            do = musicObject()
            do.musicObject = self.title
            do.musicObject = self.artist
            do.musicObject = self.length
            do.musicObject = self.year
            do.musicObject = self.label
            do.musicObject = self.cover
            do.musicObject = self.file
            return do


#creating my dataobject class where i can define all the and pull all the json information.


class musicDataObject(object):
    def __init__(self):
        self.musicObject = None
        self.title = ''
        self.artist = ''
        self.length = 0
        self.year = 0
        self.label = ''
        self.cover = ''
        self.file = ''


# this is where all my html is located.
class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title> Final exam </title>
</head>
<body>"""
    _content = '''
    <h1> Top 10 Pop Hits </h1>
    <a href="#"><button> Like a Rolling Stone </button></a>
    <a href="#"><button> Satisfaction </button></a>
    <a href="#"><button> Imagine </button></a>
    <a href="#"><button> What's Going On </button></a>
    <a href="#"><button> Respect </button></a>
    <a href="#"><button> Good Vibrations </button></a>
    <a href="#"><button> Hey Jude </button></a>
    <a href="#"><button> Smells Like Teen Spirit </button></a>
    <a href="#"><button> What'd I Say </button></a>
    '''
    _close = """
</body>
</html>"""

    def print_out(self):
        return self._head + self._content + self._close


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
