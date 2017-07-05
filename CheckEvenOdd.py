def inputNum() :
  arr = list()
  num = raw_input("Enter how many elements you want : ")
  print 'Enter numbers in array : '
  for i in range(int(num)) :
      n = raw_input("Number index "+ str(i+1) +" : ")
      arr.append(int(n))
  print 'Your number is : ',arr
  return arr

def checkNum(arr) :
  oddList = list()
  evenList = list()
  
  for n in arr :
    if n%2 != 0 :
      oddList.append(int(n))
      # print 'N is ',n,' [Odd]'
    else:
      evenList.append(int(n))
      # print 'N is ',n,' [Even]'

  printVal(oddList, evenList)

def printVal(oddList, evenList):
  oddPrint = "Odd : "
  evenPrint = "Even : "
  for odd in oddList:
    oddPrint = oddPrint + str(odd) + "  "

  for even in evenList:
    evenPrint = evenPrint + str(even) + "  "

  print oddPrint
  print evenPrint
  
status = False

while status == False :
  arr = inputNum()
  confirm = raw_input("Confirm your number ? [Y/y] : ")
  if confirm in ('Y', 'y') :
    status = True

checkNum(arr)
  

