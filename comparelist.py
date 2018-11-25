# Complete the miniMaxSum function below.
def mindiffmax(arr):

    #Getting the minimum value
    max_val = max(arr)
    max_i = arr.index(max_val)
    arr.pop(max_i)
    min_sum = sum(arr)

    #getting the maximum value
    arr.append(max_val)
    min_val = min(arr)
    min_i = arr.index(min_val)
    arr.pop(min_i)
    max_sum = sum(arr)

    print(min_sum,max_sum)

mindiffmax([7, 69, 2, 221, 8974])





# # num1 = [1,3,5]
# # num2 = [2,11,6]
# # a = 0
# # b = 0
# #
# # # for i,x in enumerate(num1):
# # #     print (x + num2[i])
# #
# # locate = [[1,4,5,6],[1,3,6,7],[5,7,9,2],[9,6,2,7]]
# #
# # print(locate[0][2])
# #
# # # for i in range(len(locate)):
# # #     for j in range(len(locate)):
# # #         print(locate[i][j])
# #
# # for col,row in enumerate(locate):
# #     val = locate[col][col]
# #     sum_ltr = sum_ltr + val
# #
# # print (sum_ltr)
# #
# # for row in locate:
# #     val = locate[row][rev_col]
# #     sum_rtl = sum_rtl + val
# #     rev_col -= 1
# #
# # print(sum_rtl)
#
# print (str(24))
#
# ff = 0.3333333333333333
#
# print ('%.2f'%ff)
#
# print ('#'.ljust(10))
#
# for val in range(6):
#         print(("#"*(val+1)).center(6," "))
#
# str = "this is string example....wow!!!"
# print str.rjust(50, '*')
# vv = [2,4,6,8,9,30]
#
# print (max(vv))
#
# new = vv.remove(30)
#
# print (new)
#
# arr = [396285104, 573261094, 759641832, 819230764, 364801279]
# max_val = max(arr)
# min_val = min(arr)
#
# max_i = arr.index(max_val)
# print(max_i)
# min_i = arr.index(min_val)
# print(min_i)
#
# arr.pop(max_i)
# min_sum = sum(arr)
# print(arr)
#
# arr.append(max_val)
# arr.pop(min_i)
# max_sum = sum(arr)
# print(arr)
#
# print(min_sum,max_sum)
