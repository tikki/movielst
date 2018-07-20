from flask import Flask, render_template
import json
from movielst import config

app = Flask(__name__)


@app.route('/')
def index():
    with open(config.get_setting('Index', 'location'), 'r') as file:
        data = json.loads(file.read())

    return render_template('home.html', movie_list=data)


@app.route('/movie/<variable>')
def movie(variable):
    with open(config.get_setting('Index', 'location'), 'r') as file:
        data = json.loads(file.read())
    i = 0
    list = {}
    for datas in data:
        if datas["title"] == variable:
            list["title"] = datas["title"]
            list["genre"] = datas["genre"]
            list["imdb"] = datas["imdb"]
            list["runtime"] = datas["runtime"]
            list["tomato"] = datas["tomato"]
            list["year"] = datas["year"]
            list["awards"] = datas["awards"]
            list["cast"] = datas["cast"]
            list["director"] = datas["director"]
        i+=1
    print(list)
    return render_template('movie.html', list=list)


if __name__ == '__main__':
    app.run(debug=True)
