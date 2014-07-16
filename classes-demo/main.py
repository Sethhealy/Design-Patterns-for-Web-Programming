
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        yoda = Character() #create instance
        yoda.name = "Jedi Master Yoda"
        yoda.occupation = "Jedi Knight"
        yoda.hometown = "Dagoba"
        yoda.quote = "Anger leads to hate <br />"

        self.response.write(yoda.say())


        leia = Character()
        leia.name = "Princess Leia Organa"
        leia.occupation = "General of the forces"
        leia.hometown = "Alderan"
        leia.quote = "Help me Obi Wan"
        self.response.write(leia.say())


class Character(object):

    def __init__(self):
        self.name =""
        self.occupation =""
        self.age =0
        self.hometown =""
        self.quote = ""

    def fight(self):
        print "AHA ! Fight"

    def say(self):
        print self.quote
        return self.quote


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
