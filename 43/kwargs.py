def get_profile(*args, **kwargs) -> str:

    if len(args) > 0:
        raise TypeError('no positional arguments are allowed')

    if len(kwargs.keys()) == 1 and 'name' not in kwargs.keys():
        raise TypeError(f'Invalid kwargs: {kwargs.keys()}')

    if len(kwargs.keys()) > 2:
        raise TypeError(f'Invalid kwargs: {kwargs.keys()}')

    name = kwargs.get('name', 'julian')
    profession = kwargs.get('profession', 'programmer')

    return f'{name} is a {profession}'