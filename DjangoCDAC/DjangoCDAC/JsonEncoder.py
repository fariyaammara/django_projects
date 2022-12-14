from datetime import datetime, date
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return datetime.isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)
