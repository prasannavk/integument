REGISTERED_CLASSES = []

def registered_class(cls):
    REGISTERED_CLASSES.append(cls)
    return cls