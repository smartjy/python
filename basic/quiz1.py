# 표준 체중을 구하는 프로그램
# 표준 체중 : 각 개인의 키에 적당한 체중
# 성별에 따른 공식
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21
# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#   함수명: std_weight
#   전달값: 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시
# 출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.
##############################################################################3
# def std_weight(height, gender):
#     if gender == 'm':
#         weight = height * height * 22
#         gender = '남자'
#     else:
#         weight = height * height * 21
#         gender = '여자'
#     print('{}, 키 {}cm, 표준 체중 {}kg'.format(gender, height, weight))
#
# weight = std_weight(180 / 100, 'm')

##############################################################################3
# 1회 작성해야하는 보고서가 있다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 한다.
# ? 주차 주간보고
# 부서:
# 이름:
# 업무 오약
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건 : 파일명은 '1주차.txt', '2주차.txt' ...와 같이 만듭니다.
# i = 1
# report_file = open(i + '주차 주간보고', 'wb')
for i in range(1, 11):
    with open(str(i) + '주차 주간보고', 'w', encoding='utf8') as report_file:
        report_file.write('부서: \n')
        report_file.write('이름: \n')
        report_file.write('업무요약: \n')