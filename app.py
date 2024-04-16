from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hellow World, from flask!"


@app.route("/Login",methods= ["POST","GET"] )
def login():
    return render_template()

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
if __name__ == "__main__":
    app.run(debug=True)