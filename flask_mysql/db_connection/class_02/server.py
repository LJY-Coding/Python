from flask import Flask,render_template,redirect,request,session
from user import Users
app = Flask(__name__)

app.secret_key="superdeliciouspizzapie"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dash():
    
    return render_template("dash.html",users=Users.getAll())

@app.route("/submit",methods=["POST"])
def submit():
    print(request.form)
    if request.form["action"] == "register":
        data={
            "f_name":request.form["f_name"],
            "l_name":request.form["l_name"],
            "email":request.form["email"],
            "password":request.form["password"]
        }

    
        Users.save(data)
        # session["user_id"]=
        
        return redirect("/dashboard")

    else:

        for user in Users:
            if request.form["email"] == user["email"] and request.form["password"] == user["password"]:
                session["user"]=user
                return redirect("/dashboard")

        return redirect("/")

@app.route('/users/<int:id>/edit')
def updateView(id):
    return render_template('update.html', user=Users.getOne({'id':id}))


@app.route("/users/<int:id>/update", methods=["POST"])
def update(id):
    data={
            "id": id,
            "f_name":request.form["f_name"],
            "l_name":request.form["l_name"],
            "email":request.form["email"],
            "password":request.form["password"]
        }
    Users.update(data)
    return redirect("/dashboard")

@app.route("/users/<int:id>/delete")
def destroy(id):
    data={
            "id": id
        }
    Users.destroy(data)
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)
