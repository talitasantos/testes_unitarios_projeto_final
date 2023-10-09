from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', ['morango', 'uva', 'chocolate', 'coco'])
        resposta_esperada = 'No momento temos os seguintes sabores de sorvete disponíveis:'
        for flavor in iceCream.flavors:
            resposta_esperada += f'\n\t-{flavor}'

        # Chamada
        resposta = iceCream.flavors_available()

        # Avaliação
        assert resposta_esperada == resposta

    def test_flavors_unavailable(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', [])
        resposta_esperada = "Estamos sem estoque atualmente!"

        # Chamada
        resposta = iceCream.flavors_available()

        # Avaliação
        assert resposta_esperada == resposta

    def test_find_flavor(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', ['morango', 'uva', 'chocolate', 'coco'])
        flavor = 'morango'
        resposta_esperada = f"Temos no momento {flavor}!"

        # Chamada
        resposta = iceCream.find_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta

    def test_find_flavor(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', ['morango', 'uva', 'chocolate', 'coco'])
        flavor = 'morango'
        resposta_esperada = f"Temos no momento {flavor}!"

        # Chamada
        resposta = iceCream.find_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta

    def test_not_found_flavor(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', ['morango', 'uva', 'chocolate', 'coco'])
        flavor = 'milho'
        resposta_esperada = f"Não temos no momento {flavor}!"

        # Chamada
        resposta = iceCream.find_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta

    def test_fnd_flavor_without_stock(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', None)
        flavor = 'milho'
        resposta_esperada = "Estamos sem estoque atualmente!"

        # Chamada
        resposta = iceCream.find_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta

    def test_add_flavor(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', ['morango', 'uva', 'chocolate', 'coco'])
        flavor = 'milho'
        resposta_esperada = f"{flavor} adicionado ao estoque!"

        # Chamada
        resposta = iceCream.add_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta


    def test_add_exists_flavor(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', ['morango', 'uva', 'chocolate', 'coco'])
        flavor = 'uva'
        resposta_esperada = "\nSabor já disponivel!"

        # Chamada
        resposta = iceCream.add_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta

    def test_add_flavor_without_stock(self):
        # Setup
        iceCream = IceCreamStand('Sorvete Petrópolis', 'sorveteria', None)
        flavor = 'uva'
        resposta_esperada = "Estamos sem estoque atualmente!"

        # Chamada
        resposta = iceCream.add_flavor(flavor)

        # Avaliação
        assert resposta_esperada == resposta
