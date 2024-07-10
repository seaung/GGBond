import os
from typing import Any

from celery import shared_task
from shodan import Shodan


@shared_task
def device_nearby(lat: str = '', lon: str = '', id: int = 1, query: str = '') -> dict:
    shodan_key = os.getenv('SHODAN_API_KEY')
    res: Any = None

    shodan_client = Shodan(shodan_key)
    try:
        res = shodan_client.search('geo:' + lat + ',' + lon + ',15' + query)
    except Exception:
        pass

    return {'result': res}

