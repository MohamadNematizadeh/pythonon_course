import arcade 
import random
SCRE_WHTE = 600
SCRE_HAT = 600
arcade.open_window(SCRE_WHTE,SCRE_HAT,"Sekeran")
arcade.set_background_color(arcade.color.BLUE_GREEN)

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0,SCRE_WHTE,SCRE_HAT /3 ,0 ,arcade.color.MSU_GREEN)
arcade.draw_circle_filled(400,SCRE_WHTE - 50, 75 , arcade.color.SUNGLOW)

def daraw_tree(x,y):
    arcade.draw_rectangle_filled(x,x + 20 ,y + 60,y,arcade.color.BROWN_NOSE)
    arcade.draw_circle_outline(x+10,y+80,30,arcade.color.BABY_BLUE)

for i in range(25,SCRE_WHTE-25,70):
    x = random.randrange(i - 25,i+25)
    y = random.randrange(SCRE_HAT/3)
    daraw_tree(x,y)

arcade.finish_render()
arcade.run() 