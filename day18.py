import math

def explode(snail_number, position):
    left_num = int(snail_number[position])
    right_num = int(snail_number[position+2])
    
    for i in range(position-1, -1, -1):
        if snail_number[i].isdigit():
            snail_number[i] = str(int(snail_number[i]) + left_num)
            break

    for i in range(position+3, len(snail_number)):
        if snail_number[i].isdigit():
            snail_number[i] = str(int(snail_number[i]) + right_num)
            break

    snail_number = snail_number[:position-1] + ["0"] + snail_number[position+4:]

    return snail_number

def split(snail_number, position):
    num = int(snail_number[position])
    left_num = str(math.floor(num / 2))
    right_num = str(math.ceil(num / 2))

    snail_number = snail_number[:position] + ["["] + [left_num] + [","] + [right_num] + ["]"] + snail_number[position+1:]

    return snail_number

def calc_magnitude(snail_number):
    if isinstance(snail_number, int):
        return snail_number

    return 3 * calc_magnitude(snail_number[0]) + 2 * calc_magnitude(snail_number[1])

def add_snail_numbers(num1, num2):
    result = ["["] + num1 + [","] + num2 + ["]"]

    reduced = False
    while not reduced:
        nested_count = 0
        exploded = been_split = False
        for i, char in enumerate(result):
            if char.isdigit() and nested_count > 4:
                result = explode(result, i)
                exploded = True
                break
            elif char == "[":
                nested_count += 1
            elif char == "]":
                nested_count -= 1

        if not exploded:
            for i, char in enumerate(result):
                if char.isdigit() and int(char) > 9:
                    result = split(result, i)
                    been_split = True
                    break

        if not exploded and not been_split:
            reduced = True

    return result

if __name__ == "__main__":
    with open("data/input18.txt", "r") as f:
        snail_numbers = [list(row) for row in f.read().split("\n")]

    number1 = snail_numbers[0]
    for number2 in snail_numbers[1:]:
        number1 = add_snail_numbers(number1, number2)
    print(f"Part 1: {calc_magnitude(eval("".join(number1)))}")

    max_mag = 0
    for number1 in snail_numbers:
        for number2 in snail_numbers:
            if number1 != number2:
                result = add_snail_numbers(number1, number2)
                max_mag = max(max_mag, calc_magnitude(eval("".join(result))))
    print(f"Part 2: {max_mag}")