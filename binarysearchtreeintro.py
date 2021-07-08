
class btree():
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.right = right
    self.left = left
   
 
n = [12,25,37,50,62, 75,87] 


def bsttree(n, start, end):
  while(start<=end):
    mid = (start +end)//2
    
    val = n[mid]
    lc = bsttree(n, start, mid - 1)
    
    rc = bsttree(n, mid +1, end)
    
    p = btree(val, lc, rc)
    
    return p
    
  
root = bsttree(n,0, len(n)-1) 

   
    
def display(root):
  if(root == None):
    return
  s = ""
  s += str(root.left.data) if (root.left!=None) else "."
  
  s += "<-" + str(root.data) + "->" 
  
  s += str(root.right.data) if (root.right!=None) else "."
 
  print(s)
  
  display(root.left)
  display(root.right)   
    
    
  
display(root)
  