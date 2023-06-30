print("Welcome to my computer quiz!")
playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
print("Okay Let´s play :)")
score=0 #Stablis a score

answer=input("1.Whats does CPU stand for? ").lower()
if answer== "central proccessing unit":
    print('Correct!')
    score +=1 #Increase the score if user got it right
else:
    print("Incorrect!")

answer=input("2.What does GPU stand for? ").lower()
if answer=="graphics proccessing unit":
    print('Correct')
    score +=1
else:
    print('Incorrect')

answer=input("3.Whats does PSU stand for? ").lower()
if answer=="power supply":
    print('Correct')
    score+=1
else:
    print('Incorrect!')

answer=input("4.What does Ram stand for? ").lower()
if answer=="random access memory":
    print('Correct')
    score+=1
else:
    print('Incorrect!')

print("Thaks for playing\n","Score: "+str(score) )
print("You got "+str((score/4)*100)+"%.")


