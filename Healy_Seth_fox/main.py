import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        a = AnimalPage()

        animal = Animal()

        if self.request.GET:
            if self.request.GET.has_key("animal"):
                if self.request.GET["animal"] == "horse":
                    animal = Horse()
                if self.request.GET["animal"] == "cow":
                    animal = Cow()
                if self.request.GET["animal"] == "fox":
                    animal = Fox()
        a.animal = animal
        a.render()
        self.response.write(a.print_out())


class AnimalPage(object):
    animalarray = []
    animal = None

    title = ""

    header = """ <!DOCTYPE HTML>
<head>
    <title>What does the Fox say</title>
    <link rel="stylesheet" href="styles/styles.css" type="text/css"" />
</head>
<body><div class="wrapper">
"""

    footer = """</div></body>
</html>"""
    content2 = """

    """

    content = """

        <h1> What does the fox say </h1>
        <p> Though there is great diversity in the animal kingdom, animals
        can be distinguished from the other kingdoms by a set of characteristics.
        Though other types of life may share some of these characteristics, the set
        of characteristics as a whole provide a distinction from the other kingdoms.</p>

        <ol>
            <li>    Animals are multicellular. </li>
            <li>    Animals are heterotrophic, obtaining their energy by consuming
            energy-releasing food substances. </li>
            <li>    Animals typically reproduce sexually. </li>
            <li>    Animals are made up of cells that do not have cell walls.</li>
            <li>    Animals are capable of motion in some stage of their lives.
            <li>    Animals are able to respond quickly to external stimuli as a result of
            nerve cells, muscle or contractile tissue, or both. </li>
        </ol>
        <div class='links'>
        <a href="/?animal=fox">Fox</a>
        <div class="space"></div>
        <a href="/?animal=cow">Cow</a>
        <div class="space"></div>
        <a href="/?animal=horse">Horse</a>
        <div class="space"></div>
        </div>
    """
    closer = ""

    def __init__(self):
        pass

    def print_out(self):
        return self.header + self.content + self.content2 + self.closer

    def render(self):
        self.content += self.header.format(**locals())

        if bool(self.animal):
            self.content += "<div class='names'>"
            self.content += '<img src="/images/' + self.animal.image + '.jpg" />'
            self.content += "<p>" + "Animal name: " + self.animal.name + "</p>"
            self.content += "<p>" + "Phylum: " + self.animal.phylum + "</p>"
            self.content += "<p>" + "Classification: " + self.animal.classification + "</p>"
            self.content += "<p>" + "Family: " + self.animal.family + "</p>"
            self.content += "<p>" + "Genus: " + self.animal.genus + "</p>"
            self.content += "<p>" + "Average: " + str(self.animal.average) + " Years</p>"
            self.content += "<p>" + "Habitat: " + self.animal.habitat + "</p>"
            self.content += "<p>" + "Geo: " + self.animal.geo + "</p>"
            self.content += "<p>" + "Sound: " + self.animal._sound + "</p>"
            self.content += "</div>"
        self.content += self.footer


class Animal(object):
    def __init__(self):
        self._sound = "meow"
        self.image= "lion"
        self.name = "Lion"
        self.phylum = "Chordata"
        self.classification = "Mammalia"
        self.family = "Felidae"
        self.genus = "Panthera"
        self.average = "10-14"
        self.habitat = "Savannah"
        self.geo = "Africa"

    def sound(self):
        return self._sound


class Fox(Animal):
    def __init__(self):
        self.image= "fox"
        self.name = "Fox"
        self.phylum = "Chordata"
        self.classification = "Mammalia"
        self.family = "Canidae"
        self.genus = "Vulpes"
        self.average = "5"
        self.habitat = "Forests and deserts"
        self.geo = "Varies"
        self._sound = "Wa-pa-pa-pa-pa-pa-pow"

    def sound(self):
        return self._sound

class Cow(Animal):
    def __init__(self):
        self.image= "cow"
        self.name = "Cow"
        self.phylum = "Chordata"
        self.classification = "Mammalia"
        self.family = "Bovidae"
        self.genus = "Bos"
        self.average = "15"
        self.habitat = "Varies"
        self.geo = "Varies"
        self._sound = "Moo"

    def roar(self):
        return self._sound


class Horse(Animal):
    def __init__(self):
        self.image= "horse"
        self.name = "Horse"
        self.phylum = "Chordata"
        self.classification = "Mammalia"
        self.family = "Equidae"
        self.genus = "Equus"
        self.average = "25-30"
        self.habitat = "Varies"
        self.geo = "Varies"
        self._sound = "Neigh"

    def sound(self):
        return self._sound



app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
