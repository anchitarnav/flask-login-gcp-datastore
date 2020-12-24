__author__ = 'arnavanchit@gmail.com'

# Imports from the ndb module: https://googleapis.dev/python/python-ndb/latest/index.html
from google.cloud import ndb

# Imports from the same module
from flask_login_user.gcp.datastore.config import get_db_client
from flask_login_user.gcp.datastore.caching import cached


class User(ndb.Model):
    """
    The User class that you are required to implement for flask-login
    https://flask-login.readthedocs.io/en/latest/#your-user-class
    """
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.authenticated = kwargs.get('authenticated', False)
        self.activated = kwargs.get('activated', True)
        self.anonymous = False

    def __str__(self):
        return "{} ({})".format(self.email, self.name)

    def __repr__(self):
        return "{} ({})".format(self.email, self.name)

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_active(self):
        return self.activated

    @property
    def is_anonymous(self):
        return self.anonymous

    def get_id(self):
        """
        returns a unicode that uniquely identifies this user,
        and can be used to load the user from the user_loader callback
        :return: str: user_id
        """
        return self.key.id()

    def can_login(self, password: str):
        """
        Tells if the user has entered the correct password
        :param password: str
        :return: bool
        """
        return password == self.password

    @staticmethod
    @cached
    def get(user_id: str):
        """
        Get an object of User class based on the passed user_id. returns None if user not found
        :param user_id: str: The user ID for which the User object is required
        :return: User or None
        """
        with get_db_client().context():
            return User.get_by_id(id=user_id)
