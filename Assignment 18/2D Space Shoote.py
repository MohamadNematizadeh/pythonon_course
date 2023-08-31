import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "2D Space Shoote"
LASER_SPEED = 5

class Bullet(arcade.Sprite):
    def __init__(self, host, a, s):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = s
        self.angle = a
        self.change_x = 0
        self.change_y = 1

    def move(self):
        if self.angle == 90:
            self.center_y += self.speed
        elif self.angle == -90:
            self.center_y -= self.speed

class Spaceship(arcade.Sprite):
    def __init__(self,Game,im=":resources:images/space_shooter/playerShip3_orange.png",y=70,a=0,ba=90):
        super().__init__(im)
        self.ba = ba
        self.center_x = Game.width / 2
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.speed = 4
        self.angle = a
        self.Game_width = Game.width
        self.Bullet_list = []
        self.jons = []

    def update_jon(self,y=25):
        x = 25
        for i in range(3):
            new_jon = Jon(x,y)
            self.jons.append(new_jon)
            x+=30

    def move(self):
        if self.change_x == -1:
            if self.center_x > 20:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.Game_width-20:
                self.center_x += self.speed
                
    def fire(self):
        new_bullet = Bullet(self, self.ba, LASER_SPEED)
        if len(self.Bullet_list) <= 2: 
            self.Bullet_list.append(new_bullet)

class Jon(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(":resources:images/items/gemGreen.png")
        self.center_x = x
        self.center_y = y
        self.width = 50
        self.height = 50

class MyGame(arcade.Window):
    def __init__(self, w, h, t):
        super().__init__(w, h, t)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.player_1 = Spaceship(self)
        self.player_2 = Spaceship(self, ":resources:images/space_shooter/playerShip1_blue.png", SCREEN_HEIGHT-70, 180, -90)
        self.player_1.update_jon()
        self.player_2.update_jon(SCREEN_HEIGHT-25)
        self.s = "s"

    def on_draw(self):
        arcade.start_render()
        
        if self.s == "g":
            self.player_1.draw()
            self.player_2.draw()
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
            for bullet in self.player_1.Bullet_list:
                bullet.draw()
            for bullet in self.player_2.Bullet_list:
                bullet.draw()
            for jon in self.player_1.jons:
                jon.draw()
            for jon in self.player_2.jons:
                jon.draw()

        elif self.s == "s":
            arcade.draw_text("Click a button", SCREEN_WIDTH/3, SCREEN_HEIGHT/2, font_size=15)

        elif self.s == "w_1":
            arcade.draw_text("player_Blue win", SCREEN_WIDTH/3, SCREEN_HEIGHT/2, font_size=15)

        elif self.s == "w_2":
            arcade.draw_text("player_red win", SCREEN_WIDTH/3, SCREEN_HEIGHT/2, font_size=15)

        arcade.finish_render()

    def on_key_release(self, synbol : int, modifiers: int):
        if synbol == arcade.key.A or synbol == arcade.key.D:
            self.player_1.change_x = 0
        if synbol == arcade.key.J or synbol == arcade.key.L:
            self.player_2.change_x = 0

    def on_key_press(self,synbol : int, modifiers: int):
        if self.s == "s":
            self.s = "g"
        
        elif self.s == "g":
            if synbol == arcade.key.A:
                self.player_1.change_x = -1
            elif synbol == arcade.key.D:
                self.player_1.change_x = 1
            elif synbol == arcade.key.SPACE:
                self.player_1.fire()

            if synbol == arcade.key.J:
                self.player_2.change_x = -1
            elif synbol == arcade.key.L:
                self.player_2.change_x = 1
            elif synbol == arcade.key.I:
                self.player_2.fire()
    
    def on_update(self, delta_time):
        if self.s == "g":
            self.player_1.move()
            self.player_2.move()

            for bullet in self.player_1.Bullet_list:
                bullet.move()
            for bullet in self.player_2.Bullet_list:
                bullet.move()

            for bullet in self.player_1.Bullet_list:
                if arcade.check_for_collision(self.player_2, bullet):
                    self.player_1.Bullet_list.remove(bullet)
                    self.player_2.jons.remove(self.player_2.jons[0])
                if bullet.center_y > 600:
                    self.player_1.Bullet_list.remove(bullet)

            for bullet in self.player_2.Bullet_list:
                if arcade.check_for_collision(self.player_1, bullet):
                    self.player_2.Bullet_list.remove(bullet)
                    self.player_1.jons.remove(self.player_1.jons[0])
                if bullet.center_y < 0:
                    self.player_2.Bullet_list.remove(bullet)

        if len(self.player_1.jons) == 0:
            self.s = "w_2"
        elif len(self.player_2.jons) == 0:
            self.s = "w_1"

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.run()

if __name__ == "__main__":
    main()