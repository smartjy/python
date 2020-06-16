M = input();m = input().split()
N = input();n = input().split()

print("\n".join(sorted(list(set(m) ^ set(n)),key=int)))


# a = input()
# lis = a.split()
# print(lis)
#
# newlis = list(map(int, lis))
# print(newlis)

# myset = {1,2}
# myset = set()
# myset = set(['a', 'b'])
# print(myset)
#
# myset.add('c')
# print(myset)
# myset.add('a')
# myset.add((5,4))
# print(myset)
#
# myset.update([1,2,3,4])
# print(myset)
# myset.update({1,7,8})
# print(myset)
# myset.update({1, 6}, [5, 13])
# print(myset)
#
# myset.discard(10)
# print(myset)
# myset.remove(13)
# print(myset)
#
# a = {2, 4, 5, 9}
# b = {2, 4, 11, 12}
# a.union(b)
# b.union(a)
# print(b)