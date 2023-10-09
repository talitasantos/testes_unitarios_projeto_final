from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            #BUG: não estava retornando nada
            # print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            # for flavor in self.flavors:
            #     print(f"\t-{flavor}")
            answer = 'No momento temos os seguintes sabores de sorvete disponíveis:'
            for flavor in self.flavors:
                answer += f'\n\t-{flavor}'
            return answer
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                #BUG: precisa retornar o sabor e nao a lista de sabores
                #  print(f"Temos no momento {self.flavors}!")
                return f"Temos no momento {flavor}!"
            else:
                #BUG: precisa retornar o sabor e nao a lista de sabores
                return f"Não temos no momento {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                return "\nSabor já disponivel!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!"
