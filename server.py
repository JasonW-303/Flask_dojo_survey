from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "abcd-1234"


@app.get("/")
def ninja_survey():

    return render_template("index.html")


@app.post("/process")
def process():
    name = request.form["name"]
    print("USER NAME: ", name)
    session["name"] = name

    location = request.form["location"]
    print("LOCATION: ", location)
    session["location"] = location

    language = request.form["language"]
    print("LANGUAGE: ", language)
    session["language"] = language

    comment = request.form["comment"]
    print("COMMENT: ", comment)
    session["comment"] = comment

    return redirect("/result")


@app.get("/result")
def result():
    name = session.get("name")
    location = session.get("location")
    language = session.get("language")
    comment = session.get("comment")

    return render_template(
        "result.html", name=name, location=location, language=language, comment=comment
    )


@app.get("/destroy_session")
def destroy_session():
    session.clear()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
