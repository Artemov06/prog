polog = []
i = 0
score = 0
gameOver=1
class Koronavirus:
    def __init__(self,r):
        self.r = r
        self.img = [loadImage("gha.png")]
    def loading(self):
        global polog
        x = random(20,570)
        y = -10
        polog.append({'x': x,'y': y})
    def draw_(self):
        global polog,start,x,score,y,gameOver
        for j in range(len(polog)-1):
            image(self.img[0],polog[j]['x'],polog[j]['y'],self.r+10,self.r+10)
            polog[j]['y'] += 10
            if polog[j]['y'] > y-40 and polog[j]['y'] < y+40 and polog[j]['x'] > x-50 and polog[j]['x'] < x+50:
                start = 0
                gameOver= 0
    def reload(self):
        for i in range(len(polog)):
            del polog[0]
x=300
y=500
speed=10
start=0
pause = 0 
i = 0
j = 100
o=j
def Geometry(x,y):
    fill("#FE03FF")
    rect(x+18,y+18,50,50)
    fill("#03DBFF")
    rect(x+5,y+13,15,10)
    rect(x+30,y+13,15,10)
    rect(x+20,y+30,15,10)
def setup():
    global koronavirus,immage
    immage = [loadImage("gha02.jpg"),loadImage("10101.png")]
    koronavirus = Koronavirus(50)
    size(600,600)
    background(255)
    rectMode(CENTER)
    textSize(50)
def draw():
    image(immage[1],0,0,600,600)
    global x,y,speed,start,i,j
    fill(0-255)
    o=j
    text(o,60,60)

    if start == 1:
        if i % j == 0 and j > 8:
            koronavirus.loading()
            j-=1
        i+=1
        koronavirus.draw_()
        Geometry(x,y)
    if j < 9 or start == 0:
        background(225)
        start = 0
        j = 100
        koronavirus.reload()
    print(j)
    if keyPressed:
        if keyCode == LEFT and x > -1:
            x-= speed
        elif keyCode == RIGHT and x < 550:
            x+= speed
        elif key == ' ' and start == 1:
            start = 2
    
    if start == 2:
        background(225)
        fill(255,0,0)
        rect(310,300,70,70)
        fill("#F6FF08")
        text("I",290,320)
        text("I",310,320)

                   
            
    if start == 0:
        fill("#F0B71B")
        rect(300,300,150,100)
        fill(255,0,0)
        triangle(475-200,275,475-200,325,525-200,300)
        text("S",225,230)
        fill("#FA9B00")
        text("T",250,230)
        fill("#F6FF08")
        text("A",275,230)
        fill("#08FF16")
        text("R",310,230)
        fill("#08F5FF")
        text("T",335,230)
        fill("#FE00FF")  
        if gameOver == 0:
            text("!GameOver!",170,450)

def mousePressed():
    global start,score,x
    if mouseX > 425-200 and mouseX < 575-200 and mouseY > 250 and mouseY < 350:
        start = 1
        score = 0
        x = 300
