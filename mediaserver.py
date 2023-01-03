import json, folium
from url import URL

urls, plotdata = [],[]

while int(input('1 To Add URL, -1 To Cancel : ')) != int(-1):
    urls.append(str(input('Your URL Sir : ')))

for n in range(len(urls)):
    plotdata.append([])
    if not plotdata[n]:
        plotdata[n] = [float(x) for x in URL(urls[n]).ipinfo()['loc'].split(',')]
    map = folium.Map(location=plotdata[n])
    map.add_child(folium.Marker(location=plotdata[n]))
    map.save(f'{URL(urls[n]).url[4:-4]}.html')
