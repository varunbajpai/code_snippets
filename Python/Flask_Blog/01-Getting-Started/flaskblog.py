from flask import Flask
app = Flask(__name__)                           #This will create an object of app which we will run later


@app.route("/")                                 #Setting up routes is so easy in django
@app.route("/home")                             #the '/' and '/home' wil be returning the same html page as shown
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")                            #this is setting up the '/about' route as shown
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5000,debug=True).  #This will bind the host to the current ip on the port 5000
