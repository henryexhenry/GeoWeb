import lxml.etree

root = lxml.etree.parse('mondial-3.0.xml')

def getCityNameByCityId(cityId):
    res = root.xpath('//city[@id="'+cityId+'"]/name')[0]
    return res.text

def getImgsByContinentId(ctnid):   # ctnid -> [img]
    L = []
    for img in root.xpath('continent[@id="'+ctnid+'"]//img/@src'):
        L.append(img)
    return L

def getCountriesByContinentId(ctnid):   # ctnid -> [country]
    L = []
    for ctry in root.xpath('country[./encompassed/@continent="'+ctnid+'"]'):
        L.append({'name':ctry.attrib['name'], 'id':ctry.attrib['id']})
    return L

def getCountryIdByCountryName(ctryName):
    res = root.xpath('country[@name="'+ctryName+'"]/@id')
    if type(res) == list:
        return res[0]
    return res

def getCountryElementByCountryId(ctryid):
    res = root.xpath('country[@id="'+ctryid+'"]')
    if type(res) == list:
        return res[0]
    return res

def getCitiesByCountryId(ctryid): #ctryid -> [city]
    res = root.xpath('country[contains(@id, "'+ctryid+'")]//city[contains(@latitude, ".")]')
    return res

def getEcoByCountryId(ctryid, ECO): #ctryid -> [Sea]
    res = root.xpath(ECO+'[./located/@country="'+ctryid+'"]')
    if len(res) > 10:
        return res[:10]
    return res

