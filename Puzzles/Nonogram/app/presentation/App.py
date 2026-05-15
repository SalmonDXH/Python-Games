import customtkinter as ctk

from . import widgets as w

from ..application import services

"CONFIGURATION"
NAME    = "Nonogram"
VERSION = "0.0.0"
AUTHOR  = "SALMON"

HEIGHT = 800
WIDTH = 1200

class NonogramApp(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title(f"{NAME} v{VERSION} by {AUTHOR}")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        
        self.top_nav_bar = w.TopNavBar(self)
        self.content_widget = w.ContentWidget(self)
    
    def start(self):
        self.mainloop()
    
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        result = services.game_service.generate_table(width,height,percentage,seed_id)
        print(result)