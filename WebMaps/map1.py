import folium
import pandas
data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    else:
        return 'red'
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
map = folium.Map(location=[21.18,72.84],zoom_start=6,tiles="Mapbox Bright")

fgv=folium.FeatureGroup(name="My Map")

for lt,ln,el,name in zip(lat,lon,elev,name):

    iframe = folium.IFrame(html=html % (name,name,str(el)), width=200,height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius = 6,popup=folium.Popup(iframe),color='grey',fill=True,fill_opacity=0.7,fill_color=color_producer(el)))

fgv.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig'),style_function=lambda x: {'fill_color':'yellow'}))

map.add_child(fgv)

map.save("Map1.html")
