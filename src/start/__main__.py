import uvicorn
from config import settings

uvicorn.run(
    'main:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)