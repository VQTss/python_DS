# How the typle can be used to key for dictionary?
# yes, because tuple is immutable, and key for dictionary must be immutable and unique.
# The tuple is best used for dictionary keys because they are immutable and unique. Ensure the keys are unique and immutable.


# my_dict = {(1, 2): 'apple', (3, 4): 'banana'}
# my_dict[(1, 2)]


my_typle = ('key1', 'key2')
my_list = [1, 2]
my_dict = dict(zip(my_typle, my_list))
print(my_dict)


# Not every tuple is hashable. Only tuples that contain immutable elements are hashable.
x = (1, 2, [3, 4])
print(type(x))
# print(hash(x)) # TypeError: unhashable type: 'list'

