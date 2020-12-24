__author__ = 'arnavanchit@gmail.com'

_user_cache = dict()

# Basic Caching implementation
# This can be changed to implement a more details cache
# The decorator ensures that the usage in users.py does not require to be changed


def cached(func):
    """
    return a function which retrives the User object from local cache if present
    else calls the original function to get the value
    :param func: callable
    :return:
    """
    def new_func(user_id):
        cached_user = _user_cache.get(user_id)
        if not cached_user:
            cached_user = func(user_id)
            _user_cache[user_id] = cached_user
        return cached_user
    new_func.__name__ = "get"
    return new_func
