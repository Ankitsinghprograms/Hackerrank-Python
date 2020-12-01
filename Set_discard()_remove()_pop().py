n=int(input())
s=set(map(int,input().split()))
for i in range(int(input())):
	user=input()
	i_list=user.split(" ")
	if i_list[0]=="pop":
		s.pop()
	if i_list[0]=="remove":
		s.remove(int(i_list[1]))
	if i_list[0]=="discard":
		s.discard(int(i_list[1]))

print(sum(s))
	
