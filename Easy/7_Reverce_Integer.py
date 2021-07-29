#!/usr/bin/env python3

#7. Reverse Integer
#Easy
#
#5279
#
#7912
#
#Add to List
#
#Share
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# 
#
#Example 1:
#
#Input: x = 123
#Output: 321
#Example 2:
#
#Input: x = -123
#Output: -321
#Example 3:
#
#Input: x = 120
#Output: 21
#Example 4:
#
#Input: x = 0
#Output: 0
# 
#
#Constraints:
#
#-231 <= x <= 231 - 1


#========CODE===========

class Solution:
    def reverse(self, x: int):
        minx = -2**31
        maxx = 2**31 -1
        res = ""
        if x < 0:
            res = "-"
        res = int(res + (str(abs(x)) [::-1]))
        if res in range(minx, maxx):
            return res
        else:
            return 0

#Конечный результат может вылезти за пределы данные в условие
