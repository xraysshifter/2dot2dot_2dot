import html.entities, re
from html.parser import HTMLParser

class Spider(HTMLParser):
    data = []
    words = []
    matches = []

    def handle_starttag(self, tag, attrs):
        if not tag == "br":
            pass
            #print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        if not tag == "br":
            pass
            #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        i = self.getpos()
        for word in self.words:
            match = re.search(word, data)
            if match != None:
                print(match.group(0))
                obj = [i, match.group(0)]
                self.matches.append(obj)

            

    def handle_entityref(self, name):
        entities = []

        if not name == "nbsp":
            codepoint = html.entities.name2codepoint[name]
            character = chr(codepoint)

            obj = [codepoint, character]
            entities.append(obj)
            #print(f"Found entity '{name}', replaced with: {character}")

        self.data.append(entities)




