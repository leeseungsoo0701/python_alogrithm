"""
입력:
2
홍길동 95
이순신 77
"""
# 입력 받을 튜플을 수
N = int(input())

# 입력 받은 데이터를 넣어줄 리스트
result = []

for i in range(N):
    # map을 활용한 student,grade 입력 받기
    student_name, grade = map(str, input().split())

    # 튜플 형태로 리스트에 append 해주기
    result.append((student_name, grade))

# lambda를 활용하여 result를 result의 [1], 즉 grade 순으로 정렬한다.
result = sorted(result, key=lambda sorted_result: sorted_result[1])

for name in result:
    print(name[0], end=' ')
