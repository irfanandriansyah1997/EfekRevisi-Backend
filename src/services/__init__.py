from src.services.NewsHandler import processor as NewsProcessor

from thrift.TMultiplexedProcessor import TMultiplexedProcessor
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class ServiceHandler:
    def __init__(self, host, port):
        self.config = {
            'host': host,
            'port': port
        }

        self.transport = self.set_connection()
        self.processor = TMultiplexedProcessor()

    def set_processor(self, item):
        self.processor.registerProcessor(**item)

    def set_connection(self):
        return TSocket.TServerSocket(**self.config)

    @staticmethod
    def get_processor():
        return [
            {
                'serviceName': 'news',
                'processor': NewsProcessor
            }
        ]

    def run(self):
        for item in ServiceHandler.get_processor():
            self.set_processor(item)

        print("Serving the Wrapper listener, port: " + str(self.config.get('port')))

        return TServer.TThreadedServer(
            self.processor,
            self.transport,
            TTransport.TBufferedTransportFactory(),
            TBinaryProtocol.TBinaryProtocolFactory()
        )
