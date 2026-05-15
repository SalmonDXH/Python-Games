from ..repositories.GameRepository import GameRepository


class GameService:
    _gr:GameRepository
    
    def __init__(self):
        self._gr = GameRepository()
        
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        return self._gr.generate_table(width,height,percentage,seed_id)
    
    def choose_block(self, block_id:int, type:bool):
        pass
    
    def get_table(self):
        pass