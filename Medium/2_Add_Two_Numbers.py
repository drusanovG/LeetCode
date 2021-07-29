#!/usr/bin/env python3

#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# 
#
#Example 1:
#
#
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#Example 2:
#
#Input: l1 = [0], l2 = [0]
#Output: [0]
#Example 3:
#
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
# 
#
#Constraints:
#
#The number of nodes in each linked list is in the range [1, 100].
#0 <= Node.val <= 9
#It is guaranteed that the list represents a number that does not have leading zeros.


#========CODE===========

fn = ""
l1 = [2, 4, 3]
l2 = [8, 0, 5]
l1.reverse()
l2.reverse()
for el in l1:
    fn = fn + str(el)
res = int(fn)
fn = ""
for el in l2:
    fn = fn + str(el)
res = int(str(res + int(fn)))
#res = int(str(res) [::-1])
print(res)
if res % 10 == 0:
	print("ekw")
print("kekw")
a = 0 % 10
print(a)
#while true:
#	if res % 10 = 0:
#		res = res / 10
#		i = 0
#	else:
#		break
#res = int(str(res) [::-1])
#print([int(d) for d in str(res)])
#
##Конечный результат может вылезти за пределы данные в условие
