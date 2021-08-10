from bleak import BleakScanner, BleakClient
from typing import List
import asyncio
import time

UART_TX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

class BleSerial:
    def __init__(self) -> None:
        self.client = None
        self.device = None
        self.scanned_devices = []


    async def scan(self) -> List[str]:
        self.scanned_devices = await BleakScanner.discover()
        return [d.name for d in self.scanned_devices]


    def notification_handler(self, sender, data) -> None:
        print("{0}: {1}".format(sender, data))


    async def connect(self, device_name) -> bool:
        print("Connecting...")
        for device in self.scanned_devices:
            if device.name == device_name:
                self.device = device
                self.client = BleakClient(device.address)
                try:
                    await self.client.connect()
                    await self.client.start_notify(UART_RX_UUID, self.notification_handler)
                    print("Connected!")
                    return True
                except Exception as err:
                    print(err)
                    return False
        return False

    async def disconnect(self) -> None:
        if self.client is not None:
            print("Disconnecting")
            await self.client.disconnect()
            print("Disconnected")

    async def send(self, payload: bytes) -> None:
        await self.client.write_gatt_char(UART_TX_UUID, bytearray(payload, 'utf-8'))

    async def send_str(self, payload: str) -> None:
        p = payload + "\r\n"
        await self.send(p)

    async def read(self):
        data = await self.client.read_gatt_char(UART_RX_UUID)
        return data

# async def go(loop):
#     a = BleCon()
#     await a.scan()
#     await a.connect("Hexapod")
#     while 1:
#         await a.send_str("Hello");
#         time.sleep(1)

# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(go(loop))
