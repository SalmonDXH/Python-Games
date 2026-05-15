class BlockModel:
    flag = False
    def __init__(self, flag:bool=False):
        self.flag = flag

class SeedTemplateModel():
    id:int = 0
    table:list[list[BlockModel]] = []
    def __init__(self, id:int, table:list[list[BlockModel]]):
        self.id = id
        self.table = table

class BlockPresentationModel:
    block : BlockModel
    select : bool = False
    def __init__(self, block:BlockModel=BlockModel()):
        self.block = block