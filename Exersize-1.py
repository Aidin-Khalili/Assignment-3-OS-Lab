from random import choice
words=["book","phone","soccer","food","king","computer","car","clock"]
true_answer = choice(words)
health = 10
flag = True
answer = dict()
while True:
    flag = True
    id = 0
    for char in true_answer:
        if (true_answer.index(char,id) in answer) and (char == answer[true_answer.index(char,id)]):
            print(char, end = '')
        else:
            print("_ ", end = '') 
            flag = False
        id += 1
    if flag == 1:
        print("\nYou Win ! congragulation")
        break
    ans = input("Enter your guess letter : ")
    position = int(input("\nEnter a position that you think it is : "))
    if ans == true_answer[position]:
        answer[position] = ans
        print("Yeeeeep")
    else:
        print("noooo, it doesn\'t have it.")
        health -= 1
    if health == 0:
        print ("The answer is :" , true_answer ,"\nGame over !")
        break