from clean_architecture.use_cases.business_entity_gateway import BusinessEntityGateway


class UseCase(object):
    def __init__(self, gateway):
        gateway: BusinessEntityGateway
        self._gateway = gateway

    def execute(self):
        pass
