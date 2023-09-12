import sys
input = sys.stdin.readline

iter_num = int(input())

for i in range(iter_num):
    num_friend, num_car, num_area = map(int, input().split())
    drunk_list = []
    not_drunk_list = []
    car_list = []
    car_with_driver = []

    for _ in range(num_friend):
        friend_info = input().split()
        if friend_info[1] == "I":
            drunk_list.append(friend_info[0])
        else:
            not_drunk_list.append(friend_info[0])

    for _ in range(num_car):
        car_list.append(input().split())

    for not_drunk in not_drunk_list:
        for car in range(len(car_list)):
            if not_drunk == car_list[car][0]:
                car_list[car][1] = str(int(car_list[car][1]) - 1)
                car_with_driver.append(car_list.pop(car))
                break
    car = 0
    while car_with_driver:
        for r in range(len(drunk_list)):
            if car_with_driver[car][0] == drunk_list[r]:
                car_with_driver[car][1] = str(int(car_with_driver[car][1]) - 1)
                drunk_list.pop(r)
                break
        if car_with_driver[car][1] == "0":
            car_with_driver.pop(car)