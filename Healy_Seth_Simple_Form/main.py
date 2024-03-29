import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()

        if self.request.GET:
            p.content ="<div class=\"wrapper\">"
            p.content += 'Confirm this information to be true and if so keep as a record <br/>' \
                        '<br/>'
            p.content += "First name: " + self.request.GET['fname']
            p.content += "<br />Last name: " + self.request.GET['lname']
            p.content += "<br />Email: " + self.request.GET['ename']
            p.content += "<br />City: " + self.request.GET['city']
            p.content += "<br />State: " + self.request.GET['state']
            p.content += "<br />Country: " + self.request.GET['country']

            if self.request.GET.has_key('ps4'):
                p.content += "<br />System: " + self.request.GET['ps4']

            if self.request.GET.has_key('xbox'):
                p.content += "<br />System: " + self.request.GET['xbox']

            if self.request.GET.has_key('wiiu'):
                p.content += "<br />System: " + self.request.GET['wiiu']

            if self.request.GET.has_key('pc'):
                p.content += "<br />System: " + self.request.GET['pc']

            p.content += "<br /> Retailer: " + self.request.GET['retail']
            p.content += "<br /> Edition: " + self.request.GET['edition']
            p.content +="</div>"


            self.response.write(p.print_out_page())

        else:
            self.response.write(p.print_out_form())


class Page(object):
    header = """<!DOCTYPE>
    <html>
        <head>
            <link rel="stylesheet" href="styles/style.css" type="text/css"/>
            <title>Pre-order today!!! </title>
        </head>
        <body>


    """
    content = '''Please Work'''
    form_content = '''
        <form method="GET">
        <h1> Destiny Beta </h1>
        <div class="wrapper">
        <h2> Pre-order Today</h2>
            <input type="text" placeholder ="First Name" name= "fname" />
            <input type="text" placeholder ="Last Name"  name= "lname"/><br/>
            <input type="text" placeholder ="Email"  name= "ename"/><br/>
            <input type="text" placeholder ="City"  name= "city"/>
            <input type="text" placeholder ="State"  name= "state"/><br/>
            <input type="text" placeholder ="Country"  name= "country"/>
            <h5 class="systems">Systems</h5>
            <input type="checkbox" name="ps4" value="ps4">PS4
            <input type="checkbox" name="xbox" value="xbox">Xbox1<br/>
            <input type="checkbox" name="wiiu" value="wii u">Wii U
            <input type="checkbox" name="pc" value="pc">PC
            <h5 class="retailer">Retailers</h5>
            <div class="space"></div>
            <select name="retail">
                <option value="bestbuy">Best buy</option>
                <option value="gamestop">GameStop</option>
                <option value="psn">PlayStation store</option>
                <option value="target">Target</option>
            </select>
            <div class="space"></div>
            <select name="edition">
                <option value="Standard">Standard</option>
                <option value="Collectors Edition">Collectors edition</option>
                <option value="Limited Edition">Limited Edition</option>
            </select>
            <div class="space"></div>
            <input type="submit" value ="Order" />
        </form>
        </div>
    '''
    closer = '''
     </body>
     </html>'''

    def __init__(self):
        pass

    def print_out_page(self):
        return self.header + self.content + self.closer

    def print_out_form(self):
        return self.header + self.form_content + self.closer


app = webapp2.WSGIApplication([
                                  ('/', MainHandler)
                              ], debug=True)
