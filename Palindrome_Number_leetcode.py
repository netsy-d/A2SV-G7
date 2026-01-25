class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num=0
        reminder=0
        num = x
        while num > 0:
            reminder = num%10
            reversed_num = (reversed_num*10) + reminder
            num = num//10
        return reversed_num == x
