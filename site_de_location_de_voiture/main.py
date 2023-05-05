from bs4 import BeautifulSoup
import requests
from item.models import Cars


def get_car_price():
    url = "https://www.discovercars.com/morocco?keyword=%2Bcar%20%2Bhire%20%2Bmorocco&network=g&gclid=Cj0KCQjw0tKiBhC6ARIsAAOXutkiflF9lHMlc5wR3ubz6Yw7lz6T_31TH6Npggb52NcMkQmPcNa8p1QaAhOlEALw_wcB"
    response = requests.get(url).text
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find("span", {"class": "landing-cb-price open-pick-modal"})
    return price.text

def update_rent_price(car):
    price = get_car_price()
    Cars.rent_price = price
    car.save()

def update_car_prices():
    cars = Cars.objects.all()
    for car in cars:
        update_rent_price(car)   