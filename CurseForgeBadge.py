from flask import Flask
from CFReader import get_downloads

app = Flask(__name__)


@app.route('/<int:project_id>.svg')
@app.route('/<style>-<int:project_id>.svg')
@app.route('/<style>-<int:project_id>-<extra>.svg')
def hello_world(project_id, style='full', extra=None):
    template = app.open_resource('templates/shield.svg', 'r').read()
    dls = get_downloads(project_id)
    if style == 'short':
        splitted = dls.split(',')
        dls = splitted[0] + ('M+' if len(splitted) > 2 else ('k+' if len(splitted) > 1 else ''))
    if extra:
        dls += " " + extra
    width = max(len(dls) * 7 + 12, 40)
    return template\
        .replace('{{dls}}', dls)\
        .replace('{{width}}', repr(width))\
        .replace('{{totalWidth}}', repr(30 + width))\
        .replace('{{offset}}', repr(30.5 + width / 2))

if __name__ == '__main__':
    app.run()
