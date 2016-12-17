import re
import urllib2


def get_project(project):
    return urllib2.urlopen("https://minecraft.curseforge.com/projects/" + project).read()


def get_downloads(project):
    response = get_project(project)
    pattern = 'Total Downloads\s*</div>\s*<div class="info-data">(.*?)</div>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'


def get_versions(project):
    response = get_project(project)
    pattern = '<h4 class="e-sidebar-subheader overflow-tip">\s+<a.*?>\s+Minecraft (.*?)\s+</a>\s+</h4>'
    versions = re.findall(pattern, response)
    if len(versions) > 0:
        return versions
    else:
        return 'Error'


def get_tile(project):
    response = get_project(project)
    pattern = '<h1 class="project-title">\s+<a.*?>\s+<span class="overflow-tip">(.*?)\s*</span></a>\s+</h1>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'
