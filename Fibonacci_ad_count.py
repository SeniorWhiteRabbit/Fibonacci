first=1
second=1
score=0 #actual number of digits
count=2 #counter of strings in sequence with the same length
co_list=[] #counter's records
cun=None  #co_list.append
stop=40 #the limit of number's length
deb=0 #
def fib(first,sec,score,co,deb):
	sec+=first
	sc=len(str(sec))
	print(sec,(stop-sc)*"-", sc,end="")
	if sc==len(str(sec+first)):
		print("")
		co+=1
		cu=False
		d=deb
	elif sc!=len(str(sec+first)):
		print("",(4-len(str(sc)))*"-",co,"after [%s]" %deb)
		d=str(sec)[0]
		cu=co
		co=1
	return sec,first,sc,co,cu,d

q=input("Do you want to set initial values? (Y/N)")
if q=="Y"or q=="y":
	first=int(input("Enter first number:\n"))
	second=int(input("Enter second number:\n"))

print("\n ",(stop-1)*"-","\n")
score=len(str(first))
print(first,(stop-score)*"-", score)
score=len(str(second))
print(second,(stop-score)*"-", score)

while score<stop:
	if first>=second:
		first,second,score,count,cun,deb=fib(first,second,score,count,deb)
		if cun:co_list.append(cun)
	elif first<second:
		first,second,score,count,cun,deb=fib(second,first,score,count,deb)	
		if cun:co_list.append(cun)
else: print(co_list)