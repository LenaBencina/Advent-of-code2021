with open('Input/input3.txt') as f:
    numbers = f.read().splitlines()

# 1 part
n = len(numbers)
gamma_binary = []
for i in range(len(numbers[0])):  # for each bit
    gamma_bit = 0
    for j in range(n):  # for each number
        gamma_bit += int(numbers[j][i])
    gamma_binary.append((gamma_bit > n / 2))

eps_binary = [not b for b in gamma_binary]

get_decimal = lambda binary: sum([2 ** p * binary[len(binary) - 1 - p] for p in range(len(binary))])

gamma = get_decimal(gamma_binary)
eps = get_decimal(eps_binary)

print(gamma * eps)


# 2 part
def get_numbers(numbers, bit_position, more_or_less):

    n = len(numbers)
    bits_by_position = [int(numbers[j][bit_position]) for j in range(n)]

    number_to_use = int(sum(bits_by_position) >= n/2)
    number_to_use = number_to_use if more_or_less == 'more' else not number_to_use

    indices = [i for i, x in enumerate(bits_by_position) if x == number_to_use]  # save index if 1

    numbers_new = [numbers[i] for i in indices]
    bit_position += 1  # move to next bit

    # repeat
    while len(numbers_new) > 1:
        return get_numbers(numbers_new, bit_position, more_or_less)

    # end
    final_number = [bool(int(i)) for i in list(numbers_new[0])]
    return get_decimal(final_number)


oxy = get_numbers(numbers, 0, 'more')
co2 = get_numbers(numbers, 0, 'less')
print(oxy * co2)



