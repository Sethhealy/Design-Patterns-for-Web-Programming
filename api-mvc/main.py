import webapp2
import urllib2
from xml.dom import minidom


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # p=Page()
        f = FormPage()
        f.inputs = [{'type': 'text', 'placeholder': 'Zip Code', 'name': 'zip'},
                    {'type': 'submit', 'name': 'submit', 'value': 'Get Weather'}]
        # self.response.write(f.print_out())
        #if there is key value pair in the url

        if self.request.GET:
            zip = self.request.GET['zip']
            wm = Weathermodel(zip)  #instance of weather model


            wv = WeatherView()
            wv.dos = wm.dos #this passes the data from the model to the view

            #pass subview

            f.additional_view = wv.content
        self.response.write(f.print_out())





class WeatherView(object):
    def __init__(self):
        self.__dos = []
        self.content =''

    @property
    def dos(self):
        pass
    #this allows us to call create display when it gets teh data
    @dos.setter
    def dos(self, arr):
        self.__dos = arr
        self.create_display()


    def create_display(self):
        for do in self.__dos:
            self.content += "Day: " + do.day
            self.content += "(" + do.date + ')'
            self.content += "High: " + do.high + '   Low: ' + do.low
            self.content += "<img src=\"images/" + do.code + '.png" />'
            self.content += "<br />"
        print self.content

class Weathermodel(object):
    """THis is the model class. it is sending a request to the yahoo api and getting
    xml from the api. It the sorts it into a data object"""

    def __init__(self, z):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p="

        # create a request to send to server
        request = urllib2.Request(self.url + z)
        opener = urllib2.build_opener()
        # sends the request and gets response
        self.data = opener.open(request)
        self.parse()


    def parse(self):
        xmldoc = minidom.parse(self.data)
        forecast = xmldoc.getElementsByTagName("yweather:forecast")

        self.__dos = []

        for item in forecast:
            do = WeatherDataObject()
            do.day = item.attributes['day'].value
            do.date = item.attributes['date'].value
            do.high = item.attributes['high'].value
            do.low = item.attributes['low'].value
            do.code = item.attributes['code'].value
            do.description = item.attributes['text'].value
            # this adds the finished data object into the array
            self.__dos.append(do)
            # print self.__dos[1].day

    @property
    def dos(self):
        return self.__dos


class WeatherDataObject(object):
    """This class is just a big associative array for holding the info we need to pass
    between model and view"""

    def __init__(self):
        self.high = 0
        self.low = 0
        self.code = 0
        self.description = ""
        self.data = ""
        self.day = ""


class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>Model View Controller</title>
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


class FormPage(Page):
    __inputs = []
    _form_open = "<form method=\"GET\" action="" />"
    _form_close = "</form"
    additional_view = ''


    def __init__(self):
        # invoke constructor class
        Page.__init__(self)

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, i):
        self.__inputs = i

    def create_input(self):
        tot_inputs = ''
        for i in self.__inputs:
            # for each item in our array
            tot_inputs += '<input type="' + i['type'] + '" name="' + i['name'] + '" '
            if 'placeholder' in i:
                tot_inputs += ' placeholder="' + i['placeholder'] + '"'
            if 'value' in i:
                tot_inputs += ' value="' + i['value'] + '"'
            tot_inputs += '/>'
        return tot_inputs
        # Page.print_out(self)

    # this function overrides the print out function in the page class

    def print_out(self):
        return self._head + self._form_open + self.create_input() + \
               self._form_close + self._close + self.additional_view



        # accept an array of dictionaries
        # use to build out form input elements


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
