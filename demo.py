#!/usr/bin/env python
# encoding: utf-8

import flask
from flatland.out.markup import Generator
from schema import Species


app = flask.Flask(__name__)

_my_extensions = app.jinja_options['extensions'] + ['jinja2.ext.do']
app.jinja_options = dict(app.jinja_options, extensions=_my_extensions)
app.jinja_env.globals['form_generator'] = Generator('html')


@app.route('/')
def index():
    rows = [
        Species({'name': u'cioară', 'site': {'isolation': 'B'}}, name='1'),
        Species({'name': u'rață', 'site': {'isolation': 'C'}}, name='2'),
        Species(),
    ]
    return flask.render_template('index.html', schema=Species(), rows=rows)


@app.route('/save', methods=['POST'])
def save():
    import flatland
    from pprint import pformat
    from werkzeug.utils import escape
    SpeciesList = flatland.List.of(Species)
    sl = SpeciesList.from_flat(flask.request.form.to_dict())
    return "<pre>" + escape(pformat(sl.value)) + "</pre>"


if __name__ == '__main__':
    app.run(debug=True)
