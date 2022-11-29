import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
print(data)

lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])

def color_producer(elvn):
    if elvn<1000:
        return "green"
    elif 1000 <= elvn <3000 :
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58, -99.1],zoom_start = 6, tiles = "Stamen Terrain")
fgv= folium.FeatureGroup(name = "Volcano")

for lt,ln,el in zip(lat,lon,elv):  #to iterate more than one kist at same time
    fgv.add_child(folium.CircleMarker(location=[lt,ln],popup= str(el)+"m" ,radius=6,fill_color=color_producer(el),color = "grey",fill_opacity = 0.7,))

fgp= folium.FeatureGroup(name = "Population")
    
fgp.add_child(folium.GeoJson(data =open('world.json','r',encoding= 'utf-8-sig').read(), style_function= lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }  ))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map8.html")