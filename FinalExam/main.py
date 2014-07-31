'''
Seth Healy
Final Exam
07/31/14
'''

import json
import webapp2
from urllib2 import urlopen, Request



class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET:
            searchedmusic = self.request.GET['music']
            mm = musicModel()
            searchdata = mm.music(searchedmusic)
            mv = musicView()
            mv.music = searchdata


class musicView(object):
    def __init__(self):
        self.__music =musicDataObject()



class musicModel(object):
    def music(self,title):


        musicrequest = Request('http://rebeccacarroll.com/api/music/music.json')
        musicresponse = urlopen(musicrequest)
        musicObject = json.load(musicresponse)


        do = musicDataObject()
        do.musicObject['title'] = self.title
        do.musicObject['artist'] =
        do.musicObject['length'] =
        do.musicObject['year'] =
        do.musicObject['label'] =
        do.musicObject['cover'] =
        do.musicObject['file'] =
        return do


class musicDataObject(object):
    def __init__(self):
        self.title = ''
        self.artist = ''
        self.length = 0
        self.year = 0
        self.label = ''
        self.cover = ''
        self.file = ''

class Page():


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
