import requests;
import os;

Google_API_KEY = os.getenv("Google_API_KEY")

class GoogleOperations:
    def getAddressCoordinates(address):
        googleUrl = "https://maps.google.com/maps/api/geocode/json?address=" + address + "&key=" + Google_API_KEY;
        googleResponse = requests.get(googleUrl);
        return googleResponse["results"]["geometry"]["location"];