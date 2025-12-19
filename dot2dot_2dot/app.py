import os, json, random
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

cfpath = "./content"
abspath = os.path.abspath(os.getcwd())

def append_user(useragent):
    return

def load_articles(files):
    articles = []
    
    for file in files:
        cpath = cfpath + '/' + file
        article = json.load(open(cpath, "r"))
        articles.append(article)

    return articles

def load_article(name):
    cpath = cfpath + '/' + name + '.json'
    article = json.load(open(cpath, 'r'))
    
    return article



@app.route('/')
def index():
    string = "Feb 6, 2030 23:26:00"
    files = [e for e in os.listdir(cfpath)]
    useragent = request.headers.get('User-Agent')

    entries = load_articles(files)
    return render_template("index.html", entries=entries, string=string,
                           useragent=useragent)


@app.route('/seek/<path:path>')
def seeker(path):
    print(path)
    with open(f"content/{path}.json", "r") as j:
        page = json.load(j) 

    return render_template('seeker.html', page=page)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="6001")
