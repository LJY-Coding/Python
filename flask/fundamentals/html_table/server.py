from flask import Flask, render_template
import data
app = Flask(__name__)

@app.route('/')
def table():
    return render_template('index.html', data=data.users)


if __name__ == "__main__":
    app.run(debug=True)