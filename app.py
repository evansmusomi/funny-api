""" Defines Minimalist Flask API that displays funny quotes"""

import random
from quotes import funny_quotes
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/api/funny")
def serve_funny_quote():
    """ Returns one randomly selected funny quote """

    quotes = funny_quotes()
    number_of_quotes = len(quotes)
    selected_quote = quotes[random.randint(0, number_of_quotes - 1)]
    return jsonify(selected_quote)


if __name__ == "__main__":
    app.run(debug=True)
