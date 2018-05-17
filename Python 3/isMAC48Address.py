# A media access control address (MAC address) is a unique identifier assigned to 
# network interfaces for communications on the physical network segment.
# The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is
# six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).
# Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.


def isMAC48Address(inputString):

    for i in range(len(inputString)):
        if i % 3 == 2:
            if inputString[i] != '-':
                return False
        else:
            sym = inputString[i]
            if not ('0' <= sym and sym <= '9' or 'A' <= sym and sym <= 'F'):
                return False

    return len(inputString) == 17

