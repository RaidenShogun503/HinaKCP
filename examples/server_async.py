from __future__ import annotations

from kcp.server import Connection
from kcp.server import KCPServerAsync

# Create the initial server instance.
server = KCPServerAsync(
    "127.0.0.1",
    9999,
    conv_id=1,
    no_delay=True,
)

# Set performance options.
server.set_performance_options(
    update_interval=10,
)


# When the server starts.
@server.on_start
async def on_start() -> None:
    print("Server started!")


# When data is received from a client.
@server.on_data
async def on_data(connection: Connection, data: bytes) -> None:
    print(f"Received data from {connection.address}: {data}")

    # Send a response back to the client
    response = b"Hello, client!"
    connection.enqueue(response)  # Gửi dữ liệu đến client bằng phương thức enqueue
    print(f"Sent data to {connection.address}: {response}")


# Start the server.
server.start()
