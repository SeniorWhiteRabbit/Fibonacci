data=[1,1,0]
stop=20 #number of digits, required to reach before the stop
def fib(first,sec,score=data[2]):
	sec+=first
	score=len(str(sec))
	print((stop-score)*"-",str(sec)[::-1],sec,(stop-score)*"-")
	return sec,first,score

data[0]=int(input("Enter first number:\n"))
data[1]=int(input("Enter second number:\n"))

print("\n",stop*"-",stop*"-","\n")
data[2]=len(str(data[0]))
print((stop-data[2])*"-",str(data[0])[::-1],data[0],(stop-data[2])*"-")
data[2]=len(str(data[1]))
print((stop-data[2])*"-",str(data[1])[::-1],data[1],(stop-data[2])*"-")

while data[2]<stop:
	if data[0]>=data[1]:
		data=fib(data[0],data[1])
	elif data[0]<data[1]:
		data=fib(data[1],data[0])	