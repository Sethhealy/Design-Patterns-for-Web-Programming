import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        A = AnimalPage()

        animal1 = Animal()
        animal1.name = "Fox"
        animal1.phylum = " "
        animal1.classification = " "
        animal1.family = ""
        animal1.genus = ""
        animal1.average = 0
        animal1.habitat = ""
        animal1.geo = ""


        animal2 = Animal()
        animal2.name = "Fox"
        animal2.phylum = " "
        animal2.classification = " "
        animal2.family = ""
        animal2.genus = ""
        animal2.average = 0
        animal2.habitat = ""
        animal2.geo = ""



        animal3 = Animal()
        animal3.name = "Fox"
        animal3.phylum = " "
        animal3.classification = " "
        animal3.family = ""
        animal3.genus = ""
        animal3.average = 0
        animal3.habitat = ""
        animal3.geo = ""



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
        self.name = ""
        self.phylum = ""
        self.classification = ""
        self.family = ""
        self.genus = ""
        self.average = 0
        self.habitat = ""
        self.geo = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
