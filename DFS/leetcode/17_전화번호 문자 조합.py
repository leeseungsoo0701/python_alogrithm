def dfs_phone_num(digits:str )->list[str]:
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    if digits == "":
        return []


    numbers = list(dic[digits[0]])   #[a,b,c]

    for digit in digits[1:]:


input = "23"
path = ""
dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


dfs_phone_num(input,path)