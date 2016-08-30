import re
import urllib2


def get_downloads(category, project):
    response = urllib2.urlopen("https://minecraft.curseforge.com/" + category + "/" + project).read()
    pattern = 'Total Downloads</div>\s+<div class="info-data">(.*?)</div>'
    m = re.search(pattern, response)
    if m:
        return m.group(1)
    else:
        return 'Error'
