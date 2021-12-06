import json
if __name__ == '__main2__':

    # Opening JSON file
    f = open('input.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['cars']:
        print(i)

    # Closing file
    f.close()

    #Write to json files

    slow_car_list = list(filter(lambda car: car["hp"] < 120, data["cars"]))
    for car in slow_car_list:
        print(car)
        with open("slow_cars.json", "w") as outfile:
            json.dump(slow_car_list, outfile)

    fast_car_list = list(filter(lambda car: 120 <= car["hp"] < 180, data["cars"]))
    for car in fast_car_list:
        print(car)
        with open("fast_cars.json", "w") as outfile:
            json.dump(fast_car_list, outfile)

    sport_car_list = list(filter(lambda car: car["hp"] >= 180, data["cars"]))
    for car in sport_car_list:
        print(car)
        with open("sport_cars.json", "w") as outfile:
            json.dump(sport_car_list, outfile)

    cheap = list(filter(lambda car: car["price"] < 1000, data["cars"]))
    for car in fast_car_list:
        print(car)
        with open("cheap_cars.json", "w") as outfile:
            json.dump(fast_car_list, outfile)

    medium = list(filter(lambda car: 1000 <= car["price"] < 5000, data["cars"]))
    for car in fast_car_list:
        print(car)
        with open("medium_cars.json", "w") as outfile:
            json.dump(fast_car_list, outfile)

    expensive = list(filter(lambda car: car["price"] >= 5000, data["cars"]))
    for car in fast_car_list:
        print(car)
        with open("expensive_cars.json", "w") as outfile:
            json.dump(fast_car_list, outfile)