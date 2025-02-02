from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form["sport"]
    if input_name == "Tennis":
        return render_template("tennis.html", name=input_name)
    if input_name == "Padel":
        return render_template("padel.html", name=input_name)
    if input_name == "Squash":
        return render_template("squash.html", name=input_name)
    if input_name == "Table Tennis":
        return render_template("tableTennis.html", name=input_name)
    if input_name == "Badminton":
        return render_template("badminton.html", name=input_name)


def process_query(query):
    query = request.args.get("q", "").strip().lower()

    responses = {"dinosaurs": "Dinosaurs ruled the"
                              " Earth 200 million years ago"}
    return responses.get(query.strip().lower(), "Unknown")


@app.route("/query", methods=["GET"])
def query_route():
    """Flask route to handle HTTP requests."""
    query = request.args.get("q", "")
    return jsonify({"response": process_query(query)})
