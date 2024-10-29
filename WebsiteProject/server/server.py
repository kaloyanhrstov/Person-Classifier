from flask import Flask, render_template, request, jsonify
import util
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/classifier", methods=['GET', 'POST'])
# def classifier():
#     return render_template("cls.html")


@app.route('/classifier', methods=['GET', 'POST'])
def classifier():
    if request.method == "POST":

        image_data = request.form['image_data']

        response = jsonify(util.classify_image(image_data))

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response

    return render_template("cls.html")


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5000)
