from tools.tools import data_read
def readdata():
    with open('input.txt') as f:
        data = f.read().splitlines()
    return data

def get_entries_three(array, sum):
    count = 0
    for i in array:
        if i > sum:
            count+=1
            continue
        res = get_entries_inner(array[count + 1:], sum - i)
        if res:
            res.append(i)
            return res
        count+=1
    return None

def get_entries_inner(array, sum):
    count = 0
    for i in array:
        if i > sum:
            count+=1
            continue
        for j in array[(count + 1):]:
            if (i + j) == sum:
                return [i,j]
        count+=1
    return None

def main():
    data_reader = data_read(0)
    array_str = data_reader.read("input.txt")
    array_int = data_reader.data_array_to_int(array_str)

    entries = get_entries_three(array_int, 2020)
    product = entries[0]*entries[1]*entries[2]
    print("Entry a: {}, Entry b: {}, Entry c:{}".format(entries[0], entries[1], entries[2]))
    print("Product is: {}".format(product))
main()