import json, folium
from url import URL

urls, plotdata,datadict = [],[],{}

while int(input('1 To Add URL, -1 To Cancel : ')) != int(-1):
    urls.append(str(input('Your URL Sir : ')))

for n in range(len(urls)):
    plotdata.append([])
    if not plotdata[n]:
        try : plotdata[n] = [float(x) for x in URL(urls[n]).ipinfo()['loc'].split(',')]
        except TypeError:
            plotdata[n] = str('string') 
    map = folium.Map(location=plotdata[n]) if not type(plotdata[n]) == str else print('Map Can Not Be Created For This URL')
    map.add_child(folium.Marker(location=plotdata[n])) if not type(plotdata[n]) == str else print('Map Can Not Be Created For This URL')
    map.save(f'{URL(urls[n]).url[4:-4]}.html') if map else print('Map Not Created Sir')
    datadict.update({f'{URL(urls[n]).url[4:-4]}':URL(urls[n]).ipinfo()['city']}) if map else print('URL Not Valid For This Operation')

open(f"{str(input('Your Json Output File Name Sir :: '))}.json",'a+',encoding='UTF-8').write((json.dumps(datadict,sort_keys=True, indent=4)))
del urls,plotdata,datadict
