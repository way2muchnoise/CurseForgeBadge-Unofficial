import re
import urllib2
import lxml.html
from lxml.cssselect import CSSSelector

def get_project(project):
    return urllib2.urlopen("https://minecraft.curseforge.com/projects/" + project).read()

def get_files(project):
    return get_project(project + "/files")

def get_downloads(project):
    response = get_project(project)
    pattern = 'Total Downloads\s*</div>\s*<div class="info-data">(.*?)</div>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


def get_versions(project):
    tree = lxml.html.fromstring(get_files(project))
    sel = CSSSelector('option.game-version-type')
    results = [ele.text.replace('Minecraft ', '') for ele in sel(tree) if 'Minecraft' in ele.text]
    if len(results) > 0:
       return results
    else:
        return ['Error']


def get_tile(project):
    response = get_project(project)
    pattern = '<h1 class="project-title">\s+<a.*?>\s+<span class="overflow-tip">(.*?)\s*</span></a>\s+</h1>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'
