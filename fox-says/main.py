import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        A = AnimalPage()


        fox = Fox()
        self.response.write(fox.roar())



class AnimalPage(object):
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




class Animal(object):

    def __init__(self):

        self._sound = "meow"

        self.name = ""
        self.phylum = ""
        self.classification = ""
        self.family = ""
        self.genus = ""
        self.average = 0
        self.habitat = ""
        self.geo = ""

    def roar(self):
        return self._sound



class Fox(Animal):

    def __init__(self):
        self.name = "Fox"
        self.phylum = ""
        self.classification = ""
        self.family = ""
        self.genus = ""
        self.average = 0
        self.habitat = ""
        self.geo = ""
        self._sound = "asd"


class Cow(Animal):

    def __init__(self):
        self.name = "Cow"
        self.phylum = ""
        self.classification = ""
        self.family = ""
        self.genus = ""
        self.average = 0
        self.habitat = ""
        self.geo = ""
        self._sound = "woof"



class Horse(Animal):

    def __init__(self):
        self.name = "Horse"
        self.phylum = ""
        self.classification = ""
        self.family = ""
        self.genus = ""
        self.average = 0
        self.habitat = ""
        self.geo = ""
        self._sound = "woof"



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
