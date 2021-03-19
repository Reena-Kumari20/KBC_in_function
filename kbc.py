question=["How many cntinents are there?","What is the capital of India?","Navgurukul me kon sa cource pdaya jata hai?"]
option=[["Four","Nine","Seven","eight"],["chandigarh","Bhopal","Chennai","Delhi"],["Software Engineer","Counseling","Tourism","Agricuture"]]
life_line=[["Four","Seven"],["Bhopal","Delhi"],["Software","Counseling"]]

solution1=[3,4,1]
solution2=[2,2,1]

c=0
def life_line5050(i):
    global c
    if c==1:
        print("you already use 5050")
    if c==0:
        j=0
        while j<len(life_line[i]):
            print(j+1,life_line[i][j])
            j=j+1
        c=c+1
        user=int(input("enter the your answer:____"))
        if user==solution2[i]:
            return True
        else:
            return False
    else:
        print("you already use this option 5050\nNow you can not use this life_line")
        return False

def opt(i):
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j=j+1
    user=int(input("enter the answer:______"))
    if user==solution1[i]:
        return True
    if user==5050:
        return(life_line5050(i))
    else:
        return False

def ques():
    i=0
    while i<len(question):
        print("Question.",i+1,question[i])
        answers=opt(i)
        if answers==True:
            print("your answer is right")
        else:
            print("you answer is wrong")
            break
            
        i=i+1
    #print("your all answer is right\nNow you are the winner of this game")


def main_KBC():
    print("WELCOME TO OUR GAME 'KON BNEGA KAROREPATI'....")
    ques()
main_KBC()
