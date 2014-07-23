import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #p=Page()
        f = FormPage()
        f.inputs=[{'type':'text', 'placeholder':'Zip Code', 'name':'zip'},
                {'type':'submit', 'name':'submit', 'value':'Get Weather'}]
        #self.response.write(f.print_out())
        #if there is key value pair in the url

        if self.request.GET:
            zip = self.request.GET['zip']

        #build the request
            request = urllib2.Request("http://xml.weather.yahoo.com/forecastrss?p="+zip)

        # create an object that fetches pages for us
            opener = urllib2.build_opener()

        #tell object what to fetch
            data = opener.open(request)
        #parse the info
            xmldoc = minidom.parse(data)

            titles = xmldoc.getElementsByTagName("title")


            forecast = xmldoc.getElementsByTagName("yweather:forecast")
            c=""
            for i in forecast:
                c += i.attributes['day'].value + "(" + i.attributes['date'].value +") <br/>"
                c+= "High: " + i.attributes['high'].value + '&deg' + "::: " + "Low: " + i.attributes['low'].value + '&deg'
                c+= "<img src=\"images/" + i.attributes['code'].value + '.png" width="30" />'
                c+= '<br/>'


            self.response.write(c)





        else:
            self.response.write(f.print_out())


class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>Inheritance</title>
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
        tot_inputs=''
        for i in self.__inputs:
            # for each item in our array
            tot_inputs += '<input type="' +i['type']+ '" name="'+i['name']+'" '
            if 'placeholder' in i:
                tot_inputs += ' placeholder="' + i['placeholder']+ '"'
            if 'value' in i:
                tot_inputs += ' value="'+i['value']+'"'
            tot_inputs += '/>'
        return tot_inputs
        #Page.print_out(self)
    #this function overrides the print out function in the page class

    def print_out(self):
        return self._head + self._form_open +self.create_input() +\
               self._form_close + self._close



        #accept an array of dictionaries
        # use to build out form input elements



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
