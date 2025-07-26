# logical operators = evaluate multiple conditions (or, and, not)

temp = 25
is_raining  = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else: 
    print("The outdoor event is still scheduled")


sub1_marks = 20
sub2_marks = 45
sub3_marks = 10

avgmarks = ((sub1_marks+sub2_marks+sub3_marks)/300)*100

if avgmarks > 70:
    print(avgmarks,"You really smart")
elif sub1_marks > 50 and sub2_marks > 50 and sub3_marks > 50:
    print(avgmarks,"You are above average student")
elif avgmarks > 20 and avgmarks < 50:
    print(avgmarks,"Enough to pass..")
elif avgmarks < 20:
    print(avgmarks,"Damn bro you are dumb")
else:
    print("Invalid marks or input")



isSmart = True

if not isSmart:
    print("You are not smart")
else:
    print("You are smart")