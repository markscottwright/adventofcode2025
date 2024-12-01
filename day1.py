from collections import Counter

test_input = """\
3   4
4   3
2   5
1   3
3   9
3   3"""


def parse_input(input):
    distances1 = []
    distances2 = []
    for l in input.splitlines():
        d1, d2 = l.split()
        distances1.append(int(d1))
        distances2.append(int(d2))

    distances1.sort()
    distances2.sort()
    return distances1, distances2


test_location_ids_1, test_location_ids_2 = parse_input(test_input)
test_location_ids_2_counts = Counter(test_location_ids_2)
assert 11 == sum(abs(d1 - d2) for d1, d2 in zip(test_location_ids_1, test_location_ids_2))
assert 31 == sum(d1 * test_location_ids_2_counts[d1] for d1 in test_location_ids_1)

with open("day1.dat") as f:
    location_ids_1, location_ids_2 = parse_input(f.read())
location_ids_2_counts = Counter(location_ids_2)
print("day 1 part 1: ", sum(abs(d1 - d2) for d1, d2 in zip(location_ids_1, location_ids_2)))
print("day 1 part 2: ", sum(d1 * location_ids_2_counts[d1] for d1 in location_ids_1))
