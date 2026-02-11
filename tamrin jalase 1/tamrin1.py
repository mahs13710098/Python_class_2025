d=float(input('please enter day number:'))
y=str(d//365)
r=d%365
w=str(r//7)
da=str(r%7)
print("The entered day is equivalent to "+ y + " years, with " + w + " weeks and " + da + " days")
