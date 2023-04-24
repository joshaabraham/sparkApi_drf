import geocoder

def get_coordinates_from_ip(ip_address):
    g = geocoder.ip(ip_address)

    if g.ok:
        return g.latlng
    else:
        return None

ip_address = "8.8.8.8"  # Remplacez cette valeur par l'adresse IP souhaitée
coordinates = get_coordinates_from_ip(ip_address)

if coordinates:
    print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")
else:
    print("Impossible d'obtenir les coordonnées géographiques.")