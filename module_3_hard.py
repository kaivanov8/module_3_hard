        # раз, два, три, четыре, пять... module_3_hard

data_structure = [
    [1,2,3],
    {'a':4, 'b':5},
    (6,{'cube':7,'drum':8}),
    "Hello",
    ((),[{(2,'Urban',('Urban2',35))}])]
t = 0

def calculate_structure_sum(a):
    global t
    if isinstance(a,int):
        t += a
    elif isinstance(a,str):
        t += len(a)
    elif isinstance(a,dict):
        for n,x in a.items():
            t =t + len(n) + x
    else:
        for i in a:
            calculate_structure_sum(i)
    return t

result = calculate_structure_sum(data_structure)
print(result)

