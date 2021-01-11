import pika

def main():
    
    #Conexion Inicial
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    QUERY = 'Minecraft'

    #Creacion de las Colas
    channel.queue_declare(queue='YouTube')
    channel.queue_declare(queue='Wikipedia')


    #QUERY
    print('  [*] Enviando "{}" a worker_youtube'.format(QUERY))
    channel.basic_publish(exchange='',
                        routing_key='Youtube',
                        body=QUERY)

    print('  [*] Enviando "{}" a worker_wikipedia'.format(QUERY))
    channel.basic_publish(exchange='',
                        routing_key='Wikipedia',
                        body=QUERY)


if __name__ == "__main__":
    main()
