"""
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys


def merge_tuples (tuples_list):

    tuples_list = sorted(tuples_list)

    while True:
        overlap = False
        for i in range(len(tuples_list) - 1):
            if tuples_list[i + 1][0] <= tuples_list[i][1]:
                merged_interval = (tuples_list[i][0], max(tuples_list[i][1], tuples_list[i + 1][1]))
                tuples_list[i] = merged_interval
                del tuples_list[i + 1]
                overlap = True
                break

        if not overlap:
            break
    return (tuples_list)



def sort_by_interval_size (tuples_list):
 
    sorted_list = []  

    for tup in tuples_list:
        size = tup[1] - tup[0]
        sorted_list.append((size, tup))

    sorted_list.sort()

    final_sorted_list = []
    for size, tup in sorted_list:
        final_sorted_list.append(tup)

    return final_sorted_list


def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
