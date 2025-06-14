import requests
import folium

def get_geolocation(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

def show_location_on_map(lat, lon, city):
    map_ = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup=f"Location: {city}").add_to(map_)
    map_.save("location_map.html")
    print("Map saved as location_map.html")

# Get IP from user (optional)
ip = input("Enter an IP address (or press Enter to use your own): ")

if not ip:
    # Get your own IP
    ip = requests.get("https://api.ipify.org?format=json").json()["ip"]

location = get_geolocation(ip)

if location["status"] == "success":
    print(f"Public IP: {ip}")
    print(f"Country: {location['country']}")
    print(f"Region: {location['regionName']}")
    print(f"City: {location['city']}")
    print(f"Latitude: {location['lat']}")
    print(f"Longitude: {location['lon']}")
    
    # Show on map
    show_location_on_map(location['lat'], location['lon'], location['city'])

else:
    print("Failed to retrieve location.")

