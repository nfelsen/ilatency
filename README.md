# iLatency

iLatency is a simple network latency measurement tool that operates similarly to iperf. It allows you to test network latency between servers either in a single-threaded or multi-threaded mode, providing flexibility in how network performance is measured.

## Installation

To install iLatency, simply use pip:

```bash
pip install ilatency
```

## Usage

iLatency can be run in either server or client mode.

### Server Mode
To start iLatency in server mode:

```bash
ilatency --server
```

### Client Mode
To test latency to multiple servers in parallel:

```bash
ilatency --client --host 192.168.1.1 192.168.1.2 --port 12345 --count 100 --repeat 10 --concurrency 5
```

## Contributing
Contributions to iLatency are welcome! Please fork the repository and submit a pull request with your changes or improvements.

## License
iLatency is released under the MIT License. See the LICENSE file for more details.
