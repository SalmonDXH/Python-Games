import customtkinter as ctk
import threading
import time

class GenerateDetailWidget(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.pack(fill="y", side="left", padx=5)
        
        self.generate_button = ctk.CTkButton(master=self, width=80, text="Generate", command=self.generate_table)
        self.generate_button.pack(fill="y", side="right", pady=4, padx=2)
        
        self.box_percentage = ctk.CTkEntry(master=self, width=90, placeholder_text="percentage %")
        self.box_percentage.pack(fill="y", side="right", pady=4, padx=4)
        
        self.height_input = ctk.CTkEntry(master=self, width=80, placeholder_text="height")
        self.height_input.pack(fill="y", side="right", pady=4, padx=2)
        
        self.size_label = ctk.CTkLabel(master=self, text="x")
        self.size_label.pack(fill="y",side="right", padx=2)
        
        self.width_input = ctk.CTkEntry(master=self, width=80, placeholder_text="width")
        self.width_input.pack(fill="y", side="right", pady=4, padx=2)
        
        self.seed_id_input = ctk.CTkEntry(master=self, width=80, placeholder_text="seed id")
        self.seed_id_input.pack(fill="y", side="right", pady=4, padx=4)
        
    def generate_table(self):
        percentage = self.box_percentage.get()
        try:
            percentage = float(percentage)
        except ValueError:
            percentage = 50
        
        
        width = self.width_input.get()
        width = int(width) if width != "" and width.isdigit() else 15
        
        height = self.height_input.get()
        height = int(height) if height != "" and height.isdigit()  else 15
        
        seed_id = 0
        
        self.master.generate_table(width,height,percentage,seed_id)

        

class GameStatisticWidget(ctk.CTkFrame):
    time = 0
    
    def __init__(self, master):
        super().__init__(master=master)
        self.pack(fill="x", expand=True,side="left", padx=5)
        
        self.time_label = ctk.CTkLabel(master=self,text="Time: 00:00:00")
        self.time_label.pack(fill="y",side="left",pady=4,padx=2)
        
        threading.Thread(target=self.secondly_change, daemon=True).start()
        
    def change_time(self, time:int = 0):
        self.time = time
    
    def update_time(self):
        hour = self.time // (60*60)
        minute = self.time // (60) % 60
        second = self.time % 60
        def result(time):
            return f"0{time}" if time < 10 else time
        self.time_label.configure(text=f"Time: {result(hour)}:{result(minute)}:{result(second)}")
    
    def secondly_change(self):
        while True:
            time.sleep(1)
            self.time+=1
            self.update_time()
    


class TopNavBar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master,height=60)
        self.pack(fill="x", side="top", padx=5)
        
        ""
       
        self.game_statistic_widget = GameStatisticWidget(master=self)
        self.generate_detail_widget = GenerateDetailWidget(master=self)
        
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        self.master.generate_table(width,height,percentage,seed_id)
        self.game_statistic_widget.change_time(0)
    
        
        