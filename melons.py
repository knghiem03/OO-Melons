"""Classes for melon orders."""
class AbstractMelonOrder():
    """A melon order within the USA."""

    def __init__(self, species, qty, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    def __init__(self, species, qty, tax):
        """Initialize melon order attributes."""
        super().__init__(species, qty, tax)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"

    def __init__(self, species, qty, tax, country_code):
        """Initialize melon order attributes."""
        super().__init__(species,qty, tax)
        
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


order0 = InternationalMelonOrder("watermelon",6, .17, "AUS")
x = order0.get_total()
print(x)
code = order0.get_country_code()
print(f"country code {code}")

order1 = DomesticMelonOrder("cantaloupe",8 , .08)
y =  order1.get_total()
print(y)
