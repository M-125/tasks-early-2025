with open('./input.txt', 'r') as f:
  input = f.read()
import random
inputs=[e.rstrip(" ").split(" ") for e in input.rstrip("\n").split("\n")]
dies=[2,3,4,6,8,10,20]

#inputs+=[[random.randrange(-100,100),random.randrange(-100,100)]for e in range(10)]

#print(inputs)
#for e in inputs:e.sort()
def get_biggets_dice(num):
	reverse=dies[:]
	reverse.reverse()
	if num%2==1:return 3,num-3 #ha páratlan akkor 3as kocka
	for e in reverse:
		
		if num>=e:
			return e,num-e#legnagyobbat visszaadja
		



for e in inputs:
	min=int(e[0])
	max=int(e[1])
	diff=max-min+1
	result=[]
	while diff>0:
		print(min,max,diff)
		dice,diff=get_biggets_dice(diff)
		result.append(dice)
	print(e,max-min+1,result,max-(max-min+sum(1 for e in result) ))
	

