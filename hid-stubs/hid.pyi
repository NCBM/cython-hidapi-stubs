__version__: str

import sys
from typing import Iterable, List, SupportsBytes

from typing_extensions import SupportsIndex, TypedDict

if sys.version_info >= (3, 12):
    from collections.abc import Buffer
    _BytesCompatible = bytes | Iterable[SupportsIndex] | SupportsIndex | SupportsBytes | Buffer
else:
    _BytesCompatible = bytes | Iterable[SupportsIndex] | SupportsIndex | SupportsBytes


class _HIDDeviceInfoDict(TypedDict):
    path: bytes
    vendor_id: int
    product_id: int
    serial_number: str
    release_number: int
    manufacturer_string: str
    product_string: str
    usage_page: int
    usage: int
    interface_number: int
    bus_type: int


def enumerate(vendor_id: int = 0, product_id: int = 0) -> List[_HIDDeviceInfoDict]:
    """Return a list of discovered HID devices.

    The fields of dict are:

     - 'path'
     - 'vendor_id'
     - 'product_id'
     - 'serial_number'
     - 'release_number'
     - 'manufacturer_string'
     - 'product_string'
     - 'usage_page'
     - 'usage'
     - 'interface_number'
     - 'bus_type'

    :param vendor_id: Vendor id to look for, default = 0
    :type vendor_id: int, optional
    :param product_id: Product id to look for, default = 0
    :type product_id: int, optional
    :return: List of device dictionaries
    :rtype: List[Dict]
    """
    ...


def version_str() -> str:
    """Return a runtime version string of the hidapi C library.

    :return: version string of library
    :rtype: str
    """
    ...


class device:
    def open(self, vendor_id: int = 0, product_id: int = 0, serial_number: str | None = None) -> None:
        """Open the connection.

        :param vendor_id: Vendor id to connect to, default = 0
        :type vendor_id: int, optional
        :param product_id: Product id to connect to, default = 0
        :type product_id: int, optional
        :param serial_number:
        :type serial_number: unicode, optional
        :raises IOError:
        """
        ...

    def open_path(self, path: bytes) -> None:
        """Open connection by path.

        :param path: Path to device
        :type path: bytes
        :raises IOError:
        """
        ...

    def close(self) -> None:
        """Close connection.

        This should always be called after opening a connection.
        """
        ...

    def write(self, buff: _BytesCompatible) -> int:
        """Accept a list of integers (0-255) and send them to the device.

        :param buff: Data to write (must be convertible to `bytes`)
        :type buff: Any
        :return: Write result
        :rtype: int
        """
        ...

    def set_nonblocking(self, v: int | bool) -> int:
        """Set the nonblocking flag.

        :param v: Flag value (1 or 0, True or False)
        :type v: int, bool
        :return: Flag result
        :rtype: int
        """
        ...

    def read(self, max_length: int, timeout_ms: int = 0) -> List[int]:
        """Return a list of integers (0-255) from the device up to max_length bytes.

        :param max_length: Maximum number of bytes to read
        :type max_length: int
        :param timeout_ms: Number of milliseconds until timeout (default: no timeout)
        :type timeout_ms: int, optional
        :return: Read bytes
        :rtype: List[int]
        """
        ...

    def get_manufacturer_string(self) -> str:
        """Return manufacturer string (e.g. vendor name).

        :return:
        :rtype: str
        :raises ValueError: If connection is not opened.
        :raises IOError:
        """
        ...

    def get_product_string(self) -> str:
        """Return product string (e.g. device description).

        :return:
        :rtype: str
        :raises ValueError: If connection is not opened.
        :raises IOError:
        """
        ...

    def get_serial_number_string(self) -> str:
        """Return serial number.

        :return:
        :rtype: str
        :raises ValueError: If connection is not opened.
        :raises IOError:
        """
        ...

    def get_indexed_string(self, index: int) -> str:
        """Return indexed string.

        :return:
        :rtype: str
        :raises ValueError: If connection is not opened.
        :raises IOError:
        """
        ...

    def send_feature_report(self, buff: _BytesCompatible) -> int:
        """Accept a list of integers (0-255) and send them to the device.

        :param buff: Data to send (must be convertible into bytes)
        :type buff: any
        :return: Send result
        :rtype: int
        """
        ...

    def get_feature_report(self, report_num: int, max_length: int) -> List[int]:
        """Receive feature report.

        :param report_num:
        :type report_num: int
        :param max_length:
        :type max_length: int
        :return: Incoming feature report
        :rtype: List[int]
        :raises ValueError: If connection is not opened.
        :raises IOError:
        """
        ...

    def get_input_report(self, report_num: int, max_length: int) -> List[int]:
        """Get input report

        :param report_num:
        :type report_num: int
        :param max_length:
        :type max_length: int
        :return:
        :rtype: List[int]
        :raises ValueError: If connection is not opened.
        :raises IOError:
        """
        ...

    def error(self) -> str:
        """Get error from device, or global error if no device is opened.

        :return:
        :rtype: str
        :raises IOError:
        """
        ...
