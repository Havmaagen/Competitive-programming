class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        vowels = set("aeiouAEIOU")
        
        has_vowel, has_consonant = False, False
        for char in word:
            if char.isalpha():
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not char.isdigit():
                return False
        
        answer = (len(word) >= 3) and has_vowel and has_consonant
        
        return answer