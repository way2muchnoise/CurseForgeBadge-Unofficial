import json
import re
import urllib2
from lxml import html
from lxml.cssselect import CSSSelector


def resolve_project_url(project):
    project = project.split('?')[0].split('/')[0]
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    if project.isdigit():
        opened = opener.open('https://addons-ecs.forgesvc.net/api/v2/addon/' + project)
        return json.loads(opened.read())['websiteUrl']
    else:
        opened = opener.open('https://addons-ecs.forgesvc.net/api/v2/addon/search?gameId=432&searchFilter=' + project)
        results = json.loads(opened.read())
        for result in results:
            if result['slug'] == project:
                return result['websiteUrl']
        return results[0]['websiteUrl']


def get_project(project, re_add_part=''):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    opened = opener.open(resolve_project_url(project))
    if '?' in project or re_add_part != "":
        opened_url = opened.geturl()
        if '?' in project:
            params = project.split('?')[-1]
            if params not in opened_url:
                opened_url += '?' + params
        if re_add_part != "":
            url, url_params = opened_url.split('?')
            parts = url.split('/')[-re_add_part.count('/'):]
            if parts != re_add_part.split('/'):
                opened_url = url + re_add_part + '?' + url_params
        opened = opener.open(opened_url)
    return opened.read()


def get_files(project):
    return get_project(project + "/files")


def get_downloads(project):
    response = get_project(project)
    pattern = r'Total Downloads</span>\s*<span>(.*?)</span>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


def get_versions(project):
    tree = html.fromstring(get_files(project))
    sel = CSSSelector('h4.e-sidebar-subheader.overflow-tip.mb-1 a')
    results = [ele.text.replace('Minecraft ', '').replace('-Snapshot', '').strip() for ele in sel(tree) if 'Minecraft' in ele.text or 'Snapshot' in ele.text]
    results = sorted(set(results), reverse=True)  # filter out duplicates
    if len(results) > 0:
        return list(results)
    else:
        return ['Error']


# Currently only display latest version with Release version
def get_version(project):
    response = get_project(project)
    pattern = r'Game Version: (.*?)</span>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


def get_title(project):
    response = get_project(project)
    pattern = r'<h2 class="font-bold text-lg break-all">(.*?)</h2>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


dependents_dict = {
    'embedded': '1',
    'optional': '2',
    'required': '3',
    'tool': '4',
    'incompatible': '5',
    'included': '6'
}


def get_dependents(project, type):
    response = get_project(project + '/relations/dependents?filter-related-dependents=' + dependents_dict[type], '/relations/dependents')
    pagination_pattern = r'<a href="(.*?)" class="pagination-item"><span class="text-primary-500">(\d+)</span></a>'
    pages = re.findall(pagination_pattern, response)
    current_page = 1
    if len(pages) > 0:
        largest = sorted(pages, key=lambda page: int(page[1]))[-1]
        response = get_project(largest[0][len('/minecraft/mc-mods/'):], '/relations/dependents')
        current_page = int(largest[1])
    pattern = r'<li class="project-listing-row'
    items = re.findall(pattern, response)
    return "{:,}".format(len(items) + (current_page - 1) * 20)
