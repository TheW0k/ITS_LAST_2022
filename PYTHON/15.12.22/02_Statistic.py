def my_range(values):
    _min , _max = None, None
 
    for value in values:
        if _min == None or value < _min:
            _min = value
            
        if _max == None or value > _max:
            _max = value                     
    return _min , _max

def average(num):
    sum_num = 0
    for i in num:
        sum_num += i       
    return sum_num / len(num)

def over_avarage(values):
    for value in values:
        if value > average(values):
            print(value)

values = [9,7,6,3,5,5,8]
print(my_range(values))
print(average(values))
print(over_avarage(values))