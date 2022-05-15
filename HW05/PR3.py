import time
import tqdm


class MenuAM:
    def __init__(self):
        self.delivery = DeliveryMan()
        self.dispatcher = Dispatcher()
        self.restaurant = Restaurant()
        self.review = Review()

    def order(self, street_address, restaurant_name):
        self.restaurant.name = restaurant_name
        self.dispatcher.receive_order()
        self.restaurant.make_food()
        self.delivery.deliver(street_address, restaurant_name)
        for _ in tqdm.tqdm(range(60), desc="Your order is delivering"):
            time.sleep(1 / 60)
        self.delivery.order_delivered(street_address)
        time.sleep(2)
        self.review.leave_review()

        return f"Your order will be delivered in address: {street_address}"


class DeliveryMan:

    @staticmethod
    def deliver(street_address, restaurant):
        print(f"Food on it's way from {restaurant} to {street_address}")

    @staticmethod
    def order_delivered(street_address):
        print(f"Order is in {street_address}")


class Dispatcher:

    @staticmethod
    def receive_order():
        print("Order received")


class Restaurant:

    def __init__(self, name="None"):
        self.name = name

    def make_food(self):
        print(f"Food is cooking in {self.name}")


class Review:
    @staticmethod
    def leave_review():
        print("Did you like the food? Live review at our webpage: Example.com")


def client_code(restaurant_name, street_address):
    operator = MenuAM()
    operator.order(street_address, restaurant_name)


if __name__ == "__main__":
    client_code("Subtitles", "Alek Manukyan 1")
