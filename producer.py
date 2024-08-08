import pika, json

params = pika.URLParameters('amqps://qkafgowp:5uA-eP_wynCcX3nZwrh_0t3_DGcN3Kus@rat.rmq2.cloudamqp.com/qkafgowp')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
