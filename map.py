import pandas
import folium

vol = pandas.read_csv("Volcanoes.csv")

elev = list(vol["ELEV"])

lat = list(vol["LAT"])

lon = list(vol["LON"])

name = list(vol["NAME"])

loc = list(vol["LOCATION"])

map = folium.Map(location=[80, -100], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

def marker_color(elevat):
    if elevat < 1000:
        return "blue"
    elif  1000 < elevat < 3000:
        return "orange"
    else:
        return "red"



for lt, ln, el, nm, lc in zip(lat, lon, elev, name, loc):
    fgv.add_child(folium.CircleMarker(fill=True, fill_opacity=.6, location=[lt, ln], popup= nm + ", " + lc + ", "+ str(el), fill_color=marker_color(el), color=marker_color(el) ))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x:{'fillColor':"green" if x['properties']['POP2005']< 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")

