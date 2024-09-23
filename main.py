from flask import Flask, render_template


app = Flask(__name__)
days_since_last_baddadan = 0  # Todo: make this persistent


@app.route("/")
def index():
    return render_template("index.html", days=days_since_last_baddadan)


if __name__ == "__main__":
    app.run()