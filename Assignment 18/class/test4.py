import arcade

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Night Nature Scene"

# Set up the colors
BLACK = (0, 0, 0)
DARK_BLUE = (10, 10, 50)
DARK_GREEN = (0, 30, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

class NightNatureWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(BLACK)

    def on_draw(self):
        arcade.start_render()

        # Draw the background
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4, SCREEN_WIDTH, SCREEN_HEIGHT // 2, DARK_BLUE)
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 3 // 4, SCREEN_WIDTH, SCREEN_HEIGHT // 2, DARK_GREEN)

        # Draw the moon
        arcade.draw_circle_filled(700, 100, 50, YELLOW)

        # Draw stars
        star_positions = [(150, 150), (300, 200), (500, 100), (600, 300), (100, 400)]
        for pos in star_positions:
            arcade.draw_circle_filled(pos[0], pos[1], 3, WHITE)

def main():
    window = NightNatureWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
