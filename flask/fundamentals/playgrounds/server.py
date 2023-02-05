from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def say_hello():
    return "You can change the url to 'http://localhost:5000/(x)/(color)' to display beautiful blocks "

@app.route('/play')
def play():
    return render_template('index.html', numbers = 3, page= "1", color = 'rgb(76, 169, 245)')

@app.route('/play/<int:x>')
def play_blocks(x):
    return render_template('index.html', numbers = x, page= "2" , color = 'rgb(76, 169, 245)')

@app.route('/play/<int:x>/<string:color>')
def color_blocks(x, color):
    return render_template('index.html', numbers = x, page= "3", color = color)

if __name__ == "__main__":
    app.run(debug = True)