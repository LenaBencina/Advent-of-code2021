with open('Input/input1.txt') as f:
    measurements_tmp = f.read().splitlines()

measurements = [int(m) for m in measurements_tmp]

# part 1
is_diff_positive = [mj - mi > 0 for mi, mj in zip(measurements, measurements[1:])]
is_diff_positive2 = [measurements[i+1] - measurements[i] > 0 for i in range(len(measurements) - 1)]
print(sum(is_diff_positive))
print(sum(is_diff_positive2))

# part 2
is_sum_diff_positive = [(mj+mk+ml) - (mi+mj+mk) > 0 for mi, mj, mk, ml in
                        zip(measurements, measurements[1:], measurements[2:], measurements[3:])]

m = measurements
is_sum_diff_positive2 = [(m[i+1]+m[i+2]+m[i+3]) - (m[i]+m[i+1]+m[i+2]) > 0 for i in range(len(m) - 3)]

print(sum(is_sum_diff_positive))
print(sum(is_sum_diff_positive2))

