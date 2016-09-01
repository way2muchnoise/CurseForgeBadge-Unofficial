from flask import Flask
from flask import render_template

import CFReader
from badgeCreator import create_badge

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/<project>.svg')
@app.route('/<style>_<project>.svg')
@app.route('/<style>_<project>_<extra>.svg')
def downloads(project, style='full', extra=None):
    template = app.open_resource('templates/curseShield.svg', 'r').read()
    replacement = ''
    dls = CFReader.get_downloads(project)
    if style == 'short':
        splitted = dls.split(',')
        first_number = splitted[0][0]
        padding_zeros = '0' * (len(splitted[0]) - 1)
        post_fix = ('M+' if len(splitted) > 2 else ('k+' if len(splitted) > 1 else ''))
        replacement += first_number + padding_zeros + post_fix
    else:
        replacement += dls
    if extra:
        replacement += " " + extra
    width = max(len(replacement) * 7 + 12, 40)
    return create_badge(template, dls=replacement, width=width, totalWidth=(30 + width),
                        offset=(30.5 + width / 2)), 200, {'Content-Type': 'image/svg+xml'}


@app.route('/versions/<project>.svg')
@app.route('/versions/<project>_<style>.svg')
@app.route('/versions/<text>_<project>_<style>.svg')
def supported_versions(project, style='all', text='Available for'):
    template = app.open_resource('templates/shield.svg', 'r').read()
    versions = CFReader.get_versions(project)
    versions_text = versions[0] if style == 'latest' else ' | '.join(str(version) for version in versions)
    version_width = max(len(versions_text) * 6, 40)
    text_width = len(text) * 7 + 4
    return create_badge(template, versions=versions_text, text=text, widthText=text_width, widthVersions=version_width,
                        totalWidth=(version_width + text_width), offsetText=(text_width / 2),
                        offsetVersions=(text_width + version_width / 2)), 200, {'Content-Type': 'image/svg+xml'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
