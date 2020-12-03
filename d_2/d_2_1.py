from tools.tools import data_read

def parser(input):
    return input.split(" ")

def check_valid_psk(input):
    [n_lower, n_upper] = input[0].split("-")
    char = input[1][0]
    n_string = input[2].count(char)
    if n_string >= int(n_lower) and n_string <= int(n_upper):
        return True
    return False

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