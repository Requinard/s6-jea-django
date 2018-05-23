import pika
import kwetter.settings as settings

KWEET_EXCHANGE="KWEETS"
NEW_KWEET_ROUTE="NEW_KWEET"
LIKE_KWEET_ROUTE="LIKE_KWEET"


class Messaging:
    host = "localhost"

    def __init__(
            self,
            user="rabbit",
            password="rabbit",
            vhost="/"
    ):
        if settings.DEBUG is not True:
            self.host = "stats"

        self.user = user
        self.password = password
        self.vhost = vhost

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            'localhost',
            credentials=pika.PlainCredentials(
                self.user,
                self.password
            ),
            vhost=self.vhost
        ))

        channel = self.connection.channel()
        self.channel = channel

        channel.exchange_declare(
            exchange=KWEET_EXCHANGE,
            exchange_type='topic',
        )

    def send_kweet(self, kweet_string):
        self.channel.basic_publish(
            exchange=KWEET_EXCHANGE,
            routing_key=NEW_KWEET_ROUTE,
            body=kweet_string
        )

    def send_kweet_like(self, kweet_string):
        self.channel.basic_publish(
            exchange=KWEET_EXCHANGE,
            routing_key=NEW_KWEET_ROUTE,
            body=kweet_string
        )