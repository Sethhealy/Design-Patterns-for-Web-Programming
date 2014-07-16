
class Page(object):
    title =""
    __css ="css/styles.css"
    header = """ <!DOCTYPE HTML>
<head><title></title>
<link rel="stylesheet" type="text/css" href="{self.css}" />
</head>
<body>
"""
    __content = "welcome peasants"
    closer = """
    </body>
</html>"""


    def __init__(self):
        pass

    def print_out(self):
        return self.header + self.__content + self.closer

    @property #making getter - for reading information
    def content(self):
        return self.__content

    @content.setter #gives write access
    def content(self, c):
        self.__content = c

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, c):
        self.__css = c
        self.header = self.header.format(**locals())