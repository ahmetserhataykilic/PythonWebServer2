import pika, os

from pika import connection

url = os.environ.get('CLOUDAMQP_URL', 'amqp://ahmet:1q2w3e4r@192.168.1.8:5672/')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    print(str(body))

channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True
)

print('Waiting Message: ')

channel.basic_publish(
    body='Hello RabbitMQ',
    exchange='test_exchange',
    routing_key='tests'
)
print('Message sent.')
channel.close()
connection.close()