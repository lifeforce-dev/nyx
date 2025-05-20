import uvicorn
import urllib.parse

from common.logging import setup_logging
from common.settings import APP_SETTINGS

def start(**kwargs):
    uvicorn_arguments = {
        'reload': False,
        'host': '0.0.0.0',
        'port': 8000,
        'log_level': 'debug',
        'use_colors': True,
    }

    parsed = urllib.parse.urlparse(APP_SETTINGS.base_url)
    if parsed.port is not None:
        uvicorn_arguments['port'] = parsed.port

    uvicorn_arguments.update(kwargs)

    uvicorn.run(
        'backend.app:create_app',
        factory=True,
        log_config=None,
        **uvicorn_arguments
    )

if __name__ == '__main__':
    start()