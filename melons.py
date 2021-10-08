"""Classes for melon orders."""
class AbstractMelonOrder():
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0.0

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5 * 1.5   
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order with U S Government """
    passed_inspection = False
    
    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.tax = 0.0
    def mark_inspection(self, passed):
        self.passed_inspection =  passed
        
class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.tax = 0.8

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species,qty)
        self.tax = .17
        self.country_code = country_code
       
    def get_total(self):
        if self.qty < 10:
            return super().get_total() + 3
            
        return super().get_total()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order0 = InternationalMelonOrder("watermelon",6 , "AUS")

x = order0.get_total()
print(x)

order0 = InternationalMelonOrder("watermelon",10, "AUS")
x = order0.get_total()
print(x)
code = order0.get_country_code()
print(f"country code {code}")

order0 = InternationalMelonOrder("watermelon",16,"AUS")
x = order0.get_total()
print(f"International order -- {x:.2f}")
code = order0.get_country_code()
print(f"country code {code}")

order1 = DomesticMelonOrder("cantaloupe",8)
y =  order1.get_total()
print(y)

order2 = GovernmentMelonOrder("watermelon", 10)
order2.mark_inspection(True)
z = order2.get_total()
print(f"Order from government -- ${z}")
