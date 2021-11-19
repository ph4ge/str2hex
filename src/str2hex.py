#!/usr/bin/env python3

import binascii
import logging
import pprint
from struct import pack
from textwrap import wrap
import fire

logging.basicConfig(filename="str2hex.log", filemode="a", level=logging.DEBUG)


class StringStuff:
    """
    class to get a hex representation of a string, modify its endianness so it
    lands properly into memory
    """

    def __init__(self, astr, se=False):
        """
        a_str: the string we'd like to get the hex representation
        se: stands for swap/switch endianness
        _hex_str:
        _hex_bytes:
        _len:
        """

        if StringStuff._first_read(astr):
            self.a_str = astr
            self._hex_str = ""
            self._hex_bytes = bytes
            self._se = se
            self._se_str = ""
            self._se_hex_str = ""
            self._len = len(astr)

    def str2hex(self):
        """
        convert an ascii string to its hex representation
        :return hex representation of string encoded as a str(to be able
        to print it)
          "hello"
        => hell : 68656c6c  o : 0000006f
        more examples in the tests
        """

        # first check if the string is ascii printable
        if self.a_str.isascii():
            a_str2hex = binascii.hexlify(self.a_str.encode())
            a_str2hex_str = a_str2hex.decode()

            self.hex_bytes = a_str2hex
            self._hex_str = a_str2hex_str

            # case: 0 < str <= 4
            if len(self.a_str) < 5:
                self._swap_end32()
                if self._se:
                    return "".join(
                        "{0} : {1}\n{2} : {3}".format(
                            self.a_str,
                            a_str2hex_str.zfill(8),
                            self._se_str,
                            self._se_hex_str,
                        )
                    )
                return "".join("{0} : {1}".format(self.a_str, a_str2hex_str.zfill(8)))
            # all other cases: str > 4
            # else:
            self._swap_end32()
            # split string in mini-batches of 4 bytes or 8 in hex
            # return type: list
            x = wrap(a_str2hex_str, 8)
            return "  ".join(
                [
                    "{0} : {1}".format(binascii.unhexlify(el).decode(), el.zfill(8))
                    for el in x
                ]
            )

    def _swap_end32(self):
        """
        change the endianness of the string
        updates the _se object attribute
        """

        try:
            if self._se and len(self.a_str) > 4:
                print("[+] Do not support this option for strings longer than 4.\n")
                logging.warning(
                    "Do not support this option for strings longer than 4",
                    exc_info=True,
                )
            elif self._se:
                self._se_str = pack("<I", int(self._hex_str, 16)).decode()
                # self._se_str = self._se_str.rstrip('\x00')
                self._se_hex_str = binascii.hexlify(self._se_str.encode()).decode()
                # change null bytes position?

        except Exception as e:
            logging.error("Exception raised from inside swap_end32().", exc_info=True)
            print(e)

    @staticmethod
    def _first_read(init_str=None):
        """ """

        try:
            if pprint.isreadable(init_str):
                if isinstance(init_str, str):
                    return True
                logging.error("Input string cannot be processed!", exc_info=True)
                raise TypeError("{0} is not a str instance!".format(init_str))
        except Exception as e:
            logging.error("Exception raised from inside first_read().", exc_info=True)
            print(e)
            return False

    def __str__(self):
        return f"{self.a_str}"

    def __len__(self):
        return "{0}".format(self._len)


if __name__ == "__main__":
    fire.Fire(StringStuff)
