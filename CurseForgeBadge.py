from flask import Flask
from flask import render_template
from CFReader import get_downloads

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/<project>.svg')
@app.route('/<style>_<project>.svg')
@app.route('/<style>_<project>_<extra>.svg')
def hello_world(project, style='full', extra=None):
    template = app.open_resource('templates/shield.svg', 'r').read()
    replacement = ''
    dls = get_downloads(project)
    if style == 'short':
        splitted = dls.split(',')
        first_numbner = splitted[0][0]
        padding_zeros = '0' * (len(splitted[0])-1)
        post_fix = ('M+' if len(splitted) > 2 else ('k+' if len(splitted) > 1 else ''))
        replacement += first_numbner + padding_zeros + post_fix
    else:
        replacement += dls
    if extra:
        replacement += " " + extra
    width = max(len(replacement) * 7 + 12, 40)
    return template\
        .replace('{{dls}}', replacement)\
        .replace('{{width}}', repr(width))\
        .replace('{{totalWidth}}', repr(30 + width))\
        .replace('{{offset}}', repr(30.5 + width / 2)), 200, {'Content-Type': 'image/svg+xml'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
