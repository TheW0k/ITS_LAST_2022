import random
  
def count_cypher_in_random_numbers(n_throw, start, end, num):
    
    count = 0
    random.seed(0)
    
    for _ in range(n_throw):
        
        n = random.randint(start,end)
        
        for char in str(num):
            count +=1
    return num

print(count_cypher_in_random_numbers(100,1,100,3))