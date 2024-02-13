import sys

sys.stdin.readline()

tup_list = []
tup_list = sys.stdin.readlines()

tuples_list = []
for m_tuple in tup_list:
    tup = m_tuple.split()
    tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

tuples_list = sorted(tuples_list)

while True:
    overlap = False
    for i in range(len(tuples_list) - 1):
        if tuples_list[i + 1][0] <= tuples_list[i][1]:  # Check for overlap
            merged_interval = (tuples_list[i][0], max(tuples_list[i][1], tuples_list[i + 1][1]))
            tuples_list[i] = merged_interval
            del tuples_list[i + 1]
            overlap = True
            break

    if not overlap:
        break

print(tuples_list)