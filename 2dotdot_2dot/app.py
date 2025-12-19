import os, random, json
from flask import Flask
from flask import render_template

from parser import Spider

app = Flask(__name__)

abspath = os.path.abspath(os.getcwd())
input_path = abspath + "/../dot2dot_2dot/content"

def load_article(name):
    cpath = input_path + '/' + name + '.json'
    article = json.load(open(cpath, 'r'))
    
    return article

def select_random_article():
    names = []
    files = [e for e in os.listdir(input_path)]
    for file in files:
        rpath = input_path + "/" + file
        article = json.load(open(rpath, 'r'))
        names.append(article["title"])

    name = random.choice(names)

    return name

def eat(article):
    words = ['nectar', 'singes', 'omnivores', 'mystification', 'rationnelle']
    parser = Spider(convert_charrefs=False)
    parser.words = words
    parser.feed(article["content"])

    return [parser.data, parser.matches]


def eat_more():
    # choper des infos ailleurs.. etc
    pass

def inject():
    # injections de mots
    pass

def digest():
    # ici c'est du remixing de contenu ? 
    # transformer les mots en liens... ?
    pass
    

@app.route('/')
def index():
    name = select_random_article()
    article = load_article(name)

    data = eat(article)
    print(data[1])

    return render_template("index.html")

@app.route('/shoot')
def digging():
    
    return render_template("revolver.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="6003")
