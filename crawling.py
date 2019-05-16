import requests
import xml.etree.ElementTree as ET
import time
from lxml import etree
import json

xmltree = ET.parse('mondial-3.0.xml')
xmlroot = xmltree.getroot()


countries = []
for ctry in xmlroot.findall('./country'):
    country = ctry.attrib['name']
    _id = ctry.attrib['id']
    countries.append({'name':country, 'id': _id})
print(countries)
count = 0
for c in range(len(countries)):

    target = 'https://www.flaticon.com/search?word=' + countries[c]['name'] + '&style_id=141'

    res = requests.get(target)

    html = etree.HTML(res.text)

    img = html.xpath('//div[contains(@class, "icon--holder")]/img/@src')

    try:
        print(str(c)+' : '+img[0])
        countries[c]['img'] = img[0]
    except:
        count += 1
        print(str(c)+' : '+'no img ;' + ' count: '+str(count))
        countries[c]['img'] = ''

print(countries)

with open('save.json', 'w') as f:
    json.dump(countries, f)


