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

def normalinorder(rp):
  
  while(len(rp)>0):
    
    top = rp[-1]
    if(top.state == 0):
      if(top.node.left!=None):
        
        p = pair(top.node.left,0)
        rp.append(p)
        
      top.state += 1
      
    elif(top.state == 1):
      if(top.node.right!=None):
        
        p = pair(top.node.right,0)
        rp.append(p)
        
      top.state+=1
      
      return top.node
      
    elif(top.state == 2):
      rp.pop()
    
  return None
  
  
  
def reverseinorder(rp):
 
  while(len(rp)>0):
    
    top = rp[-1]
    if(top.state == 0):
      
      if(top.node.right!=None):
        
        p = pair(top.node.right,0)
        rp.append(p)
        
      top.state += 1
      
    elif(top.state == 1):
      
      if(top.node.left!=None):
        
        p = pair(top.node.left,0)
        rp.append(p) 
        
      top.state+=1
      
       
      return top.node
      
    elif(top.state == 2):
      rp.pop()
    
  return None
  
   
def targetsum(root, ele):
  ls = []
  rs= []
  ls.append(pair(root, 0))
  rs.append(pair(root, 0))
  
  left = normalinorder(ls)
  right = reverseinorder(rs) 
  
  
  
  while(left.data < right.data):
    
    if(left.data + right.data < ele):
      
      
      left = normalinorder(ls)
     
      
    elif(left.data + right.data > ele):
      
      right = reverseinorder(rs)  
      
    else:
      
      print(left.data, right.data)
      left = normalinorder(ls)
      right = reverseinorder(rs) 
      
      

targetsum(root, ele)
    
 