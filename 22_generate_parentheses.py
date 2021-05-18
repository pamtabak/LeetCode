class Solution:
    def is_invalid (self, my_string: str, n: int) -> bool:
        counter = 0
        for my_char in my_string:
            if (my_char == "("):
                counter += 1
            else:
                counter -= 1
            if (counter < 0):
                return True
        if (n - len(my_string) < counter):
            return True
        return counter < 0

    def backtrack (self, n):
        current_list = ["("]
        for i in range (0, n - 1):
            new_list = []
            for element in current_list:
                open_element = element + "("
                if (not self.is_invalid(open_element, n)):
                    new_list.append(open_element)
                close_element = element + ")"
                if (not self.is_invalid(close_element, n)):
                    new_list.append(close_element)
            current_list = new_list

        return current_list
    
    def generateParenthesis(self, n: int) -> List[str]:
        #brute force idea: 2**(n*2), generate all options and check which ones consists of well-formed parentheses. Since our string will have n*2 chars and each char is either ( or ), there is 2 possibilities for each char. So 2**(n*2)
        #backtrack: improve brute force by stoping the algorithm as the string is invalid before generating the whole string
        return self.backtrack(n*2)
        
        