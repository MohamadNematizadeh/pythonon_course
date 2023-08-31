import arcade
import random
WIDTH = 600
HEIGHT = 600

arcade.open_window(WIDTH, HEIGHT, "picture")
arcade.set_background_color(arcade.color.BLUE_YONDER)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, WIDTH, HEIGHT / 5, 0, color=arcade.color.JUNGLE_GREEN)
arcade.draw_circle_filled(100, 600 , 100, arcade.color.SUNSET, num_segments=200)
# arcade.draw_circle_filled()
def drawtree(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 40, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x, y +20, 35,  color=arcade.color.DARK_GREEN)
# arcade.draw_arc_outline(70, 500, 20, 20, arcade.color.BLACK, 0, 90)
arcade.draw_arc_outline(470 + 40, 550, 20, 20, arcade.color.BLACK, 90, 180)
arcade.draw_arc_outline(70, 500, 50,50, arcade.color.BLACK, 90, 0)
for i in range(7, WIDTH-7, 65):
    drawtree(random.randrange(i - 25, WIDTH-25), random.randrange(HEIGHT / 5))
arcade.finish_render()
arcade.run()