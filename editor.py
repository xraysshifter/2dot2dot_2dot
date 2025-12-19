
import os, json
from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_ckeditor import CKEditor

app = Flask(__name__)
editor = CKEditor(app)
app.config['CKEDITOR_PKG_TYPE']='full'
app.config['APPLICATION_ROOT']='/home/nansp/projets/w3b/2dot2dot_2dot/'

abspath = "."
rabspath = os.path.abspath(abspath)

def saveToFile(data):
    with open(data["path"], "w") as f:
        json.dump(data, f, indent=4)

def strform(fname):
    new = fname.replace(' ', '_')

    return new


def get_request_data(request, strftime):
    title = request.form.get('title')
    author = request.form.get('author')
    content = request.form.get('ckeditor')
    path = f"{abspath}/dot2dot_2dot/content/{title}.json"

    data = {

            "title"  : title,
            "author" : author,
            "content": content,
            "date"   : strftime,
            "path"   : path

            }

    return data


@app.route('/', methods=['POST', 'GET'])
def editor():
    
    if request.method == 'POST':
        now = datetime.now()
        strftime = now.strftime("%Y-%m-%d_%H:%M:%S")

        data = get_request_data(request, strftime) 
        
        saveToFile(data)
        

    return render_template("editor.html")


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port="6002")
