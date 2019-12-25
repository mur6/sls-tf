try:
    import unzip_requirements
except ImportError:
    pass


import json
#import tensorflow as tf
import yaml
#import pandas as pd
#import numpy as np


def get(event, context):
    # a = tf.random.normal([2, 2])
    # js = json.dumps(a.numpy().tolist())
    # print(f"Returned json: {js}")
    d = {"a": 1, "b": 2}
    js = yaml.dump(d)
    response = {"statusCode": 200, "body": js}
    return response


if __name__ == "__main__":
    get('', '')
