# d={}
# for i in range(int(input())):
# 	line=input().split()
# 	d[line[0]]=sum(map(float,line[1:]))/3
#
# print('%.2f' % d[input()])

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        scores = sum(scores)/3
        student_marks[name] = scores
    query_name = input()

    print('%.2f' % student_marks[query_name])


