import urllib.request
import urllib.parse
import json

def iss_locatie() -> dict:
    #Documentation: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
    with urllib.request.urlopen("http://api.open-notify.org/iss-now.json") as response:
        return json.loads(response.read().decode())

def weer_op_locatie(latitude: str, longitude: str) -> dict:
    #Documentation: https://github.com/Yeqzids/7timer-issues/wiki/Wiki
    #               https://www.7timer.info/doc.php

    #The "ac" param defaults to 0, so it does not have to be defined in the request
    #In the exercise, the "product" param is not required, but is required to get a valid response
    params = {
        "lon": float(longitude),
        "lat": float(latitude),
        "unit": "metric",
        "output": "json",
        "product": "civil"
    }
    payload = urllib.parse.urlencode(params)
    request_url = "http://www.7timer.info/bin/api.pl?" + payload
    with urllib.request.urlopen(request_url) as response:
        return json.loads(response.read().decode())
