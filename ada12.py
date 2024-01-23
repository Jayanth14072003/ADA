def findinoutdegree(adjlist,n):
 _in = [0]*n
 out = [0]*n
 for i in range(0,len(adjlist)):
  list =adjlist[i]
  out[i] = len(list)
  for j in range(0,len(list)):
   _in[list[j]]+=1
 print("vertex\tin\tout")
 for k in range(0,n):
  print(str(k) + "\t" +str(_in[k])+ "\t" + str(out[k]))
if __name__=="__main__":
 adjlist=[]
 adjlist.append([1,2])
 adjlist.append([3])
 adjlist.append([0,5,6])
 adjlist.append([1,4])
 adjlist.append([2,3])
 adjlist.append([4,6])
 adjlist.append([5])
 n = len(adjlist)
 findinoutdegree(adjlist,n)
