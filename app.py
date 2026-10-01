from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

violations = []


@app.route("/")
def index():
    return render_template("index.html", violations=violations)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "admin123":
            return redirect(url_for("index"))

    return render_template("login.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        violation = {
            "vehicle": request.form.get("vehicle"),
            "owner": request.form.get("owner"),
            "type": request.form.get("type"),
            "location": request.form.get("location"),
            "date": request.form.get("date"),
            "status": "Pending"
        }

        violations.append(violation)
        return redirect(url_for("history"))

    return render_template("add.html")


@app.route("/history")
def history():
    return render_template("history.html", violations=violations)


@app.route("/details/<int:index>")
def details(index):
    if 0 <= index < len(violations):
        violation = violations[index]
        return render_template("details.html", violation=violation)

    return "Violation not found", 404


@app.route("/status")
def status():
    return render_template("status.html", violations=violations)


if __name__ == "__main__":
    app.run(debug=True)