class _Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def change(node1, node2):
    bid = node1.data
    node1.data = node2.data
    node2.data = bid
    del bid


class SList:
    def __init__(self):
        self.__head = None
    
    def __str__(self):
        sl = "List : ["
        tmp = self.__head
        while tmp is not None:
            sl += str(tmp.data)
            if tmp.next is not None:
                sl += ", "
            tmp = tmp.next
        return sl + ']'

    def __len__(self):
        size = 0
        tmp = self.__head
        while tmp is not None:
            tmp = tmp.next
            size += 1
        return size

    @property
    def first(self):
        try:
            return self.__head.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    @property
    def last(self):
        try:
            tmp = self.__head
            while tmp.next is not None:
                tmp = tmp.next
            return tmp.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')
    
    def empty(self):
        return self.__head is None

    def clear(self):
        while not self.empty():
            ptr = self.__head
            self.__head = self.__head.next
            del ptr

    def append(self, data):
        node = _Node(data)
        if self.empty():
            self.__head = node
        else:
            if data < self.__head.data:
                node.next = self.__head
                self.__head = node
            elif data == self.__head.data:
                node.next = self.__head.next
                self.__head.next = node
            else:
                tmp = self.__head
                cur = None
                while tmp.next is not None and data >= tmp.data:
                    cur = tmp
                    tmp = tmp.next
                if data < tmp.data:
                    cur.next = node
                    node.next = tmp
                else:
                    node.next = tmp.next
                    tmp.next = node
                del tmp, cur

    def remove(self, pos=0):
        try:
            tmp = self.__head
            count = 0
            if pos == 0:
                ptr = self.__head
                data = self.__head.data
                self.__head = self.__head.next
                del ptr
                return data
            elif pos == -1:
                while tmp.next is not None:
                    cur = tmp
                    tmp = tmp.next
                data = tmp.data
                cur.next = None
                del tmp
                return data
            while count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            data = tmp.data
            cur.next = tmp.next
            del tmp
            return data
        except Exception as ex:
            print("Error, %s" %ex)

    def delete(self, data):
        try:
            while self.__head.data == data:
                ptr = self.__head
                self.__head = self.__head.next
                del ptr
            cur = self.__head
            tmp = cur.next
            while tmp is not None:
                if tmp.data == data:
                    ptr = tmp
                    tmp = tmp.next
                    cur.next = tmp
                    del ptr
                else:
                    cur = tmp
                    tmp = tmp.next
        except Exception as ex:
            print("Error, %s" %ex)

    def find(self, data):
        count = 0
        tmp = self.__head
        while tmp is not None:
            if tmp.data == data:
                count += 1
            tmp = tmp.next
        return count

    @classmethod
    def merge(cls, sl1, sl2):
        try:
            lst = SList()
            tmp1 = sl1.__head
            tmp2 = sl2.__head
            while tmp1 is not None:
                lst.append(tmp1.data)
                tmp1 = tmp1.next
            while tmp2 is not None:
                lst.append(tmp2.data)
                tmp2 = tmp2.next
            del tmp1, tmp2
            return lst
        except Exception as ex:
            print("Error, %s" %ex)

    @classmethod
    def swap(cls, sl1, sl2):
        bid = SList()
        while not sl1.empty():
            bid.append(sl1.remove())
        while not sl2.empty():
            sl1.append(sl2.remove())
        while not bid.empty():
            sl2.append(bid.remove())
        del bid