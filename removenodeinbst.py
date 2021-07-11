
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


def maxintree(root): 
  if(root == None):
    return -1*sys.maxsize
 
  p = maxintree(root.right)
 
  temp = max(p, root.data)
 
  return temp
  

def removenode(root, ele):
  if(root ==None):
    return None
  
  if(ele <root.data):
    p = removenode(root.left, ele)
    root.left = p
    
  elif(ele > root.data):
    q = removenode(root.right , ele)
    root.right = q
   
  else:
    if(root.left!=None and root.right!=None):
      d = maxintree(root.left)
      root.data = d
      root.left = removenode(root.left, d)
      return root
      
      
    elif(root.left!=None):
      return root.left
      
    elif(root.right!=None):
      return root.right
      
    else:
      return None
      
  return root
  
  
  
removenode(root, ele)
  

      
    
      
      
    
    
def display(root):
  if(root == None):
    return  
  s = ""
  s += str(root.left.data) if (root.left!=None) else "."
  
  s += " <- " + str(root.data) + " -> " 
  
  s += str(root.right.data) if (root.right!=None) else "."
 
  print(s)
  
  display(root.left)
  display(root.right)   
    
    
  
display(root)
  