import xml.etree.ElementTree as ET
from xml.dom import minidom

xmldoc = minidom.parse('Object_Repository/LoginPage.xml')
xmlDoc = xmldoc.getElementsByTagName('Element')

#tree = ET.parse('Object_Repository/LoginPage.xml')

elementsDict = {}
print(len(xmlDoc))
print(xmlDoc[0].attributes['name'].value)
for s in xmlDoc:
    key = s.attributes['name'].value
    param = s.getElementsByTagName('param')
    value = param[0].attributes['value'].value
    # print(param[0].attributes['type'].value)
    # print(s.attributes['name'].value)
    elementsDict[key] = value
print(elementsDict)

newsitems = []
root = tree.getroot()
# iterate news items
for item in root.findall('Element/param'):

    # empty news dictionary
    news = {}

    # iterate child elements of item
    for type_tag in item:
        value = type_tag.get('param')

    # append news dictionary to news items list
    newsitems.append(news)

def new_fun(n):
    yield 1
    yield 100


print(new_fun(1))

