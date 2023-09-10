import urllib.request, json
from flask import Flask, render_template, request  
app = Flask(__name__)            

def get_xkcd_data():
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    comic_data = json.loads(data)
    return comic_data

@app.route("/")                   
def hello():   
    comic_data = get_xkcd_data()                   
    return render_template("index.html", comic_data = comic_data)  

@app.route("/about")                  
def about(): 
    name = request.args.get('name') if request.args.get('name') else "Shreya" 
    return render_template("about.html", aboutName = name)

if __name__ == "__main__":        
    app.run()  