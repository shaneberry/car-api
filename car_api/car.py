"""
This is the car module and supports all the ReST actions
for the CAR collection
"""


def find_all():
    """
    This function responds to a request for /cars with the complete
    lists of cars
    :return: json string of list of cars
    """
    # TODO: Serialize the data for the response
    pass


def find_by_id(car_id):
    """
    This function responds to a request for /cars/{id}

    :param car_id:   Identifier of car to find
    :return:         car matching id
    """
    pass


def brands():
    """
    This function return all the car brands

    :return: a list of string
    """
    pass


def models():
    """
    This function return all the car models

    :return: a list of string
    """
    pass


def create(car):
    """
    This function creates a new car in the cars structure
    based on the passed data

    :param car:  car to create
    :return      200 on success, 406 on person exists
    """
    pass


def update(car_id, new_car):
    """
    This function updates an existing car.

    :param car_id:   identifier of the car to update
    :param new_car:  car to update
    :return:         updated car structure
    """
    pass


def delete(car_id):
    """
    This function deletes a car based on an identifier

    :param car_id:   identifier of the car to delete
    :return:         200 on successful delete, 404 if not found
    """
    pass
