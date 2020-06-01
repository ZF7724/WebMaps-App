import folium
import geocoder
import pandas

def colorchanger(el):
    if el<1000:
        return 'green'
    elif el>=1000 and el<2000:
        return 'orange'
    elif el>=2000:
        return 'red'
    

def location():
    g = geocoder.ip('me')
    latlng=g.latlng
    return latlng
    


def main():
    
    
    data=pandas.read_csv("original.txt")
    lat=list(data["LON"])
    lon=list(data["LAT"])
    elev=list(data["ELEV"])

    
    

    latlng=location()
    
    
    map=folium.Map(location=latlng,zoom_start=12)
    
    Feature1=folium.FeatureGroup(name="Volcanoes in America")
    
    
    for latitude,longitude,el in zip(lon,lat,elev):
        Feature1.add_child(folium.CircleMarker(location=[latitude,longitude],popup=el,fill_color=colorchanger(el),fill_opacity=0.7,radius=6,color="green"))
    
    
    Feature2=folium.FeatureGroup(name="Country Population")
    
    
    Feature2.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(), 
    style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 
    else 'orange' if 10000000<= x['properties']['POP2005']<100000000 else 'red'}))
    
    
    
    map.add_child(Feature1)
    map.add_child(Feature2)
    map.add_child(folium.LayerControl())
    
    
    map.save("Map2.html")


main()




