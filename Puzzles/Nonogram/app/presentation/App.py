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
        self.content_widget.generate_table(width,height,percentage,seed_id)
    
    def choose_block(self, block_id:int, type:bool=None):
        if type is not None:
            result = services.game_service.choose_block(block_id=block_id, type=type)
            
            return result