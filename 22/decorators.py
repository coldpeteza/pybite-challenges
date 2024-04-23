from functools import wraps


def make_html(element):

    @wraps(element)
    def decorator(fnc):

        def wrapper(*args, **kwargs):

            result = f'<{element}>{fnc(*args, **kwargs)}</{element}>'

            return result

        return wrapper

    return decorator
