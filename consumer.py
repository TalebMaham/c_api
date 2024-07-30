import os
import logging
import django
import pika
import json
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c_api.settings')
django.setup()

from stock.models import TechnicalData, Product

def callback(ch, method, properties, body):
    data = json.loads(body)
    product_id = data.get('product')
    print(f"la data recuperé {data}")
    try:
        product = Product.objects.get(id=product_id)
        TechnicalData.objects.create(
            message=data.get('message'),
            value=data.get('value'),
            value_type=data.get('value_type'),
            product=product
        )
        print(f"Received data: {data}")
    except Product.DoesNotExist:
        logging.error(f"Product with id {product_id} does not exist")
    except Exception as e:
        logging.error(f"Error processing message: {e}")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='technical_data')
channel.basic_consume(queue='technical_data', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
