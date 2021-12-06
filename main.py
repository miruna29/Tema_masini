
car1={
    "id": 1,
    "brand": "Mercedes",
    "model": "C-Klass",
    "hp": 190,
    "price": 50000
}
car2={
    "id": 2,
    "brand": "Ford",
    "model": "Focus",
    "hp": 110,
    "price": 10000
}
car3={
    "id": 3,
    "brand": "Skoda",
    "model": "Octavia",
    "hp": 100,
    "price": 900
}
car4={
    "id": 4,
    "brand": "Audi",
    "model": "A4",
    "hp": 140,
    "price": 3000

}
car5={
    "id": 5,
    "brand": "Volkswagen",
    "model": "Passat",
    "hp": 200,
    "price": 14500
}
if __name__ == '__main__':
    car_list=[car1,car2,car3,car4,car5]

    slow_car_list = list(filter(lambda car: car["hp"] < 120, car_list))
    print(f"Slow car_list : {slow_car_list}")

    fast_car_list = list(filter(lambda car: 120 <= car["hp"] < 180, car_list))
    print(f"Fast car_list : {fast_car_list}")

    sport_car_list = list(filter(lambda car: car["hp"] >= 180, car_list))
    print(f"Sport car_list : {sport_car_list}")

    cheap = list(filter(lambda car: car["price"] < 1000, car_list))
    print(f"Cheap car_list : {cheap}")

    medium = list(filter(lambda car: 1000 <= car["price"] < 5000, car_list))
    print(f"Medium car_list : {medium}")

    expensive = list(filter(lambda car: car["price"] >= 5000, car_list))
    print(f"Expensive car_list : {expensive}")

    for car in car_list:
        print(car)



