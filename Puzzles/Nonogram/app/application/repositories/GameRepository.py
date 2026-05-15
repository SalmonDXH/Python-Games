from ...domain.models import (BlockModel, BlockPresentationModel, TableModel)
import math
import random

class GameRepository:
    current_table : TableModel = None
    def __init__(self):
        pass
    
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        total_blocks = width*height
        total_black_block = int(math.ceil(total_blocks/100*percentage))
        table_list:list[BlockPresentationModel] = []
        for i in range(total_blocks):
            if total_black_block:
                if total_black_block >= random.randint(1, total_blocks+1):
                    table_list.append(BlockPresentationModel(BlockModel(True)))
                    total_black_block -= 1
                    continue
            table_list.append(BlockPresentationModel())
        self.current_table = TableModel(width=width, height=height,blocks=table_list)
        return self._count_black_blocks()
        
        
    def _count_black_blocks(self):
        if self.current_table:
            rows:list[list[int]] = []
            columns: list[list[int]] = []
            width = self.current_table.width
            height = self.current_table.height
            for i in range(len(self.current_table.blocks)):
                columns_index = i % width
                rows_index = i % height
                if len(columns) < columns_index + 1:
                    columns.append([0])
                if len(rows) < rows_index + 1:
                    rows.append([0])
                if self.current_table.blocks[i].block.flag:
                    rows[rows_index][-1]  += 1
                    columns[columns_index][-1] += 1
                else:
                    if rows[rows_index][-1]:
                        rows[rows_index].append(0)
                    if columns[columns_index][-1]:
                        columns[columns_index].append(0)
            for ar in rows:
                if not ar[-1]:
                    ar.pop()
            for ar in columns:
                if not ar[-1]:
                    ar.pop()
            return {
                "rows": rows,
                "columns": columns,
                "height": self.current_table.height,
                "width": self.current_table.width
            }
        return False