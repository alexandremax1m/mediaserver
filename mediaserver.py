import json, folium
from url import URL

urls, plotdata,datadict = [],[],{}

while int(input('1 To Add URL, -1 To Cancel : ')) != int(-1):
    urls.append(str(input('Your URL Sir : ')))

for n in range(len(urls)):
    plotdata.append([])
    if not plotdata[n]:
        plotdata[n] = [float(x) for x in URL(urls[n]).ipinfo()['loc'].split(',')]
    map = folium.Map(location=plotdata[n])
    map.add_child(folium.Marker(location=plotdata[n]))
    map.save(f'{URL(urls[n]).url[4:-4]}.html')
    datadict.update({f'{URL(urls[n]).url[4:-4]}':URL(urls[n]).ipinfo()['city']})

open(f"{str(input('Your Json Output File Name Sir :: '))}.json",'a+',encoding='UTF-8').write((json.dumps(datadict,sort_keys=True, indent=4)))
del urls,plotdata,datadict
