import os
def scho(dam,nam):
    print("Your subjects-")
    mp = os.path.abspath('../')
    path = mp+"/sub/"+dam+"/"+nam+"/subs.txt"
    lines = tuple(open(path).read().split('\n'))
    ran = len(lines)
    for x in range(1,ran):
        y=str(x)
        x=x-1
        x=str(lines[x])
        print(y+". "+x)
        
    mans = input("Select subject (number): ")
    mans = int(mans)
    mans = mans-1
    answer = lines[mans]
    answer = str(answer)

    return answer

def sadd(dam,nam):
    mp = os.path.abspath('../')
    path = mp+"/sub/"+dam+"/"+nam+"/subs.txt"
    lines = tuple(open(path).read().split('\n'))
    ran = len(lines)
    act = []
    for x in range(1,ran):
        y=str(x)
        x=x-1
        x=str(lines[x])
        act.append(x)
    return act
