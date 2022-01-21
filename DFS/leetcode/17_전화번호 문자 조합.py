def letterCombinations(input: str):
    def dfs(deep, stack):
        if len(stack) == len(input):
            result.append(stack)
            return


        for j in dic[input[deep]]:
            dfs(deep+1,stack+j)
        return


    if not input:
        return []

    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    dfs(0, "")

    return result

print(letterCombinations("236"))