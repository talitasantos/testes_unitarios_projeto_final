from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        # Setup
        restaurant = Restaurant('Lago Sul', 'churrasco')
        restaurant.open_restaurant()
        resposta_esperada = f"Esse restaurante chama Lago Sul e serve churrasco\n Esse restaurante está servindo 0 consumidores desde que está aberto"

        # Chamada
        resposta = restaurant.describe_restaurant()

        # Avaliação
        assert resposta_esperada == resposta

    def test_open_restaurant(self):
        # Setup
        restaurant = Restaurant('Lago Sul', 'churrascaria')
        resposta_esperada = "Lago Sul agora está aberto!"

        # Chamada
        resposta = restaurant.open_restaurant()

        # Avaliação
        assert resposta_esperada == resposta

        resposta_esperada = "Lago Sul já está aberto!"
        # Chamada
        resposta = restaurant.open_restaurant()

        # Avaliação
        assert resposta_esperada == resposta

    def test_close_restaurant(self):
        # Setup
        restaurant = Restaurant('Lago Sul', 'churrascaria')
        resposta_esperada = "Lago Sul já está fechado!"

        # Chamada
        resposta = restaurant.close_restaurant()

        # Avaliação
        assert resposta_esperada == resposta

        # Setup
        resposta_esperada = "Lago Sul agora está fechado!"
        restaurant.open_restaurant()

        # Chamada
        resposta = restaurant.close_restaurant()

        # Avaliação
        assert resposta_esperada == resposta

    def test_set_number_served(self):
        # Setup
        restaurant = Restaurant('Lago Sul', 'churrasco')
        resposta_esperada = f"Lago Sul está fechado!"

        # Chamada
        resposta = restaurant.set_number_served(0)

        # Avaliação
        assert resposta_esperada == resposta

        # Setup
        restaurant.open_restaurant()
        number_served_esperado = 2

        # Chamada
        restaurant.set_number_served(number_served_esperado)

        # Avaliação
        assert restaurant.number_served == number_served_esperado

    def test_increment_number_served(self):
        # Setup
        restaurant = Restaurant('Lago Sul', 'churrasco')
        resposta_esperada = f"Lago Sul está fechado!"

        # Chamada
        resposta = restaurant.increment_number_served(2)

        # Avaliação
        assert resposta_esperada == resposta

        # Setup
        restaurant.open_restaurant()
        restaurant.set_number_served(10)
        number_served_esperado = 12

        # Chamada
        restaurant.increment_number_served(2)

        # Avaliação
        assert restaurant.number_served == number_served_esperado
