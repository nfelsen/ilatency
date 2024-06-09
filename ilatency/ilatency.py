import socket
import time
import argparse
import threading
import concurrent.futures

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((host, port))
        server.listen(5)
        print(f"Server listening on {host}:{port}")

        try:
            while True:
                client_socket, addr = server.accept()
                print(f"Connection from {addr}")
                with client_socket:
                    while True:
                        data = client_socket.recv(1024)
                        if not data:
                            break
                        client_socket.sendall(data)  # Echo back the received data
                    print(f"Closed connection from {addr}")
        except KeyboardInterrupt:
            print("Server is closing...")
            server.close()

def measure_latency(host, port, count, repeat):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(2.0)
        client.connect((host, port))
        latencies = []
        for _ in range(count):
            start_time = time.time()
            client.sendall(b"Hello")
            response = client.recv(1024)
            end_time = time.time()
            latencies.append((end_time - start_time) * 1000)
    
    avg_latency = sum(latencies) / len(latencies)
    min_latency = min(latencies)
    max_latency = max(latencies)
    return avg_latency, min_latency, max_latency

def test_server(host, port, count, repeat):
    for _ in range(repeat):
        avg, min_l, max_l = measure_latency(host, port, count, repeat)
        print(f"Host: {host}, Avg Latency: {avg:.2f} ms, Min: {min_l:.2f} ms, Max: {max_l:.2f} ms")

def main():
    parser = argparse.ArgumentParser(description='Test network latency like iperf.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s', '--server', action='store_true', help='Run in server mode')
    group.add_argument('-c', '--client', action='store_true', help='Run in client mode')
    parser.add_argument('--host', nargs='*', help='Host IPs to connect to (client mode only)')
    parser.add_argument('--port', type=int, default=12345, help='Port number to connect to or listen on')
    parser.add_argument('--count', type=int, default=100, help='Number of messages to send (client mode only)')
    parser.add_argument('--repeat', type=int, default=10, help='How many times to repeat the test (client mode only)')
    parser.add_argument('--concurrency', type=int, default=5, help='Number of concurrent tests to run (client mode only)')

    args = parser.parse_args()

    if args.server:
        host = args.host[0] if args.host else '0.0.0.0'
        start_server(host, args.port)
    elif args.client:
        if not args.host:
            raise ValueError("Host IP(s) must be provided for client mode.")
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            futures = [executor.submit(test_server, host, args.port, args.count, args.repeat) for host in args.host]
            for future in concurrent.futures.as_completed(futures):
                future.result()

if __name__ == "__main__":
    main()
