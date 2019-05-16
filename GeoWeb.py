from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from services import getImgsByContinentId, getCountriesByContinentId, getCountryElementByCountryId, getCitiesByCountryId, getCityNameByCityId, getEcoByCountryId, getCountryIdByCountryName

app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

ctnDict = {'Asia': 'f0_123', 'Europe':'f0_119', 'America': 'f0_126', 'Australia':'f0_129', 'Africa':'f0_132'}

history = []

@app.route('/')
def gotohome():
    return redirect(url_for('home', continent='Asia'))

@app.route('/continent/<continent>')
def home(continent='Asia'):
    imgs = getImgsByContinentId(ctnDict[continent])
    ctries = getCountriesByContinentId(ctnDict[continent])
    return render_template('home.html', continent = continent, imgs = imgs, countries= ctries)

@app.route('/country/<country>')
def detail(country):
    if session.get('history') == None:
        session['history'] = []     # initiating history list for a session
    
    if country[0:2] != 'f0':
        country = getCountryIdByCountryName(country)
        
    ele = getCountryElementByCountryId(country)

    ctnid = ele.find('encompassed').attrib['continent'] # obtaining continent id
    
    if ele.attrib['name'] not in session['history']:
        session['history'].append(ele.attrib['name'])   # appending visited item into history for a session
    else:
        session['history'].remove(ele.attrib['name'])
        session['history'].append(ele.attrib['name'])
    if len(session['history']) > 10:
        history = session['history'][::-1][:10]
    else:
        history = session['history'][::-1]

    for i, j in ctnDict.items():  # find ctn name by ctn id
        if j == ctnid:
            ctn = i

    cities = getCitiesByCountryId(country)

    # obtaining all items in ecosystem and storing them into a dictionary
    ECODict = {'mountain':'', 'desert':'', 'island':'', 'river':'', 'lake':'', 'sea':''}
    for eco in ECODict.keys():
        ECODict[eco] = getEcoByCountryId(country, eco)

    capital = getCityNameByCityId(ele.attrib['capital'])

    return render_template('detail.html', countryEle=ele, continent=ctn, cities=cities, ECOs=ECODict, history=history, capital=capital)