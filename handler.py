try:
    import unzip_requirements
except ImportError:
    pass


import json

import numpy as np


def get(event, context):
    a = np.arange(15).reshape(3, 5)
    js = json.dumps(a.tolist())
    print(f"Returned json: {js}")
    response = {"statusCode": 200, "body": js}
    return response


if __name__ == "__main__":
    get('', '')
