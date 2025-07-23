import requests

FIREBASE_URL = "https://any-thing-93729-default-rtdb.firebaseio.com/students.json"

for i in range(1,3):
     print('the students', i)
     student = {}
     x = input("Enter the student name: ")  
     student['name'] = x
     grades = {}
     for j in range(1,5):
          if j == 1:
               s = 'Arbic'
          elif j == 2:
               s = 'math'
          elif j == 3:
               s = 'english'
          else:
               s = 'science'    
          print(s)
          m = input('Enter the student degree: ')
          if m.isdigit():
               m = float(m)
               if m >= 90:
                    y = "excellent"
               elif m >= 80:
                    y = "very good"
               elif m >= 60:
                    y = "good"
               elif m >= 50:
                    y = "pass"
               else:
                    y = 'fail'
               grades[s] = {'degree': m, 'result': y}
          else:
               print("wrong entry _tryAgain")
               j -= 1 
     student['grades'] = grades
     response = requests.post(FIREBASE_URL, json=student)
     if response.status_code == 200:
          print("Student data has been sent successfully !")
     else:
          print("An error occurred while sending the data:", response.text)
 