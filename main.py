import json

with open("test3rows.json") as json_file:
    data = json.load(json_file)


key_dict = {}
key_arr = []


x_pos = 0
y_pos = 0

for i in data:
    x = len(i)
    for j in range(x):
        line = i[j]

        if j-1 >= 0:
            cords = i[j-1]
        else:
            cords = i[j]
        
        if str(line).startswith("{") == False:
            key_dict["key"] = line

            if str(cords).startswith("{") == True:

                # x-pos
                if "x" in cords:

                    key_dict["x_pos"] = cords["x"]
                # y-pos
                if "y" in cords:

                    key_dict["y-pos"] = cords["y"]
            
            key_arr.append(key_dict)
            key_dict = {}


print(key_arr)
# print(data[3][0]["y"])
# print(data[3][0])


# [['A', 'B'], [{'y': 0.25}, 'C', {'x': 1}, 'D']]
