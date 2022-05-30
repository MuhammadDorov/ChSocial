from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def pageNoteFound(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug = True)