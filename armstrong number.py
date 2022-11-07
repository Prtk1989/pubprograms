while True:
 print "\nHi! this is Armstrong number program\n"
 num = int(input("enter the number:"))
 sum1 =0
 temp = num
 while temp > 0:
  digit = temp %10
  sum1 = sum1 + digit ** len(str(num))
  temp = temp/10
  print (sum1)
 if num == sum1:
  print ("the number is Armstrong")
 else:
  print ("the number is not Armstrong")
