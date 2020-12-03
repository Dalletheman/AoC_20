def readdata():
    with open('input.txt') as f:
        data = f.read().splitlines()
    return data

def get_entries(array, sum):
    count = 0
    for i in array:
        i = int(i)
        if i > sum:
            continue
        for j in array[(count + 1):]:
            j = int(j)
            if (i + j) == sum:
                return [i,j]
    return None

def main():
    array = readdata()
    entries = get_entries(array, 2020)
    print("Entry a: {}, Entry b: {}".format(entries[0], entries[1]))

main()