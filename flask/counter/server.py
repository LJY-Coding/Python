from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "ironMan"

@app.route('/')
def counter():
    return render_template('index.html', counts=1, plural="")


@app.route('/click', methods=['POST'])
def counts():
    pass

if __name__ == "__main__":
    app.run(debug=True)