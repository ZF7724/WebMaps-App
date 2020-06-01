import folium
import geocoder

def location():
    g = geocoder.ip('me')
    latlng=g.latlng
    return latlng

def main():
    latlng=location()
    map=folium.Map(location=latlng,zoom_start=12)
    
    for newMarkers in [[43.262019, -79.913012],[54.2, -89.91]]:
        map.add_child(folium.Marker(location=newMarkers,popup="REVIEW 1",icon=folium.Icon(color="red")))
    
    
    
    
    map.save("Map1.html")


main()

































