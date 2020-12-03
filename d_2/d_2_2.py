from tools.tools import data_read

def parser(input):
    return input.split(" ")

def check_valid_psk(input):
    [n_first, n_second] = input[0].split("-")
    char = input[1][0]
    password = input[2]
    count = 0
    if char == password[int(n_first) - 1]:
        count+=1
    if char == password[int(n_second) - 1]:
        count+=1
    return count%2

def main():
    data_reader = data_read(0)
    array_str = data_reader.read("input.txt")
    valid_count = 0
    for i in array_str:
        parse_output = parser(i)
        res = check_valid_psk(parse_output)
        if res:
            valid_count += 1
    print("Valid count: {}".format(valid_count))
main()