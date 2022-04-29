import pygame
from sys import exit


#проверяет все возможные варианты выигрыша игрока
def win(mas,sign):
    zeroes=0
    #проходимя по рядам в массиве
    for row in mas:
        #считаем нули в ряду
        zeroes+=row.count(0)
        #считаем занки в ряду(или х или о),если знаков в ряду три,то возвращаем сам знак
        if row.count(sign)==3:
            return f"победа {sign}"
    #проверяем колонки (у)
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign :
            return f"победа {sign}"
    for col in range(3):
        if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
            return f"победа {sign}"
    for col in range(3):
        if mas[2][0] == sign and mas[1][1] == sign and mas[0][2] == sign:
            return f"победа {sign}"
    #если не сработала ни одна из комбинаций победы
    #если ни в одном ряду не осталось ни одного нуля (хотя до этого массив был заполнен нулями),
    #то выводим ничью
    if zeroes==0:
        return "ничья"
    return False

pygame.init()

green=(34, 139, 34, 255)
blue=(0, 0, 139, 255)
red=(238, 44, 44, 255)
white=(255,255,255)
black=(0,0,0)


FPS=60
clock=pygame.time.Clock()


block=100
margin=15

width=heigth=block*3+margin*4
display = pygame.display.set_mode((width,heigth))

mas=[[0]*3 for i in range(3)]#двумерный массив заполенный нулями

query=0 #эту переменную мы будем постепенно увеличивать на 1

game_over=False

while True:
    #Ждем события (действия пользователя)
    for event in pygame.event.get():
        #если нажали на крестик то закрываем окно
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse,y_mouse=pygame.mouse.get_pos()
            col = x_mouse//(block+margin)
            row = y_mouse//(block+margin)
            if mas[row][col]==0:
                if query%2==0:
                    mas[row][col]="x"
                else:
                    mas[row][col]="o"
                query+=1

        elif event.type== pygame.KEYDOWN and event.key== pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query=0
            display.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col]=="x":
                    color=red
                elif mas[row][col]=="o":
                    color=green
                else:
                    color = white
                #находим координаты левого верхнего угла для текущего квадратика
                x=col*block+(col+1)*margin
                y = row * block + (row + 1) * margin
                pygame.draw.rect(display,color,(x,y,block,block))
                if color==red:
                    #отрисовка линии у крестика
                    pygame.draw.line(display, white,(x, y), (x+block, y+block), 3)
                    pygame.draw.line(display, white, (x+block, y), (x, y+block), 3)
                elif color==green:
                    pygame.draw.circle(display,white,(x+block//2,y+block//2),block//2,3)

    if (query-1)%2==0:
        game_over=win(mas,"x")
    else:
        game_over=win(mas,"o")

    if game_over:
        #если случился конец игры,то :
        #закрашиваем экран чёрным
        display.fill(black)
        #задаём шрифт "stxingkai" и его толщина 80
        shrift=pygame.font.SysFont("stxingkai",80)
        #текст будет отображат текст из функции game_over белым цветом
        text1=shrift.render(game_over,True,white)
        #узанём его координаты
        txt_rect=text1.get_rect()
        # эти 2 строчки находят центр экрана
        txt_x=display.get_width()/2-txt_rect.width/2
        txt_y = display.get_height() / 2 - txt_rect.height / 2
        #прикрепляет текст по найденным координатам
        display.blit(text1,[txt_x,txt_y])

    pygame.display.update()
    clock.tick(FPS)
