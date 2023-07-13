from celery import shared_task, current_app

from models.models import Device


async def nmap_scan_worker(host, max_reader, search) -> None:
    port_list = []
    hostname = host.hostname[0]

    reader = max_reader.get(host.address)

    for port in host.services:
        if port.state == 'open':
            port_list.append(port.port)
        else:
            port_list.append('None')

    port_string = ', '.join(str(item) for item in port_list)

    device = Device()
    await device.save()


