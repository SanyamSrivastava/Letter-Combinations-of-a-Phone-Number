def letterCombinations(digits):
    #Initially storing the combination of letters ; In the list the index will represent the mapped phone number  
    #E.g. index 3 -> 'def' 
    diginum = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    ans = []

    #Operative Recursive Function  
    def recurCombi(digits,res,diginum,ans):
        if digits == '':
            ans.append(res)
            return
        for i in (diginum[int(digits[0])]):
            recurCombi(digits[1:], res + i[0], diginum, ans)
                
    if digits == "":
        return []
    recurCombi(digits,'',diginum,ans)
    return ans

chars = input()
print(letterCombinations(chars))