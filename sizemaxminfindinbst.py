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
ele =int(input())


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





def size(root):
  if(root ==None):
    return 0
  p = size(root.left)
  q = size(root.right)
   
  temp = p+q +1
  return temp
  
print(size(root))


def sumoftree(root):
  if(root ==None):
    return 0
  p = sumoftree(root.left)
  q = sumoftree(root.right)
   
  temp = p+q +root.data
  return temp
  
print(sumoftree(root))




def maxintree(root):
  
  if(root == None):
    return -1*sys.maxsize
 
  p = maxintree(root.right)
 
  temp = max(p, root.data)
 
  return temp
 
print(maxintree(root))



def minintree(root):
  
  if(root == None):
    return sys.maxsize
 
  p = minintree(root.left)
 
  temp = min(p, root.data)
 
  return temp
 
print(minintree(root))


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
 

print("true") if(findintree(root, ele))  else print("false")



