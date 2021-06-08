from xml.dom import minidom


class XMLParse:
    # This method will create dictionary of elements used in xpath
    @staticmethod
    def parseXML(filename):
        filename = 'Object_Repository/'+filename
        xmlDoc = minidom.parse(filename)
        xmlDoc = xmlDoc.getElementsByTagName('Element')
        elementsDict = {}
        for s in xmlDoc:
            key = s.attributes['name'].value
            param = s.getElementsByTagName('param')
            value = param[0].attributes['value'].value
            elementsDict[key] = value
        return elementsDict

