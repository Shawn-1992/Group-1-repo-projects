# Class that could potentially connect to a database to assign product cost.
# Since there is no database, mock values are used to assign the costs.
class ProductDatabase:
    def __init__(self) -> None:
        self.cost_map = {
            "product1": 1.0,
            "product2": 2.0
        }

    def get(self, product: str) -> float:
        return self.cost_map.get(product, 0.0)
