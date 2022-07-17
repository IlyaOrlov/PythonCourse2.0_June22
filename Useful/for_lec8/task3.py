class AllInts:

    # __contains__ определяет, как вести себя,
    # если к объекту применяют оператор "in"
    def __contains__(self, item):
        if isinstance(item, int):
            return True

ints = AllInts()
if '127' in ints:
    print('Yes!')
