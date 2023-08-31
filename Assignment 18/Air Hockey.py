import random
import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Air Hockey"

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color = arcade.color.YELLOW
        self.radius = 15
        self.change_x = random.choice([1,-1])
        self.change_y = random.choice([1,-1])
        self.speed = 4
        self.width = self.radius * 2
        self.height = self.radius * 2
    
    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, self.color)

class Rocket(arcade.Sprite):
    def __init__(self,x,y,c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.color = c
        self.change_x = 0
        self.change_y = 0
        self.width = 80
        self.height = 5
        self.speed = 3
        self.score = 0

    def move(self,ball,game):
        if ball.center_y > game.height//2:

            if self.center_x > ball.center_x:
                self.change_x = -1

            if self.center_x < ball.center_x:
                self.change_x = +1

            self.center_x += self.change_x * self.speed

            if self.center_x < 60:
                self.center_x = 60

            if self.center_x > game.width - 60:
                self.center_x = game.width - 60

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

class MyGame(arcade.Window):
    def __init__(self, w, h, t):
        super().__init__(w, h, t)
        arcade.set_background_color(arcade.color.BLACK)
        self.player_1 = Rocket(SCREEN_WIDTH/2, SCREEN_HEIGHT-20,arcade.color.RED)
        self.player_2 = Rocket(SCREEN_WIDTH/2, 20, arcade.color.BLUE)
        self.ball = Ball(self)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_line(15, SCREEN_HEIGHT/2, SCREEN_WIDTH-15, SCREEN_HEIGHT/2, arcade.color.WHITE)
        arcade.draw_rectangle_outline(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 ,SCREEN_WIDTH-30, SCREEN_HEIGHT-30, arcade.color.WHITE)
        self.player_1.draw() 
        self.player_2.draw()
        self.ball.draw()
        arcade.draw_text("Score: ", 40, 590,font_size=10)
        arcade.draw_text(self.player_1.score, 90, 590,font_size=10)
        arcade.draw_text("Score: ", 310, 4,font_size=10)
        arcade.draw_text(self.player_2.score, 360, 4,font_size=10)

        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        if self.player_2.width < x < self.width-self.player_2.width:
            self.player_2.center_x = x   

    def on_update(self, delta_time):
        self.ball.move()
        self.player_1.move(self.ball,self)

        if self.ball.center_x < 30 or self.ball.center_x > self.width - 20:
            self.ball.change_x *= -1
        
        if arcade.check_for_collision(self.player_1, self.ball) or arcade.check_for_collision(self.player_2, self.ball):
            self.ball.change_y *= -1

        if self.ball.center_y < 0:
            self.player_1.score += 1
            del self.ball
            self.ball = Ball(self)
            self.ball.speed += 1

        if self.ball.center_y > self.height:
            self.player_2.score += 1
            del self.ball
            self.ball = Ball(self)
            self.ball.speed += 1

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.run()

if __name__ == "__main__":
    main()