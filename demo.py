#!/usr/bin/env python

import flask
from flatland.out.markup import Generator
from schema import Species


app = flask.Flask(__name__)

_my_extensions = app.jinja_options['extensions'] + ['jinja2.ext.do']
app.jinja_options = dict(app.jinja_options, extensions=_my_extensions)
app.jinja_env.globals['form_generator'] = Generator('html')


@app.route('/')
def index():
    return flask.render_template('index.html', form=Species())


if __name__ == '__main__':
    app.run(debug=True)
