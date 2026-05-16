from ...domain.models import (BlockModel, BlockPresentationModel, TableModel, ResultModel)
import math
import random

class GameRepository:
    current_table : TableModel = None
    heart : int = 3
    def __init__(self):
        pass

    def choose_block(self, block_id:int, type:bool):
        if self.current_table:
            block = self.current_table.blocks[block_id]
            if block.select:
                return None
            block.select = True
            flag_result = True
            if block.block.flag != type:
                flag_result = False
                self.heart -= 1
            if block.block.flag:
                self.current_table.black_blocks-=1

            result = {
                "flag": block.block.flag,
                "heart": self.heart,
                "result": flag_result,
            }

            status = "not finish"
            if not self.heart:
                result["status"] = ResultModel(False, "No more life left")
            elif not self.current_table.black_blocks:
                result["status"] = ResultModel(True, "Finish everything")

            return result
        else:
            return None
    
    def generate_table(self, width:int, height:int, percentage:float,seed_id:int=None):
        total_blocks = width*height
        total_black_block = int(math.ceil(total_blocks/100*percentage))
        save_total_black_block = total_black_block
        table_list:list[BlockPresentationModel] = []
        for i in range(total_blocks):
            if total_black_block:
                if total_black_block >= random.randint(1, total_blocks+1):
                    table_list.append(BlockPresentationModel(BlockModel(True)))
                    total_black_block-=1
                    total_blocks-=1
                    continue
            total_blocks -= 1
            table_list.append(BlockPresentationModel())
        self.current_table = TableModel(width=width, height=height,blocks=table_list, black_blocks=save_total_black_block)
        self.heart = 3
        return self._count_black_blocks()
        
        
    def _count_black_blocks(self):
        if self.current_table:
            rows:list[list[int]] = []
            columns: list[list[int]] = []
            width = self.current_table.width
            height = self.current_table.height
            for i in range(len(self.current_table.blocks)):
                columns_index = i % width
                rows_index = i // height
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
            
            max_rows = 0
            max_columns = 0
            for ar in rows:
                if not ar[-1] and len(ar) > 1:
                    ar.pop()
                n = len(ar)
                max_rows = n if n > max_rows else max_rows
            for ar in columns:
                if not ar[-1] and len(ar) > 1:
                    ar.pop()
                max_columns = n if n > max_columns else max_columns
            return {
                "rows": rows,
                "columns": columns,
                "height": self.current_table.height,
                "width": self.current_table.width,
                "max_rows": max_rows,
                "max_columns": max_columns
            }
        return False