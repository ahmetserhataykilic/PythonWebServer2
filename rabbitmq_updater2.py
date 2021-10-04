import puka
import time
body = "hello"
# declare send and receive clients, both connecting to the same server on local
# machine
producer = puka.Client("amqp://ahmet:1q2w3e4r@192.168.1.8:5672/")
consumer = puka.Client("amqp://ahmet:1q2w3e4r@192.168.1.8:5672/")

# connect sending party
send_promise = producer.connect()
producer.wait(send_promise)

# connect receiving party
receive_promise = consumer.connect()
consumer.wait(receive_promise)

# declare queue (queue must exist before it is being used - otherwise messages
# sent to that queue will be discarded)
send_promise = producer.queue_declare(queue='mqtt',durable=True,auto_delete=False)
producer.wait(send_promise)

bind_promise = consumer.queue_bind(exchange='amq.topic', queue='mqtt', routing_key='webserver')
consumer.wait(bind_promise)

index = "mqtt"
headers = {"reply_to": 'webserver' }
receive_promise = consumer.basic_consume(queue='mqtt')

send_promise = producer.basic_publish(exchange='amq.topic', routing_key=index, body=body)
producer.wait(send_promise)
          
received_message = consumer.wait(receive_promise, timeout=3)
if not received_message:
    exit 
else:
    consumer.basic_ack(received_message)
    #print("GOT: %r" %
    #(received_message['body'],))
    if "success" in received_message['body']:
        print("count %d , NasID:%s updated successfuly.." % (count,value))
        time.sleep(5)