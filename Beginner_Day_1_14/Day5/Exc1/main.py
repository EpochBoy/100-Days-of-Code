# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

sumheight = 0
totalstudents = 0

for studentheight in student_heights:
    sumheight += studentheight
    totalstudents+=1

if totalstudents == 0:
    print("Can't be 0 students, please input student heights")
    exit()

print(round(sumheight/totalstudents))