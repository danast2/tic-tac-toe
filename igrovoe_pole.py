
import pygame
from sys import exit


pygame.init()
display = pygame.display.set_mode((510,510))


green=(34, 139, 34, 255)
blue=(0, 0, 139, 255)
red=(238, 44, 44, 255)

FPS=60
clock=pygame.time.Clock()

width=heigth=40
#длина отступа между квадратиками
margin=10



#вот аналогичная запись двумерного массива
#мы заполням массив 10 раз десятью нулями
# mas=[]
# for i in range(10):
#     mas.append([0]*10)


#это двумерный массив
#мы заполням массив 10 раз десятью нулями
mas=[[0]*10 for i in range(10)]




while True:
    #Ждем события (действия пользователя)
    for event in pygame.event.get():
        #если нажали на крестик то закрываем окно
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #когда кто нажимает на кнопку мыши, в эти переменные записываются координаты по x и y мыши
            x_mouse,y_mouse=pygame.mouse.get_pos()
            print(f"x={x_mouse} y={y_mouse}")
            column=x_mouse//(margin+width)
            row = y_mouse//(margin+heigth)
            # mas[row][column]=1

            if mas[row][column]==0:
                mas[row][column]=1
            else:
                mas[row][column]=0

#эта операция проходится по ряду и по колонке
#высчитывает координаты по x и y и рисует квадратики

    for row in range(10):
        for col in range(10):

            if mas[row][col]==1:
                color=red
            else:
                color=green

            #считаем х вместе с отступами
            x=col*width+(col+1)*margin
            #1*40+1+1*10
            #считаем положение у вместе с отступами
            y=row*heigth+(row+1)*margin
            pygame.draw.rect(display,color,(x,y,width,heigth))

    pygame.display.update()
    clock.tick(FPS)

