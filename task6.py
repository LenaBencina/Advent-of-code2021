from collections import Counter

with open('Input/input6ex.txt') as f:
    input_tmp = f.read().split(',')

initial_states = list(map(int, input_tmp))
new_states = initial_states.copy()

counter_states = Counter(new_states)
for i in range(1, 9):
    if i not in counter_states:
        counter_states[i] = 0

for day in range(18):
    # print(day)
    states, counts = list(counter_states.keys()), list(counter_states.values())
    count_zeros = states.count(0)
    states = list(map(lambda x: x - 1 if (x - 1) >= 0 else 6, states))

    print(states)



    # count_new = new_states.count(0)
    # new_states = list(map(lambda x: x - 1 if (x - 1) >= 0 else 6, new_states))
    # new_states = new_states + [8] * count_new
    print

# result = len(new_states)

