# Class that could potentially connect to a database to assign product cost.
# Since there is no database, mock values are used to assign the costs.
class ProductDatabase:
    def __init__(self) -> None:
        pass

    def get(self, product: str) -> float:
        pass
