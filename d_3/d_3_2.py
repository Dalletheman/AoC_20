from tools.tools import data_read

def get_num_trees(field, delta_x, delta_y):
    n_trees = 0
    x = 0
    y = 0
    height = len(field) - 1
    width = len(field[0])
    while y < height:
        x = (x + delta_x) % width
        y = y + delta_y
        obj_xy = field[y][x]
        if obj_xy == "#":
            n_trees+=1
    return n_trees

def main():
    data_reader = data_read(0)
    array_str = data_reader.read("input.txt")
    delta_x = [1, 3, 5, 7, 1]
    delta_y = [1, 1, 1, 1, 2]
    n_trees_array = []
    for i in range(0,len(delta_x)):
        n_trees = get_num_trees(array_str, delta_x[i], delta_y[i])
        n_trees_array.append(n_trees)
    prod = 1
    for n in n_trees_array:
        prod = prod * n
    print("Trees approached: {}".format(n_trees_array))
    print("Prod is: {}".format(prod))
main()