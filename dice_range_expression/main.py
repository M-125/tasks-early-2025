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
	for e in reverse:
		
		if num>=e:
			return e
		#legnagyobbat visszaadja
		



for e in inputs:
	min=int(e[0])
	max=int(e[1])
	target=max-min+1
	result=[]
	while target-sum(result)>0:
		target=max-min+1+len(result)
		print(min,max,target-sum(result))
		dice=get_biggets_dice(target-sum(result))
		result.append(dice)
	print(e,max-min+1,result,max-(max-min+len(result) ))
	

