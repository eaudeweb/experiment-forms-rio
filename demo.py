#!/usr/bin/env python

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    return "hi"


if __name__ == '__main__':
    app.run(debug=True)
