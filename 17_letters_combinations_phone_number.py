class Solution:
    numbers_map = { '2' : ["a" , "b", "c"], '3' : ["d", "e", "f"], '4' : ["g", "h", "i"], '5' : ["j", "k", "l"], '6' : ["m", "n", "o"], '7': ["p", "q", "r", "s"], '8': ["t", "u", "v"], '9': ["w", "x", "y", "z"] }
    
    def letterCombinations(self, digits: str) -> List[str]:
        current_list = []
        new_list = []
        if (not digits):
            return current_list
        #initializing list
        for letter in self.numbers_map[digits[0]]:
            current_list.append(letter)
        print(current_list)
        
        count = 0
        for digit in digits:
            count += 1
            if (count == 1):
                continue #skiping the first digit
            for combination in current_list:
                for letter in self.numbers_map[digit]:
                    new_combination = combination + letter
                    new_list.append(new_combination)
                    print(new_list)
            current_list = new_list
            new_list = []
        return current_list
            