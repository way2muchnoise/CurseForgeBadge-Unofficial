import fnmatch
import gzip
import os
import re
from HTMLParser import HTMLParser

import CFReader

directory = raw_input('dir to read: ')
output = file(raw_input('output file: '), 'w')
if not directory.endswith('/'):
    directory += '/'
pattern = re.compile(r'GET /(.*?\.svg) ')
calls = []
for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, 'access.log-*.gz'):
        print 'Analysing ' + filename
        with gzip.open(directory + filename, 'rb') as f:
            for line in f.read().split('\n'):
                match = pattern.search(line)
                if match:
                    calls.append(match.group(1))
idPattern = re.compile(r'(((full|short|small)_)|(versions/(.*?_(?=.*?_))?))?(?P<project>.*?)((_.*)|\.svg)')
resolve = []
for item in set(calls):
    resolve.append(idPattern.search(item).group('project'))
projects = []
h = HTMLParser()
for project in set(resolve):
    projects.append(h.unescape(CFReader.get_tile(project)).strip())
for project in set(projects):
    output.write(project + '\n')
