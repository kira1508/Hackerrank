import urllib.request
from xml.dom import minidom
import re
import xml.etree.ElementTree as ET


document = ('https://docs.python.org/3.4/library/xml.etree.elementtree.html')
web = urllib.request.urlopen(document)
get_web = web.read()
xmldoc = minidom.parseString(get_web)

xmldoc=xmldoc.toprettyxml()
open('xmldoc.txt','w+')

#print(xmldoc)
tree = ET.parse('xmldoc.txt')
root = tree.getroot()