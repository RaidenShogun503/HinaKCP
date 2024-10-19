from __future__ import annotations

import time

from kcp.client import KCPClientSync

# Các tham số cần thiết
address = '127.0.0.1'
port = 9999
conv_id = 1
no_delay = True  # hoặc False tùy thuộc vào yêu cầu của bạn
update_interval = 10  # khoảng thời gian cập nhật trong ms
resend_count = 2  # số lần gửi lại
no_congestion_control = False  # có hoặc không kiểm soát tắc nghẽn
receive_window_size = 128  # kích thước cửa sổ nhận
send_window_size = 32  # kích thước cửa sổ gửi

# Khởi tạo đối tượng KCPClientSync
client = KCPClientSync(
    address=address,
    port=port,
    conv_id=conv_id,
    no_delay=no_delay,
    update_interval=update_interval,
    resend_count=resend_count,
    no_congestion_control=no_congestion_control,
    receive_window_size=receive_window_size,
    send_window_size=send_window_size,
)



@client.on_data
def handle_data(data: bytes) -> None:
    print(data)


@client.on_start
def on_start() -> None:
    print("Connected to server!")

    while True:
        client.send(b"Binh Ga")
        time.sleep(1)


client.start()
