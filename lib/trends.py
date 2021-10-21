import os
import sys

sys.path.append(os.path.abspath("/app"))

nats_server_address = os.environ['NATS_URL']
nats_server_channel = os.environ['NATS_CLUSTER_NAME']

from src.Nats import NatsService

try:
    print("starting nats service instance")
    ns = NatsService(nats_server_address, nats_server_channel)
    print("listening for approved message")
    ns.start_listening()
except Exception as e:
    print(f"Error: {e}")

