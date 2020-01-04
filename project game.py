#Piano Tiles Game

import turtle
import random
import winsound

window= turtle.Screen()
window.title("masis' game")
window.bgcolor("beige")
window.setup(width=500, height=500)

def move_left():
    player.setx(player.xcor()-20)
    
def move_right():
    player.setx(player.xcor()+20)





player= turtle.Turtle()    #creating player
player.speed(0)
player.shape("triangle")
player.color("blue")
player.penup()
player.goto(0,-200)
player.direction= "90"
player.left(90)
p=0
t=0
i=-1
turtle.write("1: Ode to Joy\n2: Jingle Bells\n3: Spring\n4: Romance\n5: Marry Had a Little Lamb\n6: Happy Birthday\n7: Twinkle Twinkle\n8: Practice")
choice= window.numinput("Please choose a melody","choice")

if (choice)==1:
    a = 3,3,4,5,5,4,3,2,1,1,2,3,3,2,2,3,3,4,5,5,4,3,2,1,1,2,3,2,1,1,2,2,3,1,2,3,4,3,1,2,3,4,3,2,1,2,1,1,3,3,4,5,5,4,3,2,1,1,2,3,2,1,1
  
if (choice)==2:
    a =3,3,3_2,3,3,3_2,3,5,1,2,3_4,4,4,4,4,4,3,3,3,3,2,2,3,2_2,5_2,3,3,3_2,3,3,3_2,3,5,1,2,3_4,4,4,4,4,4,3,3,3,5,5,4,2,1_4

if (choice)==3:
    a =5,7,7,7,6-5,2.2_2,2.2-1.2,7,7,7,6-5,2.2_2,2.2-1.2,7,1.2-2.2,1.2,7,6,9/2,2,5,7,7,7,6-5,2.2_2,2.2-1.2,7,7,7,6-5,2.2_2,2.2-1.2,7,1.2-2.2,1.2,7,6_2,5,2.2,1.2-7,1.2,2.2,3,2_2,5,2.2,1.2-7,1.1,2.2,3.2,2.2_2,5,3,2.2_2,1.1,7,6-5,6_2,5_2,5,5_2

if (choice)==4:
    a =3.2,3.2,3.2,3.2,2.2,1.2,1.2,7,6,6,1.2,3.2,6.2,6.2,6.2,6.2,5.2,4.2,4.2,3.2,2.2,2.2,3.2,4.2,3.2,4.2,3.2,11/2.2,4.2,3.2,3.2,2.2,1.2,1.2,7,6,7,7,7,7,1.2,7,6,1.2,3.2,6,3/2.2,3/2.2,3/2.2,3/2.2,7,6,6,11/2,11/2,11/2,5,11/2,9/2.2,9/2.2,9/2.2,9/2.2,11/2.2,9/2.2,9/2.2,3.2,3.2,3.2,9/2.2,11/2.2,6.2,6.2,6.2,6.2,11/2.2,11/2,9/2.2,9/2.2,9/2.2,9/2.2,3.2,2.2,3/2.2,3/2.2,3/2.2,3/2.2,2.2,7,6,3/2.2,3.2,6

if (choice)==5:
    a =3,2,1,2,3,3,3_2,2,2,2_2,3,5,5_2,3,2,1,2,3,3,3,3,2,2,3,2,1_4
    
if (choice==6):
    a =2,2,3,2,5,9/2,2,2,3,2,6,5,2,2,2.2,7,5,9/2,3,1.2,1.2,7,5,6,5
    
if (choice==7):
    a =1,1,5,5,6,6,5_2,4,4,3,3,2,2,1
if (choice==8):
    a=1,2,3,4,5,4,3,2,3,4,5,6,7,6,5,4,5,6,7,1.2,2.2,1.2,7,6,7,1.2,2.2,3.2,4.2,3.2,2.2,1.2,7,1.2,2.2,1.2,7,6,5,4,3,4,5,4,3,2,1_2
    
    
while True:
     
     window.listen()

     window.onkeypress(move_left, "Left") #moves the player toward left while the "Left" key is pressed
     window.onkeypress(move_right, "Right")#moves the player toward left while the "Right" key is pressed

     
     i=i+1
     t=t+1
     
     
         
     #representing the notes as an array of numbers (9th symphonie)
     circle=turtle.Turtle()
     b=random.randint(-75,75)# the interval of position at which the circles will appear 
   
     circle.speed(0)
     circle.shape("circle")
     
     if(a[i]==1): #defining circle colors regarding to notes
      circle.color("red")
     if(a[i]==2):
         circle.color("brown")
     if(a[i]==3):
         circle.color("yellow")
     if(a[i]==4):
         circle.color("green")
     if(a[i]==5):
         circle.color("blue")
     if(a[i]==6):
         circle.color("violet")
     if(a[i]==7):
         circle.color("pink")    
         
    
     circle.penup()
     circle.shapesize(2)
     circle.setx(b)
     circle.sety(-50)
     circle.direction= "90"
     circle.left(90)
     if t==len(a):
        turtle.clear()
        turtle.write("\ngame end\nsucces:%\n  ")
        turtle.write((p/t)*100)
       
        
        break
        
       
   
     for j in range(100):
       circle.backward(5)
       if((circle.ycor()==-200) and ((b-25)<player.xcor()<(b+25))): #checking the incedence
        turtle.hideturtle()
        p=p+1
        turtle.clear()
        turtle.write(p)
        if (a[i]==1):
           winsound.Beep(523,500)#do
        if (a[i]==2):    
           winsound.Beep(587,500)#re
        if (a[i]==3):
           winsound.Beep(659,500)#mi
        if (a[i]==4):
           winsound.Beep(698,500)#fa
        if (a[i]==5):
            winsound.Beep(783,500)#sol
        if (a[i]==6):#
            winsound.Beep(880,500)#la
        if (a[i]==7):
            winsound.Beep(987,500)#si
        
        
        if (a[i]==1_4):
            winsound.Beep(523,2000)#do4
        if (a[i]==2_4):
            winsound.Beep(587,2000)#re4
        if (a[i]==3_4):
            winsound.Beep(659,2000)#mi4
        if (a[i]==4_4):
            winsound.Beep(698,2000)#fa4
        if (a[i]==5_4):
            winsound.Beep(783,2000)#sol4
        if (a[i]==6_4):
            winsound.Beep(880,2000)#la4
        if (a[i]==7_4):
            winsound.Beep(987,2000)#si4
            
            
        if (a[i]==1_2):
            winsound.Beep(523,1000)#do2
        if (a[i]==2_2):
            winsound.Beep(587,1000)#re2
        if (a[i]==3_2):
            winsound.Beep(659,1000)#mi2
        if (a[i]==4_2):
            winsound.Beep(698,1000)#fa2
        if (a[i]==5_2):
            winsound.Beep(783,1000)#sol2
        if (a[i]==6_2):
            winsound.Beep(880,1000)#la2
        if (a[i]==7_2):
            winsound.Beep(987,1000)#si2
        
               
        #second octave
             
         
        if (a[i]==(1.2)):
           winsound.Beep(1046,500)#do
        if (a[i]==2.2):    
           winsound.Beep(1174,500)#re
        if (a[i]==3.2):
           winsound.Beep(1318,500)#mi
        if (a[i]==4.2):
           winsound.Beep(1396,500)#fa
        if (a[i]==5.2):
            winsound.Beep(1567,500)#sol
        if (a[i]==6.2):#
            winsound.Beep(1760,500)#la
        if (a[i]==7.2):
            winsound.Beep(1975,500)#si
        
        
        if (a[i]==1.2_4):
            winsound.Beep(1046,2000)#do4
        if (a[i]==2.2_4):
            winsound.Beep(1174,2000)#re4
        if (a[i]==3.2_4):
            winsound.Beep(1318,2000)#mi4
        if (a[i]==4.2_4):
            winsound.Beep(1396,2000)#fa4
        if (a[i]==5.2_4):
            winsound.Beep(1567,2000)#sol4
        if (a[i]==6.2_4):
            winsound.Beep(1760,2000)#la4
        if (a[i]==7.2_4):
            winsound.Beep(1975,2000)#si4
            
            
        if (a[i]==(1.2_2)):
            winsound.Beep(1046,1000)#do2
        if (a[i]==(2.2_2)):
            winsound.Beep(1174,1000)#re2
        if (a[i]==(3.2_2)):
            winsound.Beep(1318,1000)#mi2
        if (a[i]==(4.2_2)):
            winsound.Beep(1396,1000)#fa2
        if (a[i]==(5.2_2)):
            winsound.Beep(1567,1000)#sol2
        if (a[i]==(6.2_2)):
            winsound.Beep(1760,1000)#la2
        if (a[i]==(7.2_2)):
            winsound.Beep(1975,1000)#si2
            
            
            
            
            
        #special cases
        if(a[i]==(6-5)):
            winsound.Beep(880,200)
            winsound.Beep(783,200)
        if (a[i]== 2.2-1.2):
            winsound.Beep(1174,200)
            winsound.Beep(1046,200)
        if (a[i]== 1.2-2.2):
            winsound.Beep(1046,200)
            winsound.Beep(1174,200)
        
        if (a[i]== 3/2.2):
            winsound.Beep(1108,500)#do*   winsound.Beep(1108,500)#do*
            
    
        if (a[i]== 9/2):
            winsound.Beep(740,500)#fa*
        if (a[i]== 9/2.2):
            winsound.Beep(1479,500)   
            
        
        if (a[i]==11/2):
            winsound.Beep(830,500)#sol*
            
        if (a[i]==11/2.2):
            winsound.Beep(1661,500)#sol*
            
        
               
       
           
            
                        
        
    
          
    
