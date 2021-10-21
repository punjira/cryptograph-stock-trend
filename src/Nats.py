import asyncio
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN



class NatsService:
    def __init__(self, nats_server_address, nats_server_channel):
        self.NATSERVER = nats_server_address
        self.CHANNEL = nats_server_channel
        self.CONNECTTIMEOUT = 5
        self.MAXRECONNECTATTEMPTS = 5
        self.RECONNECTTIMEWAIT = 5
        self.nc = NATS()
        self.sc = STAN()
    
    def start_listening(self):
        loop = asyncio.get_event_loop()
        try:
            loop.create_task(self.listener_loop(loop))
            loop.run_forever()
        finally:
            loop.close()
    
    async def listener_loop(self, loop):
        print("connecting to nats listener loop")
        await self.nc.connect(servers=[self.NATSERVER], io_loop=loop)
        print("creation done")
        await self.sc.connect(self.CHANNEL, "trend-client", nats=self.nc)
        async def message_handler(msg):
            data = msg.data.decode()
        print("subscribing to event message")
        await self.sc.subscribe("CANDLE_UPDATE", cb=message_handler)