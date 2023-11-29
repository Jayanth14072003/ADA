from math import*
import sys
x={ }
n = 4
def place(k,i):
 if(i in x.values()):
  return False
 j=1
 while j<k:
  a=x[j]
  if abs(a-i)== abs(j-k):
   return False
  j+=1
 return True
def clear_future_blocks(k):
 for i in range(k,n+1):
  x[i]=None
def Nqueens(k):
 for i in range(1,n+1):
  clear_future_blocks(k)
  if place(k,i):
   x[k]=i
   if k==n:
    for j in x:
     print(x[j])
     print(" ")
   else:
    Nqueens(k+1)


#_______________driver code_______________
Nqueens(1) 
