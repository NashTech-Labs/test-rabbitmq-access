import re
import pika
def extract_broker_infos(broker_url):
    prog = re.compile('^amqp://(.+):(.+)@(.+):([0-9]+)/{0,1}(.*)$')
    user, passw, host, port, vhost = prog.match(broker_url).groups()
    args = [host, user, passw, int(port)]
    if vhost:
        args += [vhost]
    return args
broker_url='amqp://imnitin28:Nitin@Knoldus@remote.server.com:5672/knoldus'
# A sample broker_url looks like this -> "amqp://user:password@remote.server.com:port//vhost"
args = extract_broker_infos(broker_url)

# def checkRabbitMQAccess(args):
host = args[0]
user = args[1]
password = args[2]
port = args[3]
vhost = args[4]

credentials = pika.PlainCredentials(user, password)
parameters = pika.ConnectionParameters(host=host,
                                           port=port,
                                           virtual_host=vhost,
                                           credentials=credentials)
connection = pika.BlockingConnection(parameters)