if __name__=="__main__":
	n = int(input())
	arr =list(map(int, input().split()))
	
	if n>=2 and n<=10:

		set_list=set(arr)
		
		winner=max(set_list)
		
		set_list.remove(winner)
		
		runner_up=max(set_list)
		
		print(runner_up)