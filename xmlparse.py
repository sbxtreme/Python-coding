import xml.etree.ElementTree as ET
tree = ET.parse("data.xml")
doc = tree.getroot()
values = doc.find('body/filAckNack/message/Message')
print(values[2].text)