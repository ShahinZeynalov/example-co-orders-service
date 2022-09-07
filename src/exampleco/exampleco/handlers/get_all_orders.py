import json

from src.exampleco.exampleco.models.database import Session
from src.exampleco.exampleco.models.database.orders import Order, OrderSchema
from src.exampleco.exampleco.models.database.services import Service, ServiceSchema

# pylint: disable=unused-argument
def get_all_orders(event, context):
    """
    Example function that demonstrates grabbing list or orders from database

    Returns:
        Returns a list of all orders pulled from the database.
    """

    # orders_schema = OrderSchema(many=True)
    # orders = Session.query(Order).all()
    # results = orders_schema.dump(orders)

    service_schema = ServiceSchema(many=True)
    services = Session.query(Service).all()
    results = service_schema.dump(services)

    response = {"statusCode": 200, "body": json.dumps(results)}

    return response
