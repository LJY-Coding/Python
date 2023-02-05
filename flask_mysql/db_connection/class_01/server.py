from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key="superironman"

users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dash():
    if "user" not in session:
        return redirect('/')
    return render_template('dash.html', users=users)

@app.route('/submit', methods=["POST"])
def submit():
    form = request.form
    if request.form["action"] == "register":
        data={
            "id": (len(users) + 1),
            "f_name": request.form["f_name"],
            "l_name": request.form["l_name"],
            "email": request.form["email"],
            "password": request.form['password']
        }

        users.append(data)
        session["user"]=data
        return redirect('/dashboard')
        
    else:
        for user in users:
            if request.form["email"] == user["email"] and request.form["password"] == user["password"]:
                session["user"]=user
                return redirect("/dashboard")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)