from flask import Flask
from flask import render_template

import CFReader
from badgeCreator import create_badge

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/<project>.svg')
@app.route('/<project>(<l_colour>).svg')
@app.route('/<style>_<project>.svg')
@app.route('/<style>_<project>(<l_colour>).svg')
@app.route('/<style>_<project>_<extra>.svg')
@app.route('/<style>_<project>_<extra>(<l_colour>).svg')
@app.route('/<style>_<project>_<extra>(<l_colour>-<r_colour>-<text_colour>-<shadow_colour>-<logo_colour>).svg')
def downloads(project, style='full', extra=None, l_colour='E04E14', r_colour='2D2D2D', text_colour='fff',
              shadow_colour='010101', logo_colour='1C1C1C'):
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
        replacement += ' ' + extra
    width = max(len(replacement) * 7 + 12, 40)
    return create_badge(template, dls=replacement, width=width, totalWidth=(30 + width),
                        offset=(30.5 + width / 2), l_colour=l_colour, r_colour=r_colour, text_colour=text_colour,
                        shadow_colour=shadow_colour, logo_colour=logo_colour), 200, {'Content-Type': 'image/svg+xml'}


@app.route('/versions/<project>.svg')
@app.route('/versions/<project>(<r_colour>).svg')
@app.route('/versions/<project>_<style>.svg')
@app.route('/versions/<project>_<style>(<r_colour>).svg')
@app.route('/versions/<text>_<project>_<style>.svg')
@app.route('/versions/<text>_<project>_<style>(<r_colour>).svg')
@app.route('/versions/<text>_<project>_<style>(<l_colour>-<r_colour>-<text_colour>-<shadow_colour>).svg')
def supported_versions(project, style='all', text='Available for', l_colour='2D2D2D', r_colour='E04E14',
                       text_colour='fff', shadow_colour='010101'):
    template = app.open_resource('templates/shield.svg', 'r').read()
    versions = CFReader.get_versions(project)
    versions_text = versions[0] if style == 'latest' else ' | '.join(str(version) for version in versions)
    version_width = max(len(versions_text) * 6, 40)
    text_width = len(text) * 7 + 4
    return create_badge(template, versions=versions_text, text=text, widthText=text_width, widthVersions=version_width,
                        totalWidth=(version_width + text_width), offsetText=(text_width / 2),
                        offsetVersions=(text_width + version_width / 2), l_colour=l_colour, r_colour=r_colour,
                        text_colour=text_colour, shadow_colour=shadow_colour), 200, {'Content-Type': 'image/svg+xml'}


@app.route('/packs/<project>.svg')
@app.route('/packs/<project>(<l_colour>).svg')
@app.route('/packs/<style>_<project>.svg')
@app.route('/packs/<style>_<project>(<l_colour>).svg')
@app.route('/packs/<style>_<project>_<before>_<after>.svg')
@app.route('/packs/<style>_<project>_<before>_<after>(<l_colour>).svg')
@app.route('/packs/<style>_<project>_<before>_<after>(<l_colour>-<r_colour>-<text_colour>-<shadow_colour>-<logo_colour>).svg')
def packs(project, style='full', before='included in', after='packs', l_colour='E04E14', r_colour='2D2D2D', text_colour='fff',
              shadow_colour='010101', logo_colour='1C1C1C'):
    template = app.open_resource('templates/curseShield.svg', 'r').read()
    replacement = before + ' '
    packs = CFReader.get_dependents(project, 'included')
    if style == 'short':
        splitted = packs.split(',')
        first_number = splitted[0][0]
        padding_zeros = '0' * (len(splitted[0]) - 1)
        post_fix = ('M+' if len(splitted) > 2 else ('k+' if len(splitted) > 1 else ''))
        replacement += first_number + padding_zeros + post_fix
    else:
        replacement += packs
    if after:
        replacement += ' ' + after
    width = max(len(replacement) * 7 + 12, 40)
    return create_badge(template, dls=replacement, width=width, totalWidth=(30 + width),
                        offset=(30.5 + width / 2), l_colour=l_colour, r_colour=r_colour, text_colour=text_colour,
                        shadow_colour=shadow_colour, logo_colour=logo_colour), 200, {'Content-Type': 'image/svg+xml'}


@app.route('/mods/<project>.svg')
@app.route('/mods/<project>(<l_colour>).svg')
@app.route('/mods/<style>_<project>.svg')
@app.route('/mods/<style>_<project>(<l_colour>).svg')
@app.route('/mods/<style>_<project>_<before>_<after>.svg')
@app.route('/mods/<style>_<project>_<before>_<after>(<l_colour>).svg')
@app.route('/mods/<style>_<project>_<before>_<after>(<l_colour>-<r_colour>-<text_colour>-<shadow_colour>-<logo_colour>).svg')
def mods(project, style='full', before='required for', after='mods', l_colour='E04E14', r_colour='2D2D2D', text_colour='fff',
              shadow_colour='010101', logo_colour='1C1C1C'):
    template = app.open_resource('templates/curseShield.svg', 'r').read()
    replacement = before + ' '
    packs = CFReader.get_dependents(project, 'required')
    if style == 'short':
        splitted = packs.split(',')
        first_number = splitted[0][0]
        padding_zeros = '0' * (len(splitted[0]) - 1)
        post_fix = ('M+' if len(splitted) > 2 else ('k+' if len(splitted) > 1 else ''))
        replacement += first_number + padding_zeros + post_fix
    else:
        replacement += packs
    if after:
        if packs == '1' and after == 'mods':
            after = 'mod'
        replacement += ' ' + after
    width = max(len(replacement) * 7 + 12, 40)
    return create_badge(template, dls=replacement, width=width, totalWidth=(30 + width),
                        offset=(30.5 + width / 2), l_colour=l_colour, r_colour=r_colour, text_colour=text_colour,
                        shadow_colour=shadow_colour, logo_colour=logo_colour), 200, {'Content-Type': 'image/svg+xml'}


@app.after_request
def add_header(response):
    # Image may be cached up to 3 hour
    response.cache_control.max_age = 60 * 60 * 3
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
