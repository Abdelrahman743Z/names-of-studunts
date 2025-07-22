lstname=[]
for i in range(1,3):
     print('the students' ,i )
     x=input("Enter the list member : ",)  
     lstname.append(x)
     for j in range(1,5):
          if j==1 :
               s='Arbic'
          elif j==2 :
               s='math'
          elif j==3 :
               s='english'
          else :
               s='science'    
          print(s)
          m=(input('Enter the students dagree :',))
          if m.isdigit():
               m=float(m)
               if m >= 90 : 
                    y=("excllent")
               elif m >= 80 :
                    y=("very good ")
               elif m >= 60 :        
                    y=("good")   
               elif m >= 50 :
                    y=("pass")
               else: 
                   y=('fail')

               lstname.append(s)
               lstname.append(m)
               lstname.append(y)

          else:
               print("wrong entery _tryAgain")
               j-=1  

print(lstname)
 