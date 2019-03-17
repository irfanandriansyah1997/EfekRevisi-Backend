from src.services import ServiceHandler
from src.helper.ConfigHelper import get_config


class App:
    def __init__(self):
        self.config = get_config('config.conf')
        self.service = ServiceHandler(**self.get_config_service())

    def get_config_service(self):
        return {
            'host': self.config.get('default', 'host'),
            'port': self.config.get('default', 'port')
        }

    def run(self):
        self.service.run().serve()


if __name__ == '__main__':
    app = App()
    app.run()
