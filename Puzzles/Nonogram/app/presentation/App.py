import customtkinter as ctk

from . import widgets as w

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
    
    def start(self):
        self.mainloop()