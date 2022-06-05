from json import JSONEncoder
from datetime import date


class AppJsonEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        # default json encoding using the __dict__
        return obj.__dict__
