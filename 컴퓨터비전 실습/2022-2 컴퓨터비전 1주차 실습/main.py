#----------------------------------------------------------#

a = 10
b = 10.0
c = 'test'

print(a,b,c)
print(type(a), type(b), type(c))

#----------------------------------------------------------#

# 한줄 주석
'''여러줄 주석
여러줄 주석'''
"""여러줄
주석"""

#----------------------------------------------------------#

list0 = list() #list0 = []
list1 = [1,3,5,7]
list2 = [2.0,4.0,6.0]
list3 = ['test1', 'test2']

print(list0)
print(list1)
print(list2)
print(list3)

#----------------------------------------------------------#

list1 = [1,3,5,7,9]

print(list1[0], list1[4], list1[-1])
print(list1[1:3], list1[3:])

#----------------------------------------------------------#
list1 = [1,3,5,7,9]

list1.append(11)
print(list1)

list1.insert(0, -1)
print(list1)

#----------------------------------------------------------#

list2 = [3,6,9,2,5,8,1,4,7]
print(list2)

list2.sort()
print(list2)

list2.reverse()
print(list2)

#----------------------------------------------------------#

tuple1 = (1, )
dict = {'과자': 1500, '음료수':1000}

print(tuple1)
print(dict['과자'])

#----------------------------------------------------------#

print(10 / 3)
print(10 % 3)
print(10 // 3)
print(10 ** 3)

#----------------------------------------------------------#

print('int:%d, float:%f, string:%s' %(i, f, s))
print('float:{1}, int:{0}, string{2}'.format(i, f, s))
print('float:{ff}, int:{ii}, string:{ss}' .format(ii=i, ff=f, ss=s))
