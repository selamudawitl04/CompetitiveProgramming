from decimal import Decimal
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.temp = 0
        
    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.temp+= 1
        total = 0
        for i in range(len(product)):
            # print(self.prices[self.products.index(product[i])])
            total+= self.prices[self.products.index(product[i])] * amount[i]
        if self.temp == self.n:
            total = total * ((100 - self.discount)/100)
            self.temp = 0
        return total
        
        
        
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)