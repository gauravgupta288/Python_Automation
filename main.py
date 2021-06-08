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


def IsLeapYear(year):
    if (year%100 != 0 and year%4 == 0) or year%400 == 0:
        return True
    else:
        return False


def ChangeStringCase(str):
    for i in str:
        print(chr(i))
        if ascii(i) >=65 and ascii(i) <=95:
            print(chr(ascii(65+26)))


ChangeStringCase('wwW.aFourTecH.Com')
print(IsLeapYear(1904))
