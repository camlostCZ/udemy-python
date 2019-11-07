import urllib.request
import json

URL = "https://geoip-db.com/json"

def locate_ip(ip_address=""):
    url_str = URL
    if len(ip_address) > 0:
        url_str = "{}/{}".format(URL, ip_address)
    with urllib.request.urlopen(url_str) as url:
        result = json.loads(url.read().decode())
    return result

data = locate_ip()
#print(data)

print("IP address:  {}".format(data["IPv4"]))
print("Country:     {} ({})".format(data["country_name"], data["country_code"]))
print("City:        {}".format(data["city"]))
print("Postal code: {}".format(data["postal"]))
print("LAT x LONG:  {}, {}".format(data["latitude"], data["longitude"]))
