import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        animalPage = AnimalPage()

        animal = Animal()

        if self.request.GET:

            if self.request.GET.has_key("animal"):

                if self.request.GET["animal"] == "horse":
                    animal = Horse()

                if self.request.GET["animal"] == "cow":
                    animal = Cow()

                if self.request.GET["animal"] == "fox":
                    animal = Fox()

        animalPage._content = animal.roar()

        self.response.write(animalPage.print_out())



class AnimalPage(object):

    person= None
    _header = """<!DOCTYPE HTML>
<head>
    <title>What Does the Fox Say</title>
</head>
<body>"""
    _content = ''

    _close = """
</body>
</html>"""

    def __init__(self):
        pass

    def print_out(self):
        return self._header + self._content + self._close


    def render(self):
        # generate content
        self._content += self.header.format(**locals())



        if bool(self.animal):
            self._content += "<div class='names'>"
            self._content += "<p>" + "Animal name: " + self.animal.name + "</p>"
            self._content += "<p>" + "Phylum: " + self.animal.phylum + "</p>"
            self._content += "<p>" + "Classification: " + self.animal.classification + "</p>"
            self._content += "<p>" + "Family: " + self.animal.family + "</p>"
            self._content += "<p>" + "Genus: " + self.animal.genus + "</p>"
            self._content += "<p>" + "Average: " + str(self.animal.average) + "</p>"
            self._content += "<p>" + "Habitat: " + self.animal.habitat + "</p>"
            self._content += "<p>" + "Geo: " + self.animal.geo +"</p>"
            self._content += "<p>" + "Sound: " + self.animal._sound +"</p>"
            self._content += "</div>"
        self._content += self.footer



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
        self._sound = "moo"



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
