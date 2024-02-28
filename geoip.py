import geocoder
import folium
me=input("enter your valid IP address:")
g=geocoder.ip(me)

myAddress= g.latlng
print(myAddress)

map=folium.Map(location=myAddress,zoom_start=10)
folium.CircleMarker(location=myAddress,radius=30,popup=me).add_to(map)
folium.Marker(myAddress,popup=me).add_to(map)

map.save("my_map.html")

