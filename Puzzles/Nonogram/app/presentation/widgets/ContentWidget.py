import customtkinter as ctk

from ...application import services


class ClueFont(ctk.CTkFont):
    def __init__(self):
        super().__init__(family="Arial",
            size=16,
            weight="bold"
            )

class BoxButton(ctk.CTkButton):
    def __init__(self,master,id:int):
        self.id = id
        super().__init__(master=master, text="",fg_color="#ffffff", command=self.choose)
        self.bind("<Button-3>",command=self.right_click)
    
    def choose(self):
        result = self.master.choose_block(self.id, True)
        if result:
            self.change_status(result.get("flag", False))
    
    def right_click(self, event):
        result = self.master.choose_block(self.id, False)
        if result:
            self.change_status(result.get("flag", False))
    
    def change_status(self, flag:bool):
        fg_color = "green" if flag else "red"
        self.configure(fg_color=fg_color)
    

class ColumnComponent(ctk.CTkFrame):
    def __init__(self,master, ar:list[int]):
        super().__init__(master=master)
        for i in ar[::-1]:
            ctk.CTkLabel(master=self,text=i, font=ClueFont()).pack(side="bottom", fill="x", pady=2)

class RowComponent(ctk.CTkFrame):
    def __init__(self,master, ar:list[int]):
        super().__init__(master=master)
        index=0
        for i in ar[::-1]:
            ctk.CTkLabel(master=self,text=i, font=ClueFont()).pack(side="right", fill="y", padx=5)

class NonogramTable(ctk.CTkFrame):
    def __init__(self,master, table:dict={}):
        super().__init__(master=master)
        for i in range(1, table.get("height", 0)+1):
            self.grid_rowconfigure(i, weight=1)
        for i in range(1, table.get("width", 0)+1):
            self.grid_columnconfigure(i, weight=1)
        id = 0
        for row in range(1, table.get("height", 0)+1):
            for column in range(1, table.get("width", 0)+1):
                BoxButton(master=self, id=id).grid(column=column, row=row, padx=5, pady=1)
                id += 1
        index=1
        for i in table.get("rows",[]):
            RowComponent(self,i).grid(column=0, row=index, sticky="nsew")
            index+=1
        index=1
        for i in table.get("columns",[]):
            ColumnComponent(self,i).grid(column=index, row=0,  sticky="nsew")
            index+=1

        self.pack(fill="both", side="left", expand=True,padx=10)
    
    def choose_block(self, block_id:int, type:bool = None):
        return self.master.choose_block(block_id, type)
    
class TableWidget(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master=master)
        self.pack(fill="both", expand=True,side="bottom")
        self.nonogram_table = None
    
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        if self.nonogram_table and isinstance(self.nonogram_table, NonogramTable):
            self.nonogram_table.destroy()
        result = services.game_service.generate_table(width,height,percentage,seed_id)
        if result:
            self.nonogram_table = NonogramTable(master=self, table=result)
    
    def choose_block(self, block_id:int, type:bool=None):
        return self.master.choose_block(block_id, type)
        

class ContentWidget(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master=master)
        self.pack(fill="both", expand=True,side="bottom", pady=5, padx=5)
        
        self.table_widget = TableWidget(self)
    
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        self.table_widget.generate_table(width,height,percentage,seed_id)
    
    def choose_block(self, block_id:int, type:bool=None):
        return self.master.choose_block(block_id, type)
        