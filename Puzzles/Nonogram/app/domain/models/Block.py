class BlockModel:
    flag = False
    def __init__(self, flag:bool=False):
        self.flag = flag


class BlockPresentationModel:
    block : BlockModel
    select : bool = False
    def __init__(self, block:BlockModel=BlockModel()):
        self.block = block

class TableModel:
    blocks:list[BlockPresentationModel]
    height:int
    width:int
    def __init__(self, width:int, height:int, blocks:list[BlockPresentationModel]):
        self.blocks = blocks
        self.height = height
        self.width = width