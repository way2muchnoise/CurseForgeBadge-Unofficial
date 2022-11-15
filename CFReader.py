import json
import re
import urllib.request
from os import getenv

API_KEY = getenv('API_KEY')
API_URL = 'https://api.curseforge.com'
MINECRAFT_GAME_ID = '432'


def new_api_call():
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('user-agent', 'way2muchnoise'),
        ('x-api-key', API_KEY),
        ('Accept', 'application/json')
    ]
    return opener


def get_project(project):
    project = project.split('?')[0].split('/')[0]
    api_call = new_api_call()
    if project.isdigit():
        api_response = api_call.open(API_URL + '/v1/mods/' + project)
        return json.loads(api_response.read())['data']
    else:
        search_string = project
        search_slug = project.lower()
        while True:
            api_response = api_call.open(API_URL + '/v1/mods/search?gameId=432&pagesize=50&slug=' + search_string)
            results = json.loads(api_response.read())['data']
            for result in results:
                if result['slug'] == search_slug:
                    return result
            search_string = search_string[:int(len(search_string) / 2)]
            if len(search_string) < 2:
                return None


def get_downloads_author(author):
    api_call = new_api_call()
    search_string = author.lower()
    api_response = api_call.open(API_URL + '/v1/mods/search?gameId=432&pagesize=50&slug=' + search_string)
    results = json.loads(api_response.read())['data']
    author_download_count = 0
    for result in results:
        authors = map(lambda result_authors: result_authors['name'], result['authors'])
        if author in authors:
            author_download_count += result['downloadCount']
    return '{:,}'.format(int(author_download_count))


def get_downloads(project):
    api_response = get_project(project)
    return '{:,}'.format(int(api_response['downloadCount'])) if api_response else 'Error'


def get_versions(project):
    api_response = get_project(project)
    if api_response:
        results = [  # Only take major versions
            re.sub(r'(\d+)\.(\d+)(\.\d+)?', r'\1.\2', gameVersionLatestFile['gameVersion'])
            for gameVersionLatestFile in api_response['latestFilesIndexes']
        ]
        return list(sorted(set(results), reverse=True, key=lambda s: list(map(int, s.split('.')))))
    else:
        return ['Error']


def get_title(project):
    response = get_project(project)
    return response['name'] if response else 'Error'


dependents_dict = {
    'embedded': '1',
    'optional': '2',
    'required': '3',
    'tool': '4',
    'incompatible': '5',
    'included': '6'
}


def get_dependents_old(project, type):
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
