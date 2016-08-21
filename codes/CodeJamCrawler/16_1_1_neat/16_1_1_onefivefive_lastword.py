class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
def lastword(inputfile, outputfile):
	fr=open(inputfile,'r')
	T=int(fr.readline())
	print(T)
	fw=open(outputfile,'w')
	for i in range(T):
		s=fr.readline()
		slen=len(s)
		head=ListNode(s[0])
		end=head
		for j in range(1,slen):
			node=ListNode(s[j])
			if node.val>=head.val:
				node.next=head
				head=node
			else:
				end.next=node
				end=node
		node=head
		result=''
		while node!=None:
			result=result+node.val
			node=node.next
		rs='Case #'+str(i+1)+': '+result
		fw.write(rs)
	fw.close
	fr.close
	return
