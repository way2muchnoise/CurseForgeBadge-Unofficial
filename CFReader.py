import re
import urllib2
from lxml import html
from lxml.cssselect import CSSSelector


def get_project(project):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    opened = opener.open("https://minecraft.curseforge.com/projects/" + project)
    if '?' in project:
        opened_url = opened.geturl()
        params = project.split('?')[-1]
        if params not in opened_url:
            opened = opener.open(opened_url + '?' + params)
    return opened.read()


def get_files(project):
    return get_project(project + "/files")


def get_downloads(project):
    response = get_project(project)
    pattern = r'Total Downloads\s*</div>\s*<div class="info-data">(.*?)</div>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


def get_versions(project):
    tree = html.fromstring(get_files(project))
    sel = CSSSelector('option.game-version-type')
    results = [ele.text.replace('Minecraft ', '') for ele in sel(tree) if 'Minecraft' in ele.text]
    if len(results) > 0:
       return results
    else:
        return ['Error']


def get_tile(project):
    response = get_project(project)
    pattern = r'<h1 class="project-title">\s+<a.*?>\s+<span class="overflow-tip">(.*?)\s*</span></a>\s+</h1>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


def get_modpacks(project):
    response = get_project(project + '/relations/dependents?filter-related-dependents=6')
    pagination_pattern = r'<a href="(.*?)" class="b-pagination-item">(\d+)</a>'
    pages = re.findall(pagination_pattern, response)
    current_page = 1
    if len(pages) > 0:
        largest = sorted(pages, key=lambda page: int(page[1]))[-1]
        response = get_project(largest[0][len('/projects/'):])
        current_page = int(largest[1])
    pattern = r'<li class="project-list-item">'
    items = re.findall(pattern, response)
    return "{:,}".format(len(items) + (current_page - 1) * 20)
