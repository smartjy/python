# 어벤져스의 멤버의 순위를 매기세요
# 변수의 순서를 변경 합니다.
# 5명 까지 순위를 정하세요
# shuffle, sample 함수를 이용합니다.

from random import *

heroes = ['Ironman', 'Thor', 'AntMan', 'Hulk', 'Wanda', 'Vision', 'Widow', 'Captain']

shuffle(heroes)
# print(heroes)

ranking = sample(heroes, 5)
# print(ranking)

# for ranker in ranking:
#     print(ranker)

for i, ranker in enumerate(ranking, start=1):
    print(i, ranker)
