from collections import OrderedDict


#ord_dict = OrderedDict().fromkeys([1, 2, 3, 4])
ord_dict = OrderedDict([('a', 'aa'), ('b', 'bb')])
print("Original Dictionary")
print(ord_dict)

# Pop the key from last
# ord_dict.popitem()
# print("\nAfter Deleting Last item :")
# print(ord_dict)

# Pop the key from beginning
# ord_dict.popitem(last=False)
# print("\nAfter Deleting Key from Beginning :")
# print(ord_dict)


ord_dict.update({'c': 'cc'})
ord_dict.move_to_end()
print(ord_dict)
