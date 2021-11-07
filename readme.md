# Cryptograph trend service

## What this is

## Nats

tho ants-streaming-server is installed and its modules are available and set up, **this project is not using nats-streaming-server** due to concurrency complexity.

## https server

to avoid such complexities, there is a minimal http flask server setup in `server.py` module which returns the requested trend. (no docs generated yet. WIP)
