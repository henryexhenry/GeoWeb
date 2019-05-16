import json
import requests
from shutil import copyfile

with open('save.json') as f:
    countries = json.load(f)

# for country in countries:
#     if country['img']:
#         with open('static/images/'+country['id']+'.jpg', 'wb') as handle:
#             response = requests.get(country['img'], stream=True)

#             if not response.ok:
#                 print(response)

#             for block in response.iter_content(1024):
#                 if not block:
#                     break

#                 handle.write(block)

noImg = [
18,
40,
44,
56,
68,
75,
117,
119,
121,
128,
135,
136,
137,
140,
162,
169,
170,
176,
177,
190,
208,
228
]
for i in noImg:
    copyfile('static/images/noImg.png', 'static/images/'+countries[i]['id']+'.jpg')
    


