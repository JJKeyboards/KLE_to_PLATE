import json

file = "test_w_h.json"


def fill_dict(legend, x, y, w, h):
    key_dict["legend"] = legend
    key_dict["x_pos"] = x
    key_dict["y_pos"] = y
    key_dict["w"] = w
    key_dict["h"] = h
    


with open(file) as json_file:
    data = json.load(json_file)

key_dict = {}
key_arr = []

x_pos = 0
y_pos = 0

x_cord = 0
y_cord = 0


counter_y = 0
counter_x = 0

class Switch:
    def __init__(self):
        self.width = 1
        self.height = 1
        
        self.coord_x=0
        self.coord_y=0

        self.pos_x =x_var




for y in data:
    for x in range(len(y)):
        width = 1
        height = 1
        item = y[x]

        if x-1 >= 0:
            cords = y[x-1]
        else:
            cords = y[x]

        if str(item).startswith("{") == False:
            

            if str(cords).startswith("{") == True:

                if "w" in cords:
                    width = 0
                    width = width+cords["w"]

                if "h" in cords:
                    height = 0
                    height = height+cords["h"]

            fill_dict(item, 0, 0, width, height)
            key_arr.append(key_dict)
        key_dict = {}
    
    







#print(key_arr)
print(counter_y)
print(counter_x)
