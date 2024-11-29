import shared.downlinkFields as DWHDR
import shared.utilities as utools
import shared.commonCommands as cfunc

class WISE2200M:
    def __init__(self) -> None:
        pass

    def time_sync(
        type: int,
        fcnt: int,
        timestamp,
        version: int = 0
    )-> str:
        """
        Perform time synchronization for Unix timestamp or ISO 8601.

        Parameters:
            type (int): Type of time sync (U for Unix, I for ISO 8601).
            fcnt (int): Frame counter value.
            timestamp (int or str): Time value, int for Unix and str for ISO 8601.
            version (int, optional): Version number (default is 0).

        Returns:
            str: Hexadecimal string of the time sync payload.
        """
        return cfunc.time_sync(type, fcnt, timestamp, version)
    
    def update_uplink_interval(
        fcnt: int,
        interval: int,
        version: int = 0
    ) -> str:
        """
        Update uplink interval for the device.

        Parameters:
            fcnt (int): Frame counter value.
            interval (int): Interval value.
            version (int, optional): Version number (default is 0).

        Returns:
            str: Hexadecimal string of the updated interval payload.
        """
        return cfunc.update_uplink_interval(fcnt, interval, version)
    
    def transparent(
        self,
        fcnt: int,
        raw_data: bytes
    ):
        """
        Convert buffer to LoRa format.

        Parameters:
            fcnt (int): Frame counter value.
            raw_data (bytes): Raw data to be converted.

        Returns:
            str: Hexadecimal string of the LoRa payload.
        """
        fcnt_b = (fcnt % 256).to_bytes(1)
        header = b''.join([b'\x80', fcnt_b])

        raw_data_len = len(raw_data)

        # Combine content
        content = b''.join([
            utools.int_to_little_endian_bytes(DWHDR.IO_APPRAW_DATA << 4, 1),
            utools.int_to_little_endian_bytes(raw_data_len, 2),
            raw_data
        ])

        header += utools.int_to_little_endian_bytes(len(content), 1)
        
        # Calculate CRC
        crc = utools.crc8(content)

        # Combine header, content, and crc
        ret = header + content + crc

        # Return hexadecimal string
        return ret.hex()