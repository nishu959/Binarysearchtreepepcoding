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



def findintree(root, ele):
  if(root == None):
    return False
  
  if(root.data == ele):
    return True
   
  if(ele > root.data):
    p = findintree(root.right, ele)
    if(p == True):
      return True
  elif(ele < root.data):
    p = findintree(root.left, ele)
    if(p == True):
      return True
   
  return False
  


def targetpair(root, ele, realroot):
  global h
  if(root == None):
    return 
    
  targetpair(root.left, ele, realroot)
  a = ele - root.data
  if(a>root.data):
    if(findintree(realroot, a)):
      print(root.data,a)
  
  targetpair(root.right, ele, realroot)
   
    
   
targetpair(root, a, root)