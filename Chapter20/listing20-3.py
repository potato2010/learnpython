import sys, re
from util import *

print '<html><head><title>...</title><body>'

title = True
f = open('listing20-1.txt')
for block in blocks(f):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'
f.close()