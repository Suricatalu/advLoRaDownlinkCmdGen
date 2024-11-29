import shared.downlinkFields as DWHDR
import shared.utilities as utools
import shared.commonCommands as cfunc

class WISE2410:
    def __init__(self) -> None:
        pass

    def time_sync(
        self,
        type: int,
        fcnt: int,
        timestamp,
        version: int = 0
    ):
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
    ):
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

    def gen_fft_command(
            self,
            type: int,
            fcnt: int,
            log_index: int,
            timestamp: int,
            isX: bool = True,
            isY: bool = True,
            isZ: bool = True,
            version: int = 0
    ) -> str:
        """
        Generate FFT command based on type, log index, and timestamp.

        Parameters:
            type (int): Type of FFT command (L for Log Index, LT for Log Index and Timestamp).
            fcnt (int): Frame counter value.
            log_index (int): Log index value.
            timestamp (int): Timestamp value (used for LT type).
            isX (bool, optional): Include X-axis data (default is True).
            isY (bool, optional): Include Y-axis data (default is True).
            isZ (bool, optional): Include Z-axis data (default is True).
            version (int, optional): Version number (default is 0).

        Returns:
            str: Hexadecimal string of the generated FFT command.
        """
        ret = ""
        
        if type == DWHDR.FFT_TYPE_L:
            ret = self._gen_fft_L(fcnt, log_index, isX, isY, isZ, version)
        elif type == DWHDR.FFT_TYPE_LT:
            ret = self._gen_fft_LT(fcnt, log_index, timestamp, isX, isY, isZ, version)
                
        return ret


    # L: Log Index
    def _gen_fft_L(
        self,
        fcnt: int,
        log_index: int,
        isX: bool = True,
        isY: bool = True,
        isZ: bool = True,
        version: int = 0
    ):
        v_header = (0x80 | version).to_bytes(1)
        fcnt_b = (fcnt % 256).to_bytes(1)
        header = b''.join([v_header, fcnt_b])

        log_index = log_index if log_index != 0 else 4294967295

        content = b''.join([
            utools.int_to_little_endian_bytes(DWHDR.IO_SENSOR_DATA << 4 | DWHDR.SENSOR_RANGE_ACC_G, 1),
            utools.int_to_little_endian_bytes(DWHDR.FFT_X_IDX << 5 | DWHDR.FFT_Y_IDX << 5 | DWHDR.FFT_Z_IDX << 5,1),
            utools.int_to_little_endian_bytes(DWHDR.SENSOR_DATA_IDX_LOGIDX_LEN, 1),
            utools.int_to_little_endian_bytes(DWHDR.SENSOR_DATA_IDX_LOGIDX, 1),
            utools.int_to_little_endian_bytes(log_index, DWHDR.PARA_LOGIDX_SIZE)
        ])

        header += utools.int_to_little_endian_bytes(len(content), 1)
        crc = utools.crc8(content, version)

        ret = header + content + crc

        return ret.hex()


    # L: Log Index; T: Timestamp
    def _gen_fft_LT(
        self,
        fcnt: int,
        log_index: int,
        timestamp: int,
        isX: bool = True,
        isY: bool = True,
        isZ: bool = True,
        version: int = 0
    ):
        v_header = (0x80 | version).to_bytes(1)
        fcnt_b = (fcnt % 256).to_bytes(1)
        header = b''.join([v_header, fcnt_b])

        log_index = log_index if log_index != 0 else 4294967295
        content = b''.join([
            utools.int_to_little_endian_bytes(DWHDR.IO_SENSOR_DATA << 4 | DWHDR.SENSOR_RANGE_ACC_G, 1),
            utools.int_to_little_endian_bytes(DWHDR.FFT_X_IDX << 5 | DWHDR.FFT_Y_IDX << 5 | DWHDR.FFT_Z_IDX << 5,1),
            utools.int_to_little_endian_bytes(DWHDR.SENSOR_DATA_IDX_LOGIDX_UTC_LEN, 1),
            utools.int_to_little_endian_bytes(DWHDR.SENSOR_DATA_IDX_LOGIDX_UTC, 1),
            utools.int_to_little_endian_bytes(log_index, DWHDR.PARA_LOGIDX_SIZE),
            utools.int_to_little_endian_bytes(timestamp, DWHDR.PARA_TIME_SIZE)
        ])

        header += utools.int_to_little_endian_bytes(len(content), 1)
        crc = utools.crc8(content, version)

        ret = header + content + crc

        return ret.hex()
    

    
