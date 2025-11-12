# оператор * args - arguments
def Pechat(*args):
    print(args)

Pechat(56, 4, )
######
def sum2(*args):
    total = 0
    for i in args:
        total+=i
    print(total)

sum2(5,7,5,6)
############ **kwargs - keyword arguments - dict {key:value}
def show(**kwargs):
    for umar,bilal in kwargs.items():
        print(f"{umar}:{bilal}")
show(name='Бека', age=21, city='Bishkek', sport='footboll')   
# №№№№№№ 
def pets(owner, **kwargs):
    print(f"Владелец: {owner}")
    for k,v in kwargs.items():
        print(k,v)
pets('Umar', dog='Bobik', cat='felix')

# №№№№№№№
def demo(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
demo(34,45,56,67, name='gena', prof='alkash')
########
class Student:
    def __init__(self,name, **info):
        self.name = name
        self.info = info

s = Student('Nurai', age=18, course='Python', city='Manas')
print(s.name, s.info)



my_str = "frg5gth57ubdfh67rgtg567"
import re 
numbers = re.findall('[0-9]+', my_str)
nums = []
for i in numbers:
    nums.append(int(i))
print(nums) 



