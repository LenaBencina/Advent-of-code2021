with open('Input/input2.txt') as f:
    instructions = f.read().splitlines()

instructions_dict1 = {'forward': lambda x, y, c: (x + c, y),
                     'down': lambda x, y, c: (x, y + c),
                     'up': lambda x, y, c: (x, y - c)}

instructions_dict2 = {'forward': lambda x, y, z, c: (x + c, y + (z * c), z),
                     'down': lambda x, y, z, c: (x, y, z + c),
                     'up': lambda x, y, z, c: (x, y, z - c)}

# initialize
x_tmp1, y_tmp1 = 0, 0
x_tmp2, y_tmp2, z_tmp2 = 0, 0, 0

for step in instructions:
    direction, c_tmp = step.split(' ')
    (x_tmp1, y_tmp1) = instructions_dict1[direction](x_tmp1, y_tmp1, int(c_tmp))  # part 1
    (x_tmp2, y_tmp2, z_tmp2) = instructions_dict2[direction](x_tmp2, y_tmp2, z_tmp2, int(c_tmp))  # part 2

print(x_tmp1 * y_tmp1)
print(x_tmp2 * y_tmp2)

