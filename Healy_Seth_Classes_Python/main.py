import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Student(object):
    def __init__(self):
        self.name = ""
        self.year_completed = 0
        self.grad = ""
        self.odds= 0
        self.chances = 0


class Page(object):
    _head = """<!DOCTYPE HTML>
<head>
    <title>Inheritance</title>
</head>
<body>"""

    """<p> Everyone goes to school for a better life but not everyone goes to school and i know not all drop outs \
        go on to be in the military or become a custodian but the odds are better then their favor </p><br/>
        if you go to school for the full 4 years and serve 8 years in the military it will be {chances} until your done. <br/>
        giving you decide to quit school and become a custodian you will get out of school if you do the full schooling in {odds}
        """
    __content = ''

    close = """
</body>
</html>"""

class Custodian(Page):
    '''
    Here im calculating how long of school you need to graduate from school and start your field of choice if the choice
    is custodial work.
    '''
    def odds(self):
        return 4 + 0


    def __init__(self):
        pass

    def print_out(self):
        return self._head + self.__content + self.close



class Solider(Page):
    '''
    This is how long it will take until you have a civilian live and out of general school (public school)
    '''
    def chances(self):
        return 4 + 8



app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
