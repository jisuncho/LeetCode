class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        
        if not digits:
            return []
        
        answer = ['']
        for digit in [int(x) for x in digits]:
            letters = dial[digit]
            new_answer = []
            for string in answer:
                for letter in letters:
                    new_answer.append(string + letter)
            answer = new_answer
        
        return answer