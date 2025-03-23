import shared.downlinkFields as DWHDR
from products.WISE2410 import WISE2410
from products.WISE4610 import WISE4610
from products.WISE2200M import WISE2200M

# WISE2410 test functions
def wise2410testtimesync():
    device = WISE2410()
    cmd = device.time_sync(
        type=DWHDR.TIMESYNC_TYPE_I,
        fcnt=0,
        timestamp="2020-06-23T10:16:07+08:00",
        version=0
    )
    print(f"Generated WISE-2410 TimeSync Command: {cmd}")

def wise2410testgenfftcommand():
    device = WISE2410()
    cmd = device.gen_fft_command(
        type=DWHDR.FFT_TYPE_L,
        fcnt=0,
        log_index=12345,
        timestamp=1742716800,  # Unix time for 2025/3/23 16:00:00+08:00
        isX=True,
        isY=True,
        isZ=True,
        version=0
    )
    print(f"Generated WISE-2410 FFT Command: {cmd}")

def wise2410testupdateuplinkinterval():
    device = WISE2410()
    cmd = device.update_uplink_interval(
        fcnt=0,
        interval=60,
        version=0
    )
    print(f"Generated WISE-2410 Uplink Interval Command: {cmd}")

# WISE4610 test functions
def wise4610testtimesync():
    device = WISE4610()
    cmd = device.time_sync(
        type=DWHDR.TIMESYNC_TYPE_U,
        fcnt=1,
        timestamp=1609459200,  # 2021-01-01 00:00:00 UTC
        version=0
    )
    print(f"Generated WISE-4610 TimeSync Command: {cmd}")

def wise4610testupdateuplinkinterval():
    device = WISE4610()
    cmd = device.update_uplink_interval(
        fcnt=1,
        interval=120,
        version=0
    )
    print(f"Generated WISE-4610 Uplink Interval Command: {cmd}")

# WISE2200-M test functions
def wise2200Mtesttimesync():
    device = WISE2200M()
    cmd = device.time_sync(
        type=DWHDR.TIMESYNC_TYPE_I,
        fcnt=2,
        timestamp="2022-09-15T12:00:00+08:00",
        version=0
    )
    print(f"Generated WISE-2200-M TimeSync Command: {cmd}")

def wise2200Mtestupdateuplinkinterval():
    device = WISE2200M()
    cmd = device.update_uplink_interval(
        fcnt=2,
        interval=180,
        version=0
    )
    print(f"Generated WISE-2200-M Uplink Interval Command: {cmd}")

def wise2200Mtesttransparent():
    device = WISE2200M()
    # Sample raw_data
    raw_data = b'\x01\x02\x03'
    cmd = device.transparent(
        fcnt=2,
        raw_data=raw_data
    )
    print(f"Generated WISE-2200-M Transparent Command: {cmd}")

def main():
    print("=== WISE-2410 Tests ===")
    wise2410testgenfftcommand()
    wise2410testtimesync()
    wise2410testupdateuplinkinterval()
    
    print("\n=== WISE-4610 Tests ===")
    wise4610testtimesync()
    wise4610testupdateuplinkinterval()
    
    print("\n=== WISE-2200-M Tests ===")
    wise2200Mtesttimesync()
    wise2200Mtestupdateuplinkinterval()
    wise2200Mtesttransparent()

if __name__ == "__main__":
    main()
