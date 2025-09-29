import requests

def iss_locatie() -> dict:
    #Documentation: http://open-notify.org/Open-Notify-API/ISS-Location-Now/

    r = requests.get("http://api.open-notify.org/iss-now.json")
    return r.json()

def weer_op_locatie(latitude: str, longitude: str) -> dict:
    #Documentation: https://github.com/Yeqzids/7timer-issues/wiki/Wiki
    #               https://www.7timer.info/doc.php

    #The "ac" param defaults to 0, so it does not have to be defined in the request
    #In the exercise, the "product" param is not required, but is required to get a valid response
    payload = {
        "lon": float(longitude),
        "lat": float(latitude),
        "unit": "metric",
        "output": "json",
        "product": "civil"
    }
    r = requests.get("http://www.7timer.info/bin/api.pl", params=payload)
    return r.json()
