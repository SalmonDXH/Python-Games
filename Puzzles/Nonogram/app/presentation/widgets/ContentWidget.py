import customtkinter as ctk


class NonogramTable(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master=master)

class TableWidget(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master=master)
        self.pack(fill="both", expand=True,side="bottom")

class ContentWidget(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master=master)
        self.pack(fill="both", expand=True,side="bottom", pady=5, padx=5)
        
        self.table_widget = TableWidget(self)
        