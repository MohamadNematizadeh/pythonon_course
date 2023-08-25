from xml.etree import ElementTree as ET
tree = ET.parse('xml_dat/Food.xml')
root = tree.getroot()
for child in root.iter('child'):
    print(child.tag, child.attrib)
    
for element in root.iter('element'):
    print(element.text)

food = ET.SubElement(root, 'Food')
food.text = 'Morgh'
print(food)
tree.write('xml_dat/Food_output.xml')