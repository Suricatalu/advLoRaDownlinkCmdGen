import shared.downlinkFields as DWHDR
import shared.utilities as utools

def time_sync(
    type: int,
    fcnt: int,
    timestamp,
    version: int = 0
):
    """
    Time synchronization for Unix timestamp or ISO 8601.

    Parameters:
        type (int): Type of time sync (U for Unix, I for ISO 8601).
        fcnt (int): Frame counter value.
        timestamp (int or str): Time value, int for Unix and str for ISO 8601.
        version (int, optional): Version number (default is 0).

    Returns:
        str: Hexadecimal string of the time sync payload.
    """
    ret = ""
        
    if type == DWHDR.TIMESYNC_TYPE_U:
        ret = _time_sync_U(fcnt, timestamp, version)
    elif type == DWHDR.TIMESYNC_TYPE_I:
        ret = _time_sync_I(fcnt, timestamp, version)
            
    return ret

def update_uplink_interval(
    fcnt: int,
    interval: int,
    version: int = 0
):
    """
    Update uplink interval.

    Parameters:
        fcnt (int): Frame counter value.
        interval (int): Interval value.
        version (int, optional): Version number (default is 0).

    Returns:
        str: Hexadecimal string of the updated interval payload.
    """
    v_header = (0x80 | version).to_bytes(1)
    fcnt_b = (fcnt % 256).to_bytes(1)
    header = b''.join([v_header, fcnt_b])

    content = b''.join([
        utools.int_to_little_endian_bytes(DWHDR.IO_DEVICE_DATA << 4 | DWHDR.DEVICE_DATA_LPWAN_APP_CONFIG, 1),
        utools.int_to_little_endian_bytes(DWHDR.DEVICE_DATA_LPWANAPPCONFIG_IDX_I_LEN, 1),
        utools.int_to_little_endian_bytes(DWHDR.DEVICE_DATA_LPWANAPPCONFIG_IDX_I, 1),
        utools.int_to_little_endian_bytes(interval, DWHDR.PARA_TIME_SIZE)
    ])

    header += utools.int_to_little_endian_bytes(len(content), 1)
    crc = utools.crc8(content, version)

    ret = header + content + crc

    return ret.hex()

# U: Unix Timestamp
def _time_sync_U(
        fcnt: int,
        timestamp: int,
        version: int = 0
):
    """
    Time synchronization for Unix timestamp.

    Parameters:
        fcnt (int): Frame counter value.
        timestamp (int): Unix timestamp value.
        version (int, optional): Version number (default is 0).

    Returns:
        str: Hexadecimal string of the time sync payload.
    """
    v_header = (0x80 | version).to_bytes(1)
    fcnt_b = (fcnt % 256).to_bytes(1)
    header = b''.join([v_header, fcnt_b])

    content = b''.join([
        utools.int_to_little_endian_bytes(DWHDR.IO_DEVICE_DATA << 4 | DWHDR.DEVICE_DATA_GENERAL, 1),
        utools.int_to_little_endian_bytes(DWHDR.DEVICE_DATA_GENERAL_IDX_U_LEN, 1),
        utools.int_to_little_endian_bytes(DWHDR.DEVICE_DATA_GENERAL_IDX_U, 1),
        utools.int_to_little_endian_bytes(timestamp, DWHDR.PARA_TIME_SIZE)
    ])

    header += utools.int_to_little_endian_bytes(len(content), 1)
    crc = utools.crc8(content, version)

    ret = header + content + crc

    return ret.hex()

# I: ISO 8601
def _time_sync_I(
        fcnt: int,
        timestamp: str,
        version: int = 0
):
    """
    Time synchronization for ISO 8601 timestamp.

    Parameters:
        fcnt (int): Frame counter value.
        timestamp (str): ISO 8601 timestamp value.
        version (int, optional): Version number (default is 0).

    Returns:
        str: Hexadecimal string of the time sync payload.
    """
    v_header = (0x80 | version).to_bytes(1)
    fcnt_b = (fcnt % 256).to_bytes(1)
    header = b''.join([v_header, fcnt_b])

    content = b''.join([
        utools.int_to_little_endian_bytes(DWHDR.IO_DEVICE_DATA << 4 | DWHDR.DEVICE_DATA_GENERAL, 1),
        utools.int_to_little_endian_bytes(DWHDR.DEVICE_DATA_IDX_I_LEN, 1),
        utools.int_to_little_endian_bytes(DWHDR.DEVICE_DATA_IDX_I, 1),
        utools.str_to_bytes(timestamp), b'\00'
    ])

    header += utools.int_to_little_endian_bytes(len(content), 1)
    crc = utools.crc8(content, version)

    ret = header + content + crc

    return ret.hex()