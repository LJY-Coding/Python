from flask import Flask
app = Flask(__name__)

# 1. localhost:5000/ - have it say "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World!"

# 2. localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# 3. Create one url pattern and function that can handle the following examples:
@app.route('/say/<string:name>')
def say_name(name):
    return f"Hi {name.capitalize()}"

# 4. Create one url pattern and function that can handle the following examples
@app.route('/repeat/<int:num>/<string:str>')
def repeat(num, str):
    return f"{str * num}"

@app.route('/<route_name>')
def exception(route_name):
    route_list = ['', 'dojo', 'say', 'repeat']
    if route_name not in route_list:
        return "Sorry! No response. Try again."


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.