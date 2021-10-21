import redis

class redisInterface:
    def __init__(self, redisUrl, redisPort):
        self.client = redis.Redis(host=redisUrl, port=redisPort, decode_responses=True)
    def getCandles(self,hashkey):
        try:
            candles = self.client.hgetall(hashkey)
            return candles
        except Exception as e:
            return None