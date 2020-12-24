__author__ = "arnavanchit@gmail.com"

from google.cloud.ndb import Client

# Optional Config
namespace = None
project = None

# set the client directly
db_client = None


def get_db_client():
    """
    Returns an ndb Client object
    (https://googleapis.dev/python/python-ndb/latest/client.html#module-google.cloud.ndb.client)
    The following priority order applies:
        1. If db_client is directly passed, return it
        2. If parameters like namespace and project are supplied create a client with them and return
        3. If parameters like namespace and project are not supplied create a client without them and return
    :return: google.cloud.ndb.client.Client
    """
    if db_client:
        return db_client
    kwargs = {}
    if namespace:
        kwargs["namespace"] = namespace
    if project:
        kwargs["project"] = project

    return Client(**kwargs)