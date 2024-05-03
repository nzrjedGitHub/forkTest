from pygame import *
#some changes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load('neoncity.jpg'), (win_width, win_height ))

player = Player('f1.png', 600, 40, 10)
monster = Enemy('enemy.png', -40, 400, 1)
final = GameSprite('treasure.png', win_width - 120, 400, 0)
monster2 = GameSprite('remove.png', 470, 120, 4)

w1 = Wall(154, 205, 50, 20, 20, 660, 10)
w2 = Wall(154, 205, 50, 20, 480, 660, 10)
w3 = Wall(154, 205, 50, 20, 20, 10, 360)
w4 = Wall(154, 205, 50, 680, 20, 10, 470)
w5 = Wall(154, 205, 50, 550, 150, 130, 10)
w6 = Wall(154, 205, 50, 170, 150, 300, 10)
w7 = Wall(154, 205, 50, 20, 250, 560, 10)
w8 = Wall(154, 205, 50, 20, 340, 380, 10)
w9 = Wall(154, 205, 50, 500, 340, 180, 10)





# w3 = Wall(154, 205, 50, 350, 250, 350, 10)
# w4= Wall(154, 205,  50, 350, 250,350,10)
# w5= Wall(154, 205,  50, 350, 150,350,10)
# w6 = Wall(205, 154, 50, 350, 250, 350,10)

# написи
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

game = True
finish = False
clock = time.Clock()
FPS = 30

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster.update()


        player.reset()
        monster.reset()
        monster2.reset()
        final.reset()


        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()





    # # Ситуація "Програш"
    # if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3):
    #     finish = True
    #     window.blit(lose, (200, 200))
    #     kick.play()

        # Ситуація "Програш"
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()


    # Ситуація "Перемога"
    if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()


    display.update()
    clock.tick(FPS)
