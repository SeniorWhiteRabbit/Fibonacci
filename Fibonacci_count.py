first=1
second=1
score=0 #actual number of digits
count=0 #counter of strings in sequence with the same length
co_list=[] #counter's records
cun=None  #co_list.append
stop=40 #the limit of number's length
def fib(first,sec,score,co):
	sec+=first
	sc=len(str(sec))
	print(sec,(stop-sc)*"-", sc,end="")
	if sc==score:
		print("")
		co+=1
		cu=None
	elif sc!=score:
		print(" ",(4-len(str(sc)))*"-",co)
		cu=co
		co=1
	return sec,first,sc,co,cu

q=input("Do you want to set initial values? (Y/N)")
if q=="Y"or q=="y":
	first=int(input("Enter first number:\n"))
	second=int(input("Enter second number:\n"))

print("\n",stop*"-","\n")
score=len(str(first))
print(first,(stop-score)*"-", score)
score=len(str(second))
count+=2
print(second,(stop-score)*"-", score)

while score<stop:
	if first>=second:
		first,second,score,count,cun=fib(first,second,score,count)
		if cun!=None:co_list.append(cun)
	elif first<second:
		first,second,score,count,cun=fib(second,first,score,count)	
		if cun!=None:co_list.append(cun)
else: print(co_list)