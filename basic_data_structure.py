

def main():
    print("=========== Tuples ===========")
    # Tuples are immutable
    # Tuples are faster than lists
    # Tuples are used when you know the data will not change
    # Tuples are used for heterogenous data
    # Tuples are used for data that will not be changed
    # Tuples are used for data that will be accessed frequently
    # Tuples are used for data that will be used as dictionary keys
    # Tuples are used for returning multiple values from a function
    # Tuples are used for passing multiple values to a function
    # Tuples are used for string formatting
    my_tuple = (1,2,3,3,3,6,7,8,9,10)
    #my_tuple[1] = 4 : Error , tuples are immutable    
    print("my_tuple: ", my_tuple)
    # Now, try to add element to the tuple
    print("Old type id: ", id(my_tuple))
    my_tuple += (0,0)
    print("New type id: ", id(my_tuple))
    # cannot append element to tuple because it is immutable, and it will create a new tuple. 
    # Can see that the id of the tuple is changed

    print("=========== Lists ===========")
    # Lists are mutable
    # Lists are slower than tuples
    # Lists are used when you know the data will change
    # Lists are used for homogenous data
    # Lists are used for data that will be changed
    # Lists are used for data that will be accessed infrequently
    # Lists are used for data that will not be used as dictionary keys
    # Lists are used for returning multiple values from a function
    # Lists are used for passing multiple values to a function
    # Lists are used for string formatting
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print("My origin list: ", my_list)
    print("ID of my_list before: ", id(my_list))
    print("My list with 3 appended: ", my_list+ [3])
    print("ID of my_list after: ", id(my_list))
    print("My list with 3 preappended: ", [3] + my_list)
    
    print("=========== Sets ===========")
    # Sets are mutable
    # Sets are unordered
    # Sets are unindexed
    # Sets are unique
    # Sets are used for membership testing
    # Sets are used for eliminating duplicate entries
    # Sets are used for mathematical operations such as intersection, union, difference, and symmetric difference
    my_set = set(my_tuple)
    print("My old set: ", my_set)
    print("My old set ID: ", id(my_set))
    # Add element to the set
    my_set.add(11)
    # Add multiple elements to the set
    my_set.update([5,6,7])
    # Remove one
    my_set.remove(11)
    print("My new set: ", my_set)
    print("My new set ID: ", id(my_set))
    
    print("=========== Dictionaries ===========")
    # Dictionaries are mutable
    # Dictionaries are unordered
    # Dictionaries are indexed
    # Dictionaries are unique
    # Dictionaries are used for mapping keys to values
    # Dictionaries are used for eliminating duplicate entries
    # Dictionaries are used for mathematical operations such as intersection, union, difference, and symmetric difference
    my_dict = {'a':1, 'b':2, 'c':3}
    print("My old dict: ", my_dict)
    print("My old dict ID: ", id(my_dict))
    print("Value of key 'a': ", my_dict['a'])
    
    # Add new key-value pair
    my_dict['d'] = 4
    print("My new dict: ", my_dict)
    print("My new dict ID: ", id(my_dict))    
    
if __name__ == '__main__':
    main()


