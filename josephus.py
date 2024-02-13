"""
  File: employee.py
  Description:

  Student Name: Wei-Yu Chiang
  Student UT EID: wc22968

  Partner Name: Panav Ladha
  Partner UT EID: pl22793

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 10-11-23
  Date Last Modified: 10-11-23
"""

import sys

class Link():
    """Single linked list with data and reference to the following element"""

    def __init__(self, data):
        """Initialize Link with given data and reference to the following Link"""
        self.data = data
        self.next = None

    def get_data(self):
        """Returns data stored in Link"""
        return self.data

    def get_next(self):
        """Returns next linked list element"""
        return self.next


class CircularList():
    """Circular list class with insert, find, delete, and delete_after methods"""

    def __init__(self):
        """Initialize empty circular list with head pointing to None"""
        self.head = None

    def insert(self, data):
        """Insert new element with the given data into circular list"""
        new_link = Link(data)
        if not self.head:
            self.head = new_link
            new_link.next = self.head
        else:
            cur_link = self.head
            while cur_link.next != self.head:
                cur_link = cur_link.next
            cur_link.next = new_link
            new_link.next = self.head

    def find(self, data):
        """Find Link with given data in circular list"""
        cur_link = self.head
        while cur_link:
            if cur_link.data == data:
                return cur_link
            cur_link = cur_link.next
            if cur_link == self.head:
                break
        return None

    def delete(self, data):
        """Delete Link with given data from circular list"""
        if not self.head:
            return None

        cur_link = self.head
        prev = None

        while True:
            if cur_link.data == data:
                if self.head.next == self.head:
                    self.head = None
                else:
                    if cur_link == self.head:
                        self.head = cur_link.next
                    prev.next = cur_link.next
                return cur_link
            prev = cur_link
            cur_link = cur_link.next
            if cur_link == self.head:
                break

        return None

    def delete_after(self, start, steps):
        """Delete nth Link beginning from given Link"""
        cur_link = start
        prev = None
        for _ in range(steps - 1):
            prev = cur_link
            cur_link = cur_link.next
        if cur_link == self.head:
            self.head = cur_link.next
        prev.next = cur_link.next
        return cur_link.data, cur_link.next

    def __str__(self):
        """Return string representation of circular list"""
        c_list = []
        cur_link = self.head
        while cur_link:
            c_list.append(str(cur_link.data))
            cur_link = cur_link.next
            if cur_link == self.head:
                break
        return '[' + ', '.join(c_list) + ']'

def main():
    """Reads input, performs functions, and print the results"""
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    clist = CircularList()

    for i in range(1, num_soldiers + 1):
        clist.insert(i)

    elim_list = []
    cur_link = clist.find(start_count)
    for i in range(num_soldiers):
        data, next_link = clist.delete_after(cur_link, elim_num)
        elim_list.append(data)
        cur_link = next_link
    for elim in elim_list:
        print(elim)


if __name__ == "__main__":
    main()
