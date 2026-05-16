class ResultModel:
    status:bool
    reason:str
    def __init__(self, status:bool, reason:str):
        self.status = status
        self.reason = reason