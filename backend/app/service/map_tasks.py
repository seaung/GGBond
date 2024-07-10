from celery import shared_task


@shared_task
def nmap_scan_task(target: str = '') -> dict:
    return {'res': target}

