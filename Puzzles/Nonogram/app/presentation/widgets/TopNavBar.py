import customtkinter as ctk

class TopNavBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,height=60)
        self.pack(fill="x", side="top")
        
        