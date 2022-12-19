def add_dots(s1):
    result = ""
    
    for i in range(len(s1)):
        if i == len(s1)-1:
            result += s1[i]
        else:
            result += s1[i] + "."
    return result
    
def remove_dots(s1):
    result = ""

    for i in range(len(s1)):
        if(i % 2 == 1):
            result = s1[i]
            
    return(result)

add_dots("test")
remove_dots("t.e.st")