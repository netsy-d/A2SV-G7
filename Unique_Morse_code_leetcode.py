class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        
        transformations = set()
        
      
        for word in words:
            
            morse_code = ''
            for char in word:
                
                index = ord(char) - ord('a')
                morse_code += morse[index]
            
           
            transformations.add(morse_code)
        
        
        return len(transformations)
