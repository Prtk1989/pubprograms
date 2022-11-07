print ("Armstrong Number Program")
num = int(input("Enter the number:"))

def armstrong(num):
	sum = 0
	temp = num
	while temp > 0 :
		digit = temp % 10
		sum = sum + digit ** len(str(num))
		temp = temp / 10
	if sum == num:
		print ("number", num , "is armstrong")
	else :
		print ("number", num ,"is not armstrong")

armstrong(num)