"""
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.


입출력 예
array	commands	return
[1, 5, 2, 6, 3, 7, 4]	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	[5, 6, 3]
입출력 예 설명
[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.


아이디어: 처음에 입력을 받은 array와 commands에 대하여
command의 첫번째와 두번째 인자를 받아 start와 end에 넣어놓고
슬라이싱을 통해 새로운 리스트에 넣어놓자 그 다음 다시 sorted를 하여 정렬하고 그 곳에 대한 index를 넣어주면
결과 answer에 그 데이터들이 쌓이며 return 하면 된다.
"""


def solution(array, commands):
    #결과를 나타낼 리스트
    answer = []

    ##초기값 (사실 없어도 된다)
    start = 0
    end = 1

    #리스트 안에 리스트이므로 이런식으로 각 인자를 받아와서 넣어준 뒤에 슬라이싱, 정렬한다.
    #마지막으로 해당하는 세번째 수에 대한 것을 array의 index에 넣어주면 된다.
    for i, command in enumerate(commands):
        start = command[0]
        end = command[1]
        index = command[2] - 1
        new_array = array[start - 1:end]
        sorted_array = sorted(new_array)
        print(sorted_array)
        answer.append(sorted_array[index])

    return answer
