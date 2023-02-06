circle_of_cats = {}

# for i in range(1, 101):
#     circle_of_cats[i] = "hat"
cats = 100
counter = 1
while counter <= cats:
    if counter == 1:
        for counter in range(1, 101):
            circle_of_cats[counter] = "hat"
        counter = counter + 1
    elif counter % counter == 0:
        circle_of_cats[counter] = "no hat"
        counter = counter + 1

    # elif counter % counter == 0:
    #     circle_of_cats[i] == "no hat"

# for i in range(1, 101):
#     if i % 2 == 0 and circle_of_cats[i] == "hat":
#         circle_of_cats[i] = "no hat"
    
print(circle_of_cats)