student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grade ={}

for i in student_scores:
   y = student_scores[i]
   if(y>=91 and y<=100):
     student_grade[f"{i}"]="Outstanding"
   elif(y>=81 and y<=90):
         student_grade[f"{i}"]="Exceeds Expectations"
   elif(y>=71 and y<=80):
        student_grade[f"{i}"]="Acceptable"
   else:
       student_grade[f"{i}"]="Fail"