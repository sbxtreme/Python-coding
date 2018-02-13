import xml.etree.ElementTree as ET
tree = ET.parse("data.xml")
root = tree.getroot()
values = root.find('body/filAckNack/message/Message')
print(values[2].text)
