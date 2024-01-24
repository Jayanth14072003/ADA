def min_edge(edge,v,vt):
    min=999
    for i in range (len(edge)):
        x=edge[i][0]
        y=edge[i][1]
        w=edge[i][2]

        if(x in v and y in vt)or(x in vt and y in v):
            if w<min:
                min=w
                pos=i
    return pos

def prims(edge,v):
    vt=[]
    et=[]
    vert=v.pop(0)
    vt.append(vert)
    n=len(v)
    for i in range(n):
        pos=min_edge(edge,v,vt)
        x=edge[pos][0]
        y=edge[pos][1]
        b=edge[pos]
        del edge[pos]
        et.append(b)
        if x in vt:
            vt.append(y)
            v.remove(y)
        else:
            vt.append(x)
            v.remove(x)
    return et

edge=[['a','b',5],['b','d',6],['c','d',4],['a','c',7],['a','e',2],
['b','e',3],['d','e',5],['c','e',4]]
vert=['a','b','c','d','e']
st_edge=[]
st_edge=prims(edge,vert)
print(st_edge)
