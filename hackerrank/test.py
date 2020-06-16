n = int(input())
std = {}

for i in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    std[name] = scores

query_name = input()
query_scores = list(std[query_name])
# print(list(query_scores))
print("{0:.2f}".format(sum(query_scores) / (len(query_scores))))

