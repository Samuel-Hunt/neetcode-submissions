class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #intialise two dictionaries
       count_s = {}
       count_t = {}
       
        #add char to the dictionary, if it is alrrady inside, increase the count by 1
       for char in s:
            count_s[char] = count_s.get(char, 0) + 1
       for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        #boolean operation will return true if they are equivelant, false otherwise
       return (count_s == count_t)
    
        
        