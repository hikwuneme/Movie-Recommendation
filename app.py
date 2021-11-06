from flask import Flask, render_template, request, url_for
import model

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def main():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        name = request.form["movie"]
        name = name.title()
        if name not in model.titles:
            return render_template("error.html")
        else:
            result = model.get_recommendations(name)
            names = []
            for i in range(len(result)):
                names.append(result.iloc[i])
            for i in names:
                new_name = i
            return render_template("sub.html", n = names, movie_name = name)

if __name__ == "__main__":
    app.run()