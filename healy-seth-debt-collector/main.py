import webapp2
from index import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = PersonPage()

        person1 = Person()
        person1.cost = 80000
        person1.name = "Alan"
        person1.degree = "web Design"
        person1.grad = 2014
        person1.year = 1985

        person2 = Person()
        person2.cost = 90000
        person2.name = "Seth"
        person2.degree = "web Design"
        person2.grad = 2014
        person2.year = 1988

        person3 = Person()
        person3.cost = 80000
        person3.name = "Carmine"
        person3.degree = "web Design"
        person3.grad = 2014
        person3.year = 1987

        person4 = Person()
        person4.cost = 100000
        person4.name = "Emmanuel"
        person4.degree = "web thinker"
        person4.grad = 2014
        person4.year = 1990

        person5 = Person()
        person5.cost = 200000
        person5.name = "Julio"
        person5.degree = "unemployed"
        person5.grad = 2014
        person5.year = 1986

        people = {
            "person1": person1,
            "person2": person2,
            "person3": person3,
            "person4": person4,
            "person5": person5
        }

        p.people(people)

        if self.request.GET:
            if self.request.GET.has_key("person"):

                getperson = self.request.GET["person"]

                p.person = people[getperson]
                p.render()

                self.response.write(p.content)

        else:
            p.render()
            self.response.write(p.content)


class PersonPage(object):

    __people = {}
    person = None

    title = ""

    header = """ <!DOCTYPE HTML>
<head>
    <title>{self.title}</title>
    <link rel="stylesheet" href="styles/styles.css" type="text/css"" />
</head>
<body>
"""

    footer = """</body>
</html>"""

    __content = """

        <h1> Debt calculator </h1>
        <p> Everyone goes to school for a better life but we all know when you go as a full time student to where\
        you cannot work you will acquire a lot of debt here I will show you how much debt a few students are and \
        what degrees they were in when they graduated </p>

        <h3> (ex)-Students </h3>

        <a href="/"> None </a>

    """

    def people(self, people):
        self.__people = people

    def render(self):
        # generate content
        self.__content += self.header.format(**locals())

        for person in self.__people:
            self.__content +=  '<a href="/?person=' + person + '"> <div class="names"><br/></div>' + self.__people[person].name + ' </a>'

        if bool(self.person):
            self.__content += "<p>" + self.person.name + "</p>"
            self.__content += "<p>" + str(self.person.year) + "</p>"
            self.__content += "<p>" + self.person.degree + "</p>"
            self.__content += "<p>" + str(self.person.age) + "</p>"
            self.__content += "<p>" + str(self.person.cost) + "</p>"
            self.__content += "<p>" + str(self.person.interest_five) + "</p>"
            self.__content += "<p>" + str(self.person.interest_ten) + "</p>"
            self.__content += "<p>" + str(self.person.interest_fifteen) + "</p>"

        self.__content += self.footer

    @property
    def content(self):
        return self.__content

    @property
    def css(self):
        return self.css


class Person(object):
    def __init__(self):
        self.name = ""
        self.year = 0
        self.degree = ""
        self.grad = 0
        self.cost = 0

    @property
    def interest_five(self):
        return .0466 * 5 * self.cost

    @property
    def interest_ten(self):
        return .0466 * 10 * self.cost

    @property
    def interest_fifteen(self):
        return .0466 * 15 * self.cost

    @property
    def age(self):
        return 2014 - self.year


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
