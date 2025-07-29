question = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["What language is primarily used for web development?", "Python", "C++", "JavaScript", "Swift", 3],
    ["What is the boiling point of water?", "90°C", "100°C", "80°C", "110°C", 2],
    ["Who invented the light bulb?", "Einstein", "Newton", "Edison", "Tesla", 3],
    ["Which animal is known as the King of the Jungle?", "Elephant", "Tiger", "Lion", "Bear", 3],
    ["What is H2O?", "Hydrogen", "Water", "Oxygen", "Salt", 2],
    ["Which one is a programming language?", "Google", "HTML", "YouTube", "Windows", 2],
    ["Which is the largest ocean on Earth?", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "Atlantic Ocean", 3]
]

prizes = [100000,320000,40000,450000,500000,600000,700000,4300000,1500000,1000000]
sum = 0

i = 0
for question in question: 
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}") 
    print(f"d.{question[4]}")

    # chaeck whether the answer is correct or not
    a= int(input("Enter your answer.1 for a , 2 for b , 3 for c , 4 for d\n"))
    if(question[5]==a):
        print("Correct Answer!!")
    else:
        print(f"Incorrect , the correct answer was {question[5]}")
        print("Better Luck Next time!!")
        break

    sum +=prizes[i]
    print(f"You won {prizes[i]}")
    i += 1






