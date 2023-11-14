n = int(input())

parked_cars = set()

for _ in range(n):
    command = input().split(", ")

    if command[0].lower() == "in":
        parked_cars.add(command[1])
    elif command[0].lower() == "out" and command[1] in parked_cars:
        parked_cars.remove(command[1])

if parked_cars:
    for car in parked_cars:
        print(car)
else:
    print("Parking is Empty")
