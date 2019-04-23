import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    davids_birthday = now.month == 6 and now.day == 16
    return render_template('index.html', davids_birthday=davids_birthday)


if __name__ == "__main__":
    app.run()