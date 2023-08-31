import arcade
SCRE_WHTE = 800
SCRE_HAT = 600
SCRE_TITEL ="Spel window"
arcade.open_window(SCRE_WHTE,SCRE_HAT,SCRE_TITEL)
class My_gam(arcade.Window):
    def __init__ (self,w,h,t):
        super().__init__(w,h,t)
        arcade.set_background_color(arcade.color.BLACK)
    def setup(self):
        pass
    def on_draw(self):
        arcade.start_render()
    def update(self):
        pass
gam = My_gam(SCRE_HAT,SCRE_WHTE,SCRE_TITEL)
gam.setup()
arcade.run()

 