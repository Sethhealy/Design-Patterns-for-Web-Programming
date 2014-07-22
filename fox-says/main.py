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

        a.content = animal.roar()

        self.response.write(a.content)


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

    content = """

        <h1> What does the fox say </h1>
        <p> Though there is great diversity in the animal kingdom, animals
        can be distinguished from the other kingdoms by a set of characteristics.
        Though other types of life may share some of these characteristics, the set
        of characteristics as a whole provide a distinction from the other kingdoms.
        The set of characteristics provided by Audesirk and Audesirk are: </p>

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




    """

    def __init__(self):
        pass

    # def print_out(self):
    #     return self._header + self._content + self._close
    #
    #
    # def render(self):
    #     # generate content
    #     self._content += self._header.format(**locals())
    #
    #     if bool(self.animal):
    #         self._content += "<div class='names'>"
    #         self._content += "<p>" + "Animal name: " + self.animal.name + "</p>"
    #         self._content += "<p>" + "Phylum: " + self.animal.phylum + "</p>"
    #         self._content += "<p>" + "Classification: " + self.animal.classification + "</p>"
    #         self._content += "<p>" + "Family: " + self.animal.family + "</p>"
    #         self._content += "<p>" + "Genus: " + self.animal.genus + "</p>"
    #         self._content += "<p>" + "Average: " + str(self.animal.average) + "</p>"
    #         self._content += "<p>" + "Habitat: " + self.animal.habitat + "</p>"
    #         self._content += "<p>" + "Geo: " + self.animal.geo + "</p>"
    #         self._content += "<p>" + "Sound: " + self.animal._sound + "</p>"
    #         self._content += "</div>"
    #     self._content += self.footer


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
        self._sound = "Wa-pa-pa-pa-pa-pa-pow"


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
        self._sound = "Moo"


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
        self._sound = "Neigh"


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
