import shared.downlinkFields as DWHDR
import shared.utilities as utools
import shared.commonCommands as cfunc

class WISE4610:
    def __init__(self) -> None:
        pass

    def time_sync(
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