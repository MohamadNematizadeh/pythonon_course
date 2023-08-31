import random
import arcade

class Apple(arcade.Sprite):
    def __init__ (self,width,height):
        super().__init__("img/apple.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Poop(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__("img/poop.jpg")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Pear(arcade.Sprite):
    def __init__(self,width,height):
        super().__init__("img/pear.png")
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, width - 10)
        self.center_y = random.randint(10, height - 10)
        self.change_x = 0
        self.change_y = 0

class Snake(arcade.Sprite):
    def __init__(self,Game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.radians = 10
        self.center_x = Game.width // 2
        self.center_y = Game.height // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 2
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radians,self.color)
        arcade.draw_text("Score", 350, 25, arcade.color.BLACK, 20)
        arcade.draw_text(self.score, 430, 23, arcade.color.BLACK, 20)

        a = 1
        for part in self.body:
            if a % 2 == 0:
                arcade.draw_circle_filled(part["x"], part["y"],self.radians , arcade.color.BLACK)
                a+=1
            else:
                arcade.draw_circle_filled(part["x"], part["y"],self.radians , arcade.color.YELLOW)
                a+=1

    def move(self):
        self.body.append({"x":self.center_x,"y":self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def apple_eat(self):
        self.score += 1

    def Poop_eat(self):
        self.score -= 1

    def pear_eat(self):
        self.score += 2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Python Snake")
        arcade.set_background_color(arcade.color.KHAKI)
        
        self.snake = Snake(self)
        self.apple_food = Apple(self.width,self.height)
        self.Poop = Poop(self.width,self.height)
        self.pear_food = Pear(self.width,self.height)

        self.a = 1
        self.s = "g"

    def on_draw(self):
        arcade.start_render()

        if self.s == "g":
            self.snake.draw()
            self.apple_food.draw()    
            self.Poop.draw()
            self.pear_food.draw()
            arcade.draw_line(2, 2, 0, 500, arcade.color.WHITE, 5)
            arcade.draw_line(2, 2, 500, 0, arcade.color.WHITE, 5)
            arcade.draw_line(498, 498, 500, 0, arcade.color.WHITE, 5)
            arcade.draw_line(498, 498, 0, 500, arcade.color.WHITE, 5)

        elif self.s == "o":
            arcade.draw_text("Game Over", self.width/3, self.height/2, font_size=25)

        arcade.finish_render()

    def on_update(self, delta_time):
        if self.s == "g":
            self.snake.move()
            
            if self.snake.center_x < 2 or self.snake.center_y < 2 or self.snake.center_x > 498 or self.snake.center_y > 498:
                self.s = "o"

            for part in self.snake.body[1:]:
                if self.snake.body[0] == part:
                    self.s = "o"

            if arcade.check_for_collision(self.snake, self.apple_food):
                del self.apple_food
                self.snake.apple_eat()
                self.apple_food = Apple(self.width,self.height)

            elif arcade.check_for_collision(self.snake, self.Poop):
                if len(self.snake.body) == 1 or len(self.snake.body) == 0:
                    self.s = "o"

                del self.Poop
                self.snake.Poop_eat()
                self.Poop = Poop(self.width,self.height)

            elif arcade.check_for_collision(self.snake, self.pear_food):
                del self.pear_food
                self.snake.pear_eat()
                self.pear_food = Pear(self.width,self.height)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        if symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()