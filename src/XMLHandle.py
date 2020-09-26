from lxml import etree

xml_path = "../data/vitamin-d.xml"
w = open("../data/vitamin-d_XML_afterHandle.txt", 'w', encoding="utf-8")
xml = etree.parse(xml_path)
root = xml.getroot()
num = 1
res = {}

for node in root.getchildren():
    w.write("====== NO." + str(num) + "protein ======\n")
    num += 1
    for i in node.getchildren():

        if i.tag == '{http://uniprot.org/uniprot}name':
            w.write("Protein Name: " + str(i.text) + "\n")

        if i.tag == '{http://uniprot.org/uniprot}feature':
            w.write("type:" + str(i.get("type")) + "  description:" + str(i.get("description")) + '\n')
