# src/shared/utilities.py

def crc8(data: bytes, version: 0, polynomial: int = 0x07, initial_value: int = 0xFF) -> bytes:
    """
    Calculate the CRC-8 checksum of the given data using the CRC-8-CCITT polynomial.

    Parameters:
        data (bytes): The input data for which the CRC is calculated.
        initial_value (int): The initial CRC value (default is 0xFF).

    Returns:
        bytes: A single byte representing the calculated CRC-8 checksum.
    """
    crc = initial_value

    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ polynomial) & 0xFF
            else:
                crc = (crc << 1) & 0xFF

    if version == 1:
        crc = 0xFF ^ crc

    return crc.to_bytes(1, 'big')

def int_to_little_endian_bytes(data: int, len: int) -> bytes:
    return data.to_bytes(len, 'little')
    
def str_to_bytes(data: str) -> bytes:
    return data.encode("utf-8")


