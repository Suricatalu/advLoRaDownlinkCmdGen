import shared.downlinkFields as DWHDR
from products.WISE2410 import WISE2410

def wise2410testtimesync():
    device = WISE2410()

    cmd = device.time_sync(
        type = DWHDR.TIMESYNC_TYPE_I,
        fcnt = 0,
        timestamp = "2020-06-23T10:16:07+08:00",
        version = 0
    )

    print(f"Generated WISE-2410 Command: {cmd}")

def main():
    wise2410testtimesync()

if __name__ == "__main__":
    main()