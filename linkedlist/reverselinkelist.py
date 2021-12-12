def reverseList(self,head):
  # 1 > 2 > 3 > 4
  prev =None
  while head:
    temp =head
    head =head.next
    temp.next = prev
    prev =temp
    
   return prev
  
