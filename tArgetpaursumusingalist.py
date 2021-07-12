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



h = []

def targetpair(root, ele):
  global h
  if(root == None):
    return 
    
  targetpair(root.left, ele)
  h.append(root.data)
  
  targetpair(root.right, ele)
   
    
   
targetpair(root, a)  



i = 0
j = len(h) - 1

while(i<j):
  if(h[i] + h[j] ==a):
    print(h[i], h[j])
    i +=1
    j -= 1
  elif(h[i] + h[j] > a):
    j-=1
    
  elif(h[i] + h[j] < a): 
    i+=1
    