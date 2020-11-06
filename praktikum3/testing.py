
data = []
genap = []
ganjil = []
batas = int(input('enter size of array : '))
for i in range (batas) :
	data.append(int(input("input element  : ")))
	if i % 2 == 0 :
		genap.append(i)
	else :
		ganjil.append(i)
print("Big array : ",data)
print("even array : ",genap)
print("odd array : ",ganjil)
