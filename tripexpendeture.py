def hotel_price(nights):
    return 140*nights
def plane_ride_cost(city):
    if "Boston" == city:
        return 183
    elif "Seattle" == city:
        return 220
    elif "Portland" == city:
        return 300
    elif "Los angeles" == city:
        return 475

def rental_car_price(days):
    if days >= 7:
        return 40*days - 50
    elif days <= 3 :
        return 40*days - 20
    else: return 40*days
def trip_price(city, days, spending_money):
    return rental_car_price(days) + hotel_price(days) + plane_ride_cost(city)+ spending_money

print("Cost of car: ", rental_car_price(6))

print("Cost of plane:", plane_ride_cost("Boston"))
print("Cost of hotel:", hotel_price(7))
print("Trip cost:", trip_price("Boston", 7, 500))