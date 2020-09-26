from lxml import etree

xml_path = "../data/vitamin-d.xml"
# w = open("../data/vitamin.txt", 'w', encoding="utf-8")
xml = etree.parse(xml_path)
root = xml.getroot()
num = 1
res = {}

for node in root.getchildren():
    # w.write("====== NO."+str(num)+"protein ======\n")
    num += 1
    for i in node.getchildren():
        print(i)
        # if i.tag == 'protein':
        #     w.write("====== basic info about protein ======\n")
        #     if i.tag == "recommendedName":
        #         print(i)
        #     w.write("====== feature about protein ======\n")
        # if i.tag == '{http://uniprot.org/uniprot}feature':
        #     w.write("type:" + str(i.get("type")) + "  description:" + str(i.get("description")) + '\n')

