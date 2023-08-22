f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\leapyear\\data.txt","w")
years=[2000,2024,1991,1995,1200,1400,1234,2020]

# for y in years:
#     if(y %100==0 and y %400==0):
#         f.write(str(y)+"\n")  #print(y)
#     elif(y %100!=0 and y %4==0):
#         f.write(str(y)+"\n")   #print(y)



#1890-3000

f=open("C:\\Users\\DELL\\Desktop\\pythonworks\\leapyear\\years.txt","w")

for num in range(1890,3001):
    f.write(str(num)+"\n")
print("process finished")
