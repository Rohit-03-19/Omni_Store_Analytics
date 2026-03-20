class BaseItem:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name

class Product(BaseItem):
    """
    Represents a retail product. 
    Uses Inheritance to demonstrate Advanced Python concepts.
    """
    def __init__(self, item_id, name, base_price, category, tags=None):
        super().__init__(item_id, name)
        self.base_price = base_price
        self.category = category
        self.tags = tags or []

    def __repr__(self):
        """Dunder method for professional representation in logs."""
        return f"<Product(ID={self.item_id}, Name='{self.name}', Category='{self.category}')>"

    def calculate_discounted_price(self, discount_rate: float):
        """Applies a discount to the base price."""
        return self.base_price * (1 - discount_rate)