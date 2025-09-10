#BÀI 1
def exercise1():
    print("\n=== BÀI 1: Dictionary Operations ===")

    # a) Convert two lists into a dictionary
    keys = ['id', 'history', 'price']
    values = [4, 'sample', 73]
    dict_from_lists = dict(zip(keys, values))
    print("Dictionary from two lists:", dict_from_lists)

    # b) Merge two Python dictionaries into one
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)

    # c) Print the value of key 'history'
    my_dict = {'id': 4, 'history': 'sample', 'price': 73}
    print("Value of 'history':", my_dict['history'])

    # d) Initialize dictionary with default values
    keys = ['a', 'b', 'c']
    dict_with_defaults = dict.fromkeys(keys, 0)
    print("Initialized with defaults:", dict_with_defaults)

    # e) Create dictionary by extracting keys
    source_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    new_dict = {k: source_dict[k] for k in ['a', 'c']}
    print("Extracted dictionary:", new_dict)

    # f) Delete list of keys
    for k in ['b', 'd']:
        source_dict.pop(k, None)
    print("After deleting keys:", source_dict)

    # g) Check if a value exists
    d = {'x': 10, 'y': 20, 'z': 30}
    print("Does 20 exist in dict?", 20 in d.values())

    # h) Rename key
    d = {'name': 'Alice', 'age': 25}
    d['full_name'] = d.pop('name')
    print("After renaming key:", d)

    # i) Get key with min value
    d = {'a': 4, 'b': 18, 'c': 73}
    min_key = min(d, key=d.get)
    print("Key with minimum value:", min_key)

    # j) Change value in nested dict
    nested_dict = {
        'emp1': {'name': 'John', 'age': 25},
        'emp2': {'name': 'Doe', 'age': 30}
    }
    nested_dict['emp1']['age'] = 26
    print("Updated nested dictionary:", nested_dict)


# BÀI 2 
def exercise2():
    print("\n=== BÀI 2: Character Count and Positions ===")

    def stats_text(text):
        stats = {}
        for pos, ch in enumerate(text):
            if ch not in stats:
                stats[ch] = {'count': 1, 'positions': [pos]}
            else:
                stats[ch]['count'] += 1
                stats[ch]['positions'].append(pos)

        for key in sorted(stats.keys()):
            print(f"Character '{key}' appears {stats[key]['count']} times, at {stats[key]['positions']}")

    paragraph = "hello world"
    stats_text(paragraph)


#BÀI 3

def exercise3():
    print("\n=== BÀI 3: Prime Dictionary ===")

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def prime_dict(N):
        primes = [x for x in range(2, N) if is_prime(x)]
        d = {i+1: primes[:i+1] for i in range(len(primes))}
        return d

    N = 20
    print(prime_dict(N))
if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()