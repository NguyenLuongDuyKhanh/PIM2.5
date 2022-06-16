import pygame
import random
from pygame.locals import(
    QUIT,
    KEYDOWN,
    K_UP
)

pygame.init()

screen = pygame.display.set_mode((800,600))
bg_screen = pygame.image.load("bg_FB.png")

pygame.display.set_caption('Flappy Bird')
#tocdo = input("Tốc độ bạn muốn là :")
class Bird:
    def __init__(self):
        self.x = 200
        self.y = 200
        pygame.draw.circle(screen, 'red',(self.x,self.y),10)
    
    def update(self):
        global is_end
        key_pressed = pygame.key.get_pressed()
        if self.y >=580:
            is_end = True
        else:
            if key_pressed[pygame.K_SPACE]:
                self.y = self.y - 2
            else:
                self.y = self.y + 2
        pygame.draw.circle(screen, 'red',(self.x,self.y),10)

    def print_toado(self):
        print(self.x,self.y)

class Pipe:
    def __init__(self):
        self.x = 500
        self.y = 0
        self.height = random.randint(100,350)
        self.space = 100
        pygame.draw.rect(screen, "green", (self.x,self.y,20,self.height))
        pygame.draw.rect(screen, "green", (self.x,self.space+self.height,20,600-self.space-self.height))

    def update(self):
        self.x -= 3
        pygame.draw.rect(screen, "green", (self.x,self.y,20,self.height))
        pygame.draw.rect(screen, "green", (self.x,self.space+self.height,20,600-self.space-self.height))
    


running = True
clock = pygame.time.Clock()
bird = Bird()
pygame.display.flip()
is_end = False
pipe_spawm_time = 0
pipes = []
point = 0

font_big = pygame.font.SysFont("couriernew",48, bold = True)
font_small = pygame.font.SysFont("couriernew",28 , bold = True)
kieu_chu = pygame.font.SysFont('calibri', 20, bold = False, italic = False)
print_point = kieu_chu.render("Số điểm là :" + str(point),True,"White","Red") 

begin = True
pygame.time.set_timer(pygame.USEREVENT+1,1000)
counter = 5
countdown_text = font_big.render(str(counter),True, "white")

while running:
    
    clock.tick(45)
    screen.fill((0,0,0))
    #screen.blit(bg_screen,(0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break
        elif event.type == pygame.USEREVENT +1:
            counter -=1
            if counter == 0:
                countdown_text = font_big.render("Start!", True, "white")
            elif counter <0:
                pygame.time.set_timer(pygame.USEREVENT+1,0)
                begin = False
            else:
                countdown_text = font_big.render(str(counter), True, "white")
        elif event.type == KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("da bam")
                is_end == False
                point = 0
                bird.__init__()
                pipes = []
    if begin:
        screen.blit(countdown_text,(230,220))
    else:
        if is_end == True:
            game_over_text = font_big.render("Game over", True, "white", "red")
            reset_text = font_small.render("Press Enter to restart", True, "white", "red")
            screen.blit(game_over_text,(120,210))
            screen.blit(reset_text,(70,270))
            screen.blit(print_point,(0,0))
            #break
        else:
            bird.update()
            current_time = pygame.time.get_ticks()      
            if current_time > (pipe_spawm_time  + random.randint(1000,8000)):
                new_pipe = Pipe()
                pipes.append(new_pipe)
                pipe_spawm_time = current_time

            for pipe in pipes:
                pipe.update()
                if pipe.x < -20:
                    pipes.remove(pipe)

                if (bird.x + 10 >= pipe.x and bird.x-10 <= pipe.x+20)  and (bird.y + 10 >= pipe.space + pipe.height or bird.y - 10 <= pipe.height ):
                    is_end = True
                    break
                if bird.x - 10 >=  pipe.x  and bird.x + 10 <= pipe.x + 20:
                    point += 1

                    #print(point)                       
                screen.blit(print_point,(0,0))
                
        
                
        
    pygame.display.flip()
    
pygame.quit()        