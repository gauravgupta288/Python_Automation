from xml.dom import minidom

class XMLParse:

    @classmethod
    def parseXML(self, filename):
        print(filename)
        filename = 'Object_Repository/'+filename
        print(filename)
        xmlDoc = minidom.parse(filename)
        xmlDoc = xmlDoc.getElementsByTagName('Element')
        elementsDict = {}
        for s in xmlDoc:
            key = s.attributes['name'].value
            param = s.getElementsByTagName('param')
            value = param[0].attributes['value'].value
            elementsDict[key] = value
        return elementsDict

