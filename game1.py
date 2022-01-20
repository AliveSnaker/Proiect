import pygame
import random
from network import Network
 
from pygame.constants import K_LEFT, KEYDOWN, KEYUP

pygame.init()

screen = pygame.display.set_mode((1920, 1020))

background = pygame.image.load('tablanoua2.png')


pygame.display.set_caption("Table cu prietenii")
icon = pygame.image.load('backgammon.png')
pygame.display.set_icon(icon)
piesa1=pygame.image.load('piesa1.png')
piesa2=pygame.image.load('piesa2.png')

def redrawWindow(screen,player, player2):
    screen.fill((255,255,255))
    player.draw(screen)
    player2.draw(screen)
    pygame.display.update()

run = True
n = Network()
p = n.getP()
clock = pygame.time.Clock()


clock.tick(60)
p2 = n.send(p)

for event in pygame.event.get():
      if event.type == pygame.QUIT:
            run = False
            pygame.quit()

#zaruri

def primulzar():
 val1=random.randint(1, 6)
 
 return val1

def aldoileazar():
    val2=random.randint(1,6)

    return val2

         

zar_image1 = pygame.image.load('zartest1.png')
def zar1():
 #primulzar()
 

 val1=primulzar()
 if val1==1:
  zarA1=pygame.image.load('zartest1.png')
 elif val1==2:
    zarA1=pygame.image.load('zartest2.png')
 elif val1==3:
    zarA1=pygame.image.load('zartest3.png')
 elif val1==4:
    zarA1=pygame.image.load('zartest4.png')
 elif val1==5:
    zarA1=pygame.image.load('zartest5.png')
 elif val1==6:
    zarA1=pygame.image.load('zartest6.png')
 return zarA1
 

zar_image2 = pygame.image.load('zartest2.png')
 # al doilea zar
def zar2():

 val2=aldoileazar()
 if val2==1:
  zarA1=pygame.image.load('zartest1.png')
 elif val2==2:
    zarA1=pygame.image.load('zartest2.png')
 elif val2==3:
    zarA1=pygame.image.load('zartest3.png')
 elif val2==4:
    zarA1=pygame.image.load('zartest4.png')
 elif val2==5:
    zarA1=pygame.image.load('zartest5.png')
 elif val2==6:
    zarA1=pygame.image.load('zartest6.png')
 return zarA1


#Grid
class Grid:
    def __init__(self):
       self.grid_lines = [((90,137), (1475,137)),
                          ((90,229), (1475,229)),
                          ((90,321), (1475,321)),
                          ((90,413), (1475,413)),
                          ((90,505), (1475,505)),
                          ((90,597), (1475,597)),
                          ((90,689), (1475,689)),
                          ((90,781), (1475,781)),
                          ((90,873), (1475,873)),
                          ((85,45), (85,970)),
                          ((192,45), (192,970)),
                          ((299,45), (299,970)),
                          ((406,45), (406,970)),
                          ((513,45), (513,970)),
                          ((620,45), (620,970)),
                          ((727,45), (727,970)),
                          ((834,45), (834,970)),
                          ((941,45), (941,970)),
                          ((1048,45), (1048,970)),
                          ((1155,45), (1155,970)),
                          ((1262,45), (1262,970)),
                          ((1369,45), (1369,970)),
                          ((1476,45), (1476,970)),]

       self.grid =[[0 for x in range(13)] for y in range(10)]
       

    def draw(self, screen):
        for line in self.grid_lines:
            pygame.draw.line(screen, (200, 200, 200), line[0], line[1], 2)

        for y in range (len(self.grid)):
           for x in range (len(self.grid[y])):
              if self.get_cell_value(y,x) =="X":
                 screen.blit(piesa1, ((x*107+90), (y*92+45)))
              elif self.get_cell_value(y,x) =="O":
                 screen.blit(piesa2, ((x*107+90),(y*92+45)))   

    def get_cell_value(self, x, y):
       return self.grid[x][y]

    def set_cell_value(self, x, y, value):
       self.grid[x][y]=value

    def get_mouse(self, x, y, player):
       if player=="7x":
          self.set_cell_value(x, y, "0")
       elif player=="6x":
          self.set_cell_value(x, y, "X")
       elif player=="5x":
          self.set_cell_value(x, y, "0")
       elif player=="4x":
          self.set_cell_value(x, y, "X")
       elif player=="3x":
          self.set_cell_value(x, y, "0")
       elif player=="2x":
          self.set_cell_value(x, y, "X")
       elif player=="1x":
          self.set_cell_value(x, y, "0")
       elif player=="x":
          self.set_cell_value(x, y, "X")


       elif player=="7o":
          self.set_cell_value(x, y, "0")
       elif player=="6o":
          self.set_cell_value(x, y, "O")
       elif player=="5o":
          self.set_cell_value(x, y, "0")
       elif player=="4o":
          self.set_cell_value(x, y, "O")
       elif player=="3o":
          self.set_cell_value(x, y, "0")
       elif player=="2o":
          self.set_cell_value(x, y, "O") 
       elif player=="1o":
          self.set_cell_value(x, y, "0")   
       elif player=="o":
          self.set_cell_value(x, y, "O") 


    def print_grid(self):
       for row in self.grid:
          print(row)


grid=Grid()
grid.set_cell_value(0,0,"X")
grid.set_cell_value(1,0,"X")
grid.set_cell_value(2,0,"X")
grid.set_cell_value(3,0,"X")
grid.set_cell_value(4,0,"X")
grid.set_cell_value(5,0,"O")
grid.set_cell_value(6,0,"O")
grid.set_cell_value(7,0,"O")
grid.set_cell_value(8,0,"O")
grid.set_cell_value(9,0,"O")
grid.set_cell_value(7,4,"X")
grid.set_cell_value(8,4,"X")
grid.set_cell_value(9,4,"X")
grid.set_cell_value(0,4,"O")
grid.set_cell_value(1,4,"O")
grid.set_cell_value(2,4,"O")
grid.set_cell_value(0,7,"O")
grid.set_cell_value(1,7,"O")
grid.set_cell_value(2,7,"O")
grid.set_cell_value(3,7,"O")
grid.set_cell_value(4,7,"O")
grid.set_cell_value(5,7,"X")
grid.set_cell_value(6,7,"X")
grid.set_cell_value(7,7,"X")
grid.set_cell_value(8,7,"X")
grid.set_cell_value(9,7,"X")
grid.set_cell_value(0,12,"X")
grid.set_cell_value(1,12,"X")
grid.set_cell_value(8,12,"O")
grid.set_cell_value(9,12,"O")

# nr1=primulzar()
# nr2=aldoileazar()
# if nr1!=nr2:
#   player="3x"
# elif nr1==nr2:
#   player="7x"

# def rand1(a):
#  z=a
#  nrzar1=primulzar()
#  nrzar2=aldoileazar()
#  if z=="x":
#   if nrzar1>nrzar2 or nrzar1<nrzar2:
#    return"3x"
#   elif nrzar1==nrzar2:
#    return"7x"
#  elif z=="o":
#     if nrzar1>nrzar2 or nrzar1<nrzar2:
#      return"3o"
#     elif nrzar1==nrzar2:
#      return "7o"
player="3x"



#game loop
open = True
while open:
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    grid.draw(screen) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
             pos=pygame.mouse.get_pos()
             grid.get_mouse((pos[1]-45)//92, (pos[0]-90)//107, player)
             if player == "7x":
                player = "6x"
             elif player == "6x":
                player = "5x"
             elif player == "5x":
                player = "4x"
             elif player == "4x":
                player = "3x"         
             elif player == "3x":
                player = "2x"
             elif player=="2x":
                player="1x"  
             elif player=="1x":
                player="x"
             elif player=="x": #and rand1==1:
                player = "3o"
             #elif player=="x": #and rand1==2:
              #  player=="3o"  

             elif player=="7o":
                player="6o"
             elif player=="6o":
                player="5o"
             elif player=="5o":
                player="4o"
             elif player=="4o":
                player="3o"
             elif player=="3o":
                player="2o"
             elif player=="2o":
                player="1o"
             elif player=="1o":
                player="o"
             elif player=="o": #and rand1==1:
                player="3x"
            # elif player=="o" and rand1==2:
             #   player="3x"


             grid.print_grid()    
    
 
         
        
         



    if event.type==pygame.KEYDOWN:    
       if event.key==pygame.K_LEFT:               
             zar_image1=zar1()

           
      
    screen.blit(zar_image1, (1650, 510))
    
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            zar_image2=zar2()
           
    


      
    screen.blit(zar_image2, (1750, 510))
    
    if zar_image1==zar_image2:
     rand1=1
    else:
     rand1=2
    print (rand1) 


    pygame.display.update()

pygame.quit()
quit()