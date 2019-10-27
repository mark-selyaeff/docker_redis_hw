import os
import socket
import redis
import time
import json

HOST = ''
PORT = 80

print("Waiting for redis server...")
time.sleep(5.0)

r = redis.Redis(host='redis', port=6379)


def process_cache(data):
    data = data.decode('utf-8')
    res = r.get(data)
    if res is None:
        r.set(data, 1)
        return f"OK: {data}"
    else:
        return f"Cached: {data}"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            response = process_cache(data)
            # print("Got:", data)
            conn.sendall((response + '\n').encode('utf-8'))
