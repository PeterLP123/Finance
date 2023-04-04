"""This is a test file for the polygon.io API."""
from typing import cast
import json
from polygon import RESTClient
from urllib3 import HTTPResponse
import config

client = RESTClient(config.API_KEY)

aggs = cast(
    HTTPResponse,
    client.get_aggs(
        'AAPL',
        1,
        'day',
        '2022-05-20',
        '2022-11-11',
        raw=True,
    )
)

data = json.loads(aggs.data)
print(data)
