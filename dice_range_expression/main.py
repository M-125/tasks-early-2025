with open('./input.txt', 'r') as f:
  input = f.read()
import random
inputs=[e.rstrip(" ").split(" ") for e in input.rstrip("\n").split("\n")]
dies=[20, 10, 8, 6, 4, 3, 2]

#inputs+=[[random.randrange(-100,100),random.randrange(-100,100)]for e in range(10)]

#print(inputs)
#for e in inputs:e.sort()


def get_biggets_dice(num):
	for e in dies:
		
		if num>=e:
			return e
		#legnagyobbat visszaadja
		
def get_dice_list(input):
	min=int(input[0])
	max=int(input[1])
	target=max-min+1
	result=[]
	while target-sum(result)>0:
		target=max-min+1+len(result)
		print(min,max,target-sum(result))
		dice=get_biggets_dice(target-sum(result))
		result.append(dice)
	return [result,min-len(result)]

def to_text(Dlist):
	dict={}
	for e in Dlist[0]:
		if not e in dict:
			dict[e]=1
		else:
			dict[e]+=1
	text=""
	for e in dict:
		text+=f"{dict[e]}d{e}+"
	if Dlist[1]<=0:text=text.rstrip("+")
	if Dlist[1]!=0:
		text+=str(Dlist[1])
	
	return text

	

results=[get_dice_list(e) for e in inputs]
print(results)
for e in results:
	print(to_text(e))
	

