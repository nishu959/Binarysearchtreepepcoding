import sys

class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left
   
  

class pair():
  def __init__(self, node, state):
    self.state = state
    self.node = node

m = int(input())
n = list(map(str, input().split()))
a =int(input())
b = int(input())



def btreeform(n, s, root):
  
  root = btree(int(n[0]))
  
  
  p = pair(root,1)
  s.append(p)
  idx =0
  while(len(s)>0):
    top = s[-1]
    if(top.state == 1):
    
      idx+=1
      if(n[idx]!="n"):
        t = btree(int(n[idx])) 
        top.node.left = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.left = None
      
      top.state += 1
    
    
    elif(top.state == 2):
      idx+=1
      if(n[idx]!="n"):
        t = btree(int(n[idx]) ,None, None)
        top.node.right = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.right = None
      
      top.state += 1
     
    else:
      s.pop()


  return root
  
  
root = btreeform(n, [], None)

l = [] 

def ntrpath(root, ele):
  global l
  if root==None:
    return []
  if(root.data == ele):
    l= []
    l.append(ele)
    return l
  
  
  if(ele < root.data):
    l = ntrpath(root.left, ele)
    if(len(l)>0):
      l.append(root.data)
      return l
       
  if(ele > root.data):
    l = ntrpath(root.right, ele)
    if(len(l)>0):
      l.append(root.data) 
      return l    
   
  return []
  
  

def findlca(root, a, b):
  p = ntrpath(root, a)
  q = ntrpath(root, b)
  
  i = len(p) - 1
  j = len(q) - 1
  
  while(i>=0 and j>=0 and (p[i]==q[j])):
    i-=1
    j-=1
    
  i+=1
  j+=1
  
  return p[i]
    
     
    
print(findlca(root, a, b)) 

    
    