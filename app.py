from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title = 'Главная страница')

@app.errorhandler(404)
def pageNoteFound(error):
    return render_template('404.html', title = '404 ошибка')

if __name__ == '__main__':
    app.run(debug = True)
