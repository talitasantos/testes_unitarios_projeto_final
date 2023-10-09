class Restaurant:
    """Model de restaurante simples."""

    #BUG: number_served e open nao foram passados como parametros no construtor
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        # BUG:
        #print(f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}.")
        # print(f"Esse restaturante chama {self.restaurant_name} e serve {self.cuisine_type}.")
        # print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")

        """Imprima uma descrição detalhada da instância do restaurante."""
        description = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}\n Esse restaurante está servindo {self.number_served} consumidores desde que está aberto"
        return description

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            #BUG: não é necessário definir self.open como False novamente, já que estamos abrindo o restaurante.
            #self.open = False
            self.open = True
            #BUG: para validar se o restaurante está aberto, número de serviço deve começa com 0
            #self.number_served = -2
            self.number_served = 0
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if self.open:
            self.number_served = total_customers
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            #BUG: nao estava incrementando
            #self.number_served = more_customers
            self.number_served += more_customers
        else:
            return f"{self.restaurant_name} está fechado!"
