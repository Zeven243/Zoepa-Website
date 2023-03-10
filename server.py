from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home_page():
    copyright_date = datetime.datetime.now().year
    return render_template("index.html", year=copyright_date)


if __name__ == "__main__":
    app.run(debug=True)