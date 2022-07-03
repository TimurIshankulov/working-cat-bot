def get_fullname(firstname, lastname):
    """Returns fullname or anonimous string"""
    if isinstance(firstname, str) and isinstance(lastname, str):
        return ' '.join([firstname, lastname])
    else:
        return 'Anonymous'