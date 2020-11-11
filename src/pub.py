class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self._age_limit = 18

    def drink_exists(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return True 
        return False

    def cost_of_drink(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink.price
            

    def sell_the_drink(self, drink_name, customer):
        #check the drink exists
        #if drink exists - can customer afford it 
        drink_check = self.drink_exists(drink_name)
        if customer.age >= self._age_limit and drink_check and self.cost_of_drink(drink_name) <= customer.wallet:
        #reduce customer wallet 
            customer.wallet -= self.cost_of_drink(drink_name)
        # increase pub cash/total
            self.till += self.cost_of_drink(drink_name)
        
    