


# 1. Sum all items in a list
def exercise_1(lst):
    return sum(lst)

# 2. Multiply all items in a list
def exercise_2(lst):
    result = 1
    for x in lst:
        result *= x
    return result

# 3. Get the largest number from a list
def exercise_3(lst):
    return max(lst)

# 4. Get the smallest number from a list
def exercise_4(lst):
    return min(lst)

# 5. Count the number of strings with length >= 2 and same first/last char
def exercise_5(lst):
    return len([s for s in lst if len(s) >= 2 and s[0] == s[-1]])

# 6. Sort list of tuples by last element
def exercise_6(lst):
    return sorted(lst, key=lambda x: x[-1])

# 7. Remove duplicates from a list
def exercise_7(lst):
    return list(set(lst))

# 8. Check if list is empty
def exercise_8(lst):
    return len(lst) == 0

# 9. Clone or copy a list
def exercise_9(lst):
    return lst[:]

# 10. Words longer than n
def exercise_10(lst, n):
    return [w for w in lst if len(w) > n]

# 11. Check common member in two lists
def exercise_11(lst1, lst2):
    return any(x in lst1 for x in lst2)

# 12. Remove 0th, 4th, 5th elements
def exercise_12(lst):
    return [x for i, x in enumerate(lst) if i not in (0, 4, 5)]

# 13. Generate 3*4*6 3D array with *
def exercise_13():
    return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

# 14. Remove even numbers
def exercise_14(lst):
    return [x for x in lst if x % 2 != 0]

# 15. Shuffle a list
import random
def exercise_15(lst):
    random.shuffle(lst)
    return lst

# 16. First and last 5 square numbers between 1 and 30
def exercise_16():
    squares = [i**2 for i in range(1, 31)]
    return squares[:5] + squares[-5:]

# 17. Check if all numbers are prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def exercise_17(lst):
    return all(is_prime(x) for x in lst)

# 18. All permutations of a list
import itertools
def exercise_18(lst):
    return list(itertools.permutations(lst))

# 19. Difference between two lists
def exercise_19(lst1, lst2):
    return list(set(lst1) - set(lst2)) + list(set(lst2) - set(lst1))

# 20. Access index of a list
def exercise_20(lst):
    return list(enumerate(lst))

# 21. Convert list of characters to string
def exercise_21(lst):
    return ''.join(lst)

# 22. Find index of item in list
def exercise_22(lst, item):
    return lst.index(item)

# 23. Flatten a shallow list
def exercise_23(lst):
    return [i for sub in lst for i in sub]

# 24. Append list to second list
def exercise_24(lst1, lst2):
    return lst1 + lst2

# 25. Select random item from list
def exercise_25(lst):
    return random.choice(lst)

# 26. Check circularly identical lists
def exercise_26(lst1, lst2):
    return len(lst1) == len(lst2) and any(lst1 == lst2[i:] + lst2[:i] for i in range(len(lst2)))

# 27. Find second smallest number
def exercise_27(lst):
    return sorted(set(lst))[1]

# 28. Find second largest number
def exercise_28(lst):
    return sorted(set(lst))[-2]

# 29. Get unique values from list
def exercise_29(lst):
    return list(set(lst))

# 30. Frequency of elements in list
from collections import Counter
def exercise_30(lst):
    return Counter(lst)

# 31. Count elements within a range
def exercise_31(lst, min_val, max_val):
    return len([x for x in lst if min_val <= x <= max_val])

# 32. Check if list contains a sublist
def exercise_32(lst, sub):
    return any(lst[i:i+len(sub)] == sub for i in range(len(lst)-len(sub)+1))

# 33. Generate all sublists
def exercise_33(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i+1, len(lst)+1)]

# 34. Sieve of Eratosthenes up to n
def exercise_34(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# 35. Concatenate list with range 1..n
def exercise_35(lst, n):
    return [x+str(i) for i in range(1, n+1) for x in lst]

# 36. Get variable id
def exercise_36(var):
    return id(var)

# 37. Common items in two lists
def exercise_37(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 38. Swap n-th and (n+1)-th elements
def exercise_38(lst):
    lst = lst[:]
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst

# 39. Convert list of ints to single int
def exercise_39(lst):
    return int(''.join(map(str, lst)))

# 40. Split list based on first char
from collections import defaultdict
def exercise_40(lst):
    d = defaultdict(list)
    for word in lst:
        d[word[0]].append(word)
    return dict(d)

# 41. Create multiple lists
def exercise_41(*args):
    return [list(arg) for arg in args]

# 42. Missing and additional values between two lists
def exercise_42(lst1, lst2):
    return {"Missing": list(set(lst1)-set(lst2)), "Additional": list(set(lst2)-set(lst1))}

# 43. Split list into variables
def exercise_43(lst):
    return tuple(lst)

# 44. Groups of five consecutive numbers
def exercise_44(n):
    return [list(range(i, i+5)) for i in range(1, n+1, 5)]

# 45. Convert pair to sorted unique array
def exercise_45(a, b):
    return sorted(set([a, b]))

# 46. Select odd items from list
def exercise_46(lst):
    return lst[1::2]

# 47. Insert element before each element
def exercise_47(lst, elem):
    return [y for x in lst for y in (elem, x)]

# 48. Print nested lists line by line
def exercise_48(lst):
    return '\n'.join(str(x) for x in lst)

# 49. Convert two lists to list of dicts
def exercise_49(lst1, lst2):
    return [{"color_name": c, "color_code": v} for c, v in zip(lst1, lst2)]

# 50. Sort list of nested dictionaries
def exercise_50(lst, key):
    return sorted(lst, key=lambda x: x[key])
# 51. Split list every Nth element
def exercise_51(lst, n):
    return [lst[i::n] for i in range(n)]

# 52. Compute difference between two lists
def exercise_52(lst1, lst2):
    return {"Color1-Color2": list(set(lst1) - set(lst2)), "Color2-Color1": list(set(lst2) - set(lst1))}

# 53. Create a list with infinite elements (generator)
def exercise_53(start=0):
    while True:
        yield start
        start += 1

# 54. Concatenate elements of a list
def exercise_54(lst):
    return ''.join(map(str, lst))

# 55. Remove key-value pairs from list of dicts
def exercise_55(lst):
    return [dict() for _ in lst]

# 56. Convert string to list
def exercise_56(s):
    return list(s)

# 57. Check if all items in list equal to a given string
def exercise_57(lst, s):
    return all(x == s for x in lst)

# 58. Replace last element in list with another list
def exercise_58(lst1, lst2):
    return lst1[:-1] + lst2

# 59. Check if nth element exists
def exercise_59(lst, n):
    return n < len(lst)

# 60. Find tuple with smallest second index value
def exercise_60(lst):
    return min(lst, key=lambda x: x[1])

# 61. Create list of empty dicts
def exercise_61(n):
    return [{} for _ in range(n)]

# 62. Print list space-separated
def exercise_62(lst):
    return ' '.join(map(str, lst))

# 63. Insert string at beginning of each list item
def exercise_63(lst, prefix):
    return [f"{prefix}{x}" for x in lst]

# 64. Iterate over two lists simultaneously
def exercise_64(lst1, lst2):
    return list(zip(lst1, lst2))

# 65. Move all zeros to end
def exercise_65(lst):
    return [x for x in lst if x != 0] + [0]*lst.count(0)

# 66. Find sublist with highest sum
def exercise_66(lsts):
    return max(lsts, key=sum)

# 67. Values greater than specified number
def exercise_67(lst, n):
    return [x for x in lst if x > n]

# 68. Extend list without append
def exercise_68(lst1, lst2):
    return lst2 + lst1

# 69. Remove duplicates from list of lists
def exercise_69(lst):
    new = []
    for sub in lst:
        if sub not in new:
            new.append(sub)
    return new

# 70. Find items starting with specific char
def exercise_70(lst, ch):
    return [x for x in lst if x.startswith(ch)]

# 71. Check if all dicts in list are empty
def exercise_71(lst):
    return all(not d for d in lst)

# 72. Flatten nested list
def exercise_72(lst):
    out = []
    for i in lst:
        if isinstance(i, list):
            out.extend(i)
        else:
            out.append(i)
    return out

# 73. Remove consecutive duplicates
def exercise_73(lst):
    result = []
    for x in lst:
        if not result or result[-1] != x:
            result.append(x)
    return result

# 74. Pack consecutive duplicates
def exercise_74(lst):
    result = []
    for x in lst:
        if result and result[-1][0] == x:
            result[-1].append(x)
        else:
            result.append([x])
    return result

# 75. Run-length encoding
def exercise_75(lst):
    result = []
    i = 0
    while i < len(lst):
        count = 1
        while i+1 < len(lst) and lst[i] == lst[i+1]:
            i += 1
            count += 1
        result.append([count, lst[i]])
        i += 1
    return result

# 76. Modified run-length encoding
def exercise_76(lst):
    result = []
    i = 0
    while i < len(lst):
        count = 1
        while i+1 < len(lst) and lst[i] == lst[i+1]:
            i += 1
            count += 1
        if count > 1:
            result.append([count, lst[i]])
        else:
            result.append(lst[i])
        i += 1
    return result

# 77. Decode run-length
def exercise_77(lst):
    result = []
    for x in lst:
        if isinstance(x, list):
            result.extend([x[1]]*x[0])
        else:
            result.append(x)
    return result

# 78. Split list into two parts of given length
def exercise_78(lst, n):
    return lst[:n], lst[n:]

# 79. Remove kth element
def exercise_79(lst, k):
    return lst[:k] + lst[k+1:]

# 80. Insert element at position
def exercise_80(lst, k, val):
    return lst[:k] + [val] + lst[k:]

# 81. Extract n random elements
import random
def exercise_81(lst, n):
    return random.sample(lst, n)

# 82. Generate combinations of n elements
import itertools
def exercise_82(lst, n):
    return list(itertools.combinations(lst, n))

# 83. Round numbers and sum*len
def exercise_83(lst):
    rounded = [round(x) for x in lst]
    return sum(rounded) * len(lst)

# 84. Round, find min/max, multiply by 5, unique sorted
def exercise_84(lst):
    rounded = [round(x) for x in lst]
    return min(rounded), max(rounded), sorted(set([x*5 for x in rounded]))

# 85. Create multidimensional list with zeros
def exercise_85(m, n):
    return [[0]*n for _ in range(m)]

# 86. Create 3x3 grid
def exercise_86():
    return [[1,2,3] for _ in range(3)]

# 87. Sum columns of matrix
def exercise_87(matrix):
    return [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]

# 88. Sum primary diagonal
def exercise_88(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

# 89. Zip two lists of lists
def exercise_89(lst1, lst2):
    return [a+b for a,b in zip(lst1, lst2)]

# 90. Count lists in list of lists
def exercise_90(lst):
    return sum(isinstance(x, list) for x in lst)

# 91. List with max and min length
def exercise_91(lst):
    return max(lst, key=len), min(lst, key=len)

# 92. Check if nested list subset of another
def exercise_92(lst1, lst2):
    return all(x in lst1 for x in lst2)

# 93. Count sublists containing element
def exercise_93(lst, elem):
    return sum(elem in sub for sub in lst)

# 94. Count unique sublistss
def exercise_94(lst):
    from collections import Counter
    return Counter(tuple(x) for x in lst)

# 95. Sort each sublist
def exercise_95(lst):
    return [sorted(x) for x in lst]

# 96. Sort list of lists by length and value
def exercise_96(lst):
    return sorted(lst, key=lambda x: (len(x), x))

# 97. Remove sublists with element outside range
def exercise_97(lst, minv, maxv):
    return [x for x in lst if all(minv <= i <= maxv for i in x)]

# 98. Scramble strings in list
import random
def exercise_98(lst):
    return [''.join(random.sample(s, len(s))) for s in lst]

# 99. Max and min in heterogeneous list
def exercise_99(lst):
    nums = [x for x in lst if isinstance(x, (int, float))]
    return max(nums), min(nums)

# 100. Extract common index elements from multiple lists
def exercise_100(*lists):
    return [x for x in zip(*lists) if len(set(x)) == 1]
