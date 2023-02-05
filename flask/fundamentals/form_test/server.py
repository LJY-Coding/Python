from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!

app = Flask(__name__)
app.secret_key = "IronMan"

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/users', methods=['POST'])
# def create_user():
#     print("Got Post Info")
#     print(request.form)
#     name = request.form['name']
#     email = request.form['email']
#     return redirect("/show")	 
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')


# @app.route('/show')
# def show_user():
#     return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

@app.route('/show')
def show_user():
    return render_template('show.html')





# # adding this method
# @app.route("/show")
# def show_user():
#     print("Showing the User Info From the Form")
#     print(request.form)
#     return redirect("/show")




if __name__ == "__main__":
    app.run(debug=True)