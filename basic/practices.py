# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

# 조건1 : 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수
# 조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# 출력문 예제
# [O] 1번 손님 (소요시간: 15분)
# 총 탑승 승객: 2분
from random import randrange

customers = 0 # 승객 수를 구하기 위한 변수, 50명의 승객이니 1부터 50까지 반복

for cst in range(1,51):     # 승객 50명 출력
    # print(cst)
    time = randrange(5, 51) # 5 ~ 50분 사이 난수 구하기
    # print(time)
    if 5 <= time <= 15:     # 5 ~ 15분 사이 승객 매칭
        print('[O] {}번째 손님 (소요시간 : {} 분)'.format(cst, time)) # [O] 매칭이 되었고 승객 순서, 5~15분 사이 승객 시간
        customers = customers +1
    else:
        print('[ ] {}번째 손님 (소요시간 : {} 분)'.format(cst, time))  # [ ] 매칭 실패 승객 순서, 5~15분 사이 넘어감

print('\n탑승 승객 : {}명 입니다.'.format(customers))


# from random import randint, randrange
#
# cnt = 0
#
# for i in range(cnt+1, 51):
#     time = randrange(5, 51)
#     # print(time)
#     if 5 <= time <= 15:
#         print('[0] Passenger: {}, Time: {} mins'.format(i, time))
#         cnt = cnt + 1
#     else:
#         print('[ ] Passenger: {}, Time: {} mins'.format(i, time))
#
# print('\nTotal Passenger = {}'.format(cnt))
#

#
# # from random import *
# # import random
# #
# # cnt = 0
# #
# # for i in range(1,51):
# #     # print(i)
# #     time = randrange(5, 51)
# #     # print(time)
# #     if 5 <= time <= 15:
# #         print("[O] People: {} , Time: {}".format(i, time))
# #         cnt =+ 1
# #     else:
# #         print("[ ] People: {} , Time: {}".format(i, time))
# #
# # print("Total: {} ".format(cnt))
# from random import randint, randrange
#
# cnt = 0
#
# for i in range(cnt+1, 51):
#     time = randrange(5, 51)
#     # print(time)
#     if 5 <= time <= 15:
#         print('[0] Passenger: {}, Time: {} mins'.format(i, time))
#         cnt = cnt + 1
#     else:
#         print('[ ] Passenger: {}, Time: {} mins'.format(i, time))
#
# print('\nTotal Passenger = {}'.format(cnt))
#

#
# # from random import *
# # import random
# #
# # cnt = 0
# #
# # for i in range(1,51):
# #     # print(i)
# #     time = randrange(5, 51)
# #     # print(time)
# #     if 5 <= time <= 15:
# #         print("[O] People: {} , Time: {}".format(i, time))
# #         cnt =+ 1
# #     else:
# #         print("[ ] People: {} , Time: {}".format(i, time))
# #
# # print("Total: {} ".format(cnt))