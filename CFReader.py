import json
import re
import urllib.request


def get_project(project):
    project = project.split('?')[0].split('/')[0]
    opener = urllib.request.build_opener()
    # Minic Twitch client
    opener.addheaders = [
        ('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'twitch-desktop-electron-platform/1.0.0 Chrome/66.0.3359.181 Twitch/3.0.16 Safari/537.36 '
                       'desklight/8.42.2'),
        ('authority', 'addons-ecs.forgesvc.net'),
        ('origin', 'https://www.twitch.tv')
    ]
    if project.isdigit():
        opened = opener.open('https://addons-ecs.forgesvc.net/api/v2/addon/' + project)
        return json.loads(opened.read())
    else:
        search_string = project
        search_slug = project.lower()
        while True:
            opened = opener.open('https://addons-ecs.forgesvc.net/api/v2/addon/search?gameId=432&pagesize=50'
                                 '&searchFilter=' + search_string)
            results = json.loads(opened.read())
            for result in results:
                if result['slug'] == search_slug:
                    return result
            search_string = search_string[:int(len(search_string) / 2)]
            if len(search_string) < 2:
                return None


def get_downloads_author(author):
    opener = urllib.request.build_opener()
    # Minic Twitch client
    opener.addheaders = [
        ('user-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'twitch-desktop-electron-platform/1.0.0 Chrome/66.0.3359.181 Twitch/3.0.16 Safari/537.36 '
                       'desklight/8.42.2'),
        ('authority', 'addons-ecs.forgesvc.net'),
        ('origin', 'https://www.twitch.tv')
    ]
    search_string = author.lower()
    opened = opener.open('https://addons-ecs.forgesvc.net/api/v2/addon/search?gameId=432&pagesize=50'
                         '&searchFilter=' + search_string)
    results = json.loads(opened.read())
    author_download_count = 0
    for result in results:
        authors = map(lambda result_authors: result_authors['name'], result['authors'])
        if author in authors:
            author_download_count += result['downloadCount']
    return '{:,}'.format(int(author_download_count))


def get_downloads(project):
    response = get_project(project)
    return '{:,}'.format(int(response['downloadCount'])) if response else 'Error'


def get_versions(project):
    response = get_project(project)
    if response:
        results = [ # Only take major versions
            re.sub(r'(\d+)\.(\d+)(\.\d+)?', r'\1.\2', gameVersionLatestFile['gameVersion'])
            for gameVersionLatestFile in response['gameVersionLatestFiles']
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
    return 'Error'


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
