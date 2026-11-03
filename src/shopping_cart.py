class Product:
    def __init__(self, id: str, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount = 0.0

    def add_item(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")
        
        current_in_cart = self.items.get(product.id, {}).get("quantity", 0)
        total_requested = current_in_cart + quantity
        
        if total_requested > product.stock:
            raise ValueError("Превышено доступное количество на складе")
        
        if product.id in self.items:
            self.items[product.id]["quantity"] = total_requested
        else:
            self.items[product.id] = {
                "product": product,
                "quantity": quantity
            }

    def remove_item(self, product_id: str, quantity: int = None):
        if product_id not in self.items:
            return
        
        if quantity is None or quantity >= self.items[product_id]["quantity"]:
            del self.items[product_id]
        else:
            self.items[product_id]["quantity"] -= quantity

    def apply_promo(self, code: str):
        if code == "DISCOUNT10":
            self.discount = 0.10
        elif code == "DISCOUNT20":
            self.discount = 0.20
        else:
            raise ValueError("Неверный промокод")

    def get_total_price(self) -> float:
        total = sum(item["product"].price * item["quantity"] for item in self.items.values())
        return total * (1.0 - self.discount)