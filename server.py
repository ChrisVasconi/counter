
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def counter():
    if "number_of_visits" in session:
        # """checking the number of visits"""
        session["number_of_visits"] += 1
    else:
        session["number_of_visits"] = 1
    return render_template("index.html")


@app.route("/<int:num>")
def func(num):
    if "number_of_visits" in session:
        session["number_of_visits"] += num - 1
    return redirect("/")


@app.route("/destroy_session")
def destroy_session():
    del session["number_of_visits"]
    return redirect("/")  # Redirect to main page


if __name__ == "__main__":
    app.run(debug=True)
