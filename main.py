print("Welcome to my quiz")

playing = input("Do you want to play a quiz? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Your answer is incorrect!!!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Your answer is incorrect!!!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Your answer is incorrect!!!")

answer = input("What does ROM stand for? ")
if answer.lower() == "read-only memory":
    print('Correct!')
    score += 1
else:
    print("Your answer is incorrect!!!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Your answer is incorrect!!!")

print(f"Congrats, you got {score} correct answer, out of 5!!!")