# IPv4 Calculator
#
# Author1: Jonathan Rojas ALfaro
#
# Author2: Kervin Sibaja
#
# Date: November 2020
#
# Course: Redes
#
# Description:
#
#   Calculates the IP class, the subnet mask, Host segment, Network segment, the first address
#   last address, the network address and the broadcast address from a given IP
#
#

def getClass(ip):
    # splits ip into its 4 segments and picks the first one
    firstSegment = int(ip.split('.')[0])
    #Converts segment to bits
    binSeg = bin(int(firstSegment))
    binSeg = binSeg.split("b")[1]
    #Fills segment with 0 if conversion is less than 8 bits
    if (len(binSeg) < 8):
        temp = ""
        for i in range(0, 8 - len(binSeg)):
            temp = temp + "0"
        binSeg = temp + binSeg
    # returns class based on its first segment bits
    if (binSeg[:4] == "1110"):
        return "Clase D"
    elif (binSeg[:3] == "110"):
        return "Clase C"
    elif (binSeg[:2] == "10"):
        return "Clase B"
    elif (binSeg[0] == "0"):
        return "Clase A"
    elif (firstSegment < 256):
        return "Clase E"
    else:
        return "No es valido"


def getSubnetMask(ip):
    # gets subnet mask bits from the ip and turns it into an integer for later use
    subnet = int(ip.split('/')[1])
    # Initializes counter for the 32 bits in the subnet mask
    count = 31
    # Initializes variable to store the subnet mask in binary
    binMask = ""
    try:
        while (count >= 0):
            # If there's bits left in the subnet variables it adds a 1 to the binary subnet mask and substract 1 from the subnet variable
            if (subnet > 0):
                subnet -= 1
                binMask = binMask + "1"
                # adds a dot every 8 bits
                if (count % 8 == 0):
                    binMask = binMask + "."
            # Keeps adding 0s to the subnet mask while subnet = 0 and count >= 0
            else:
                binMask = binMask + "0"
                if (count % 8 == 0) & (count > 0):
                    binMask = binMask + "."
            count -= 1
        # Splits the binary subnet mask into 8 bit segments (separated by the dot)
        binMaskSegmented = binMask.split(".")
        # Initializes decimal subnet mask variable
        decMask = ""
        # Iterates through each of the 8 bit segments and converts them to decimal with Python's native int method
        for segment in binMaskSegmented:
            decMask = decMask + str(int(segment, 2)) + "."  # adds dot at the end for subnet mask syntax
        decMask = decMask[:-1]  # removes last extra dot
    except:
        decMask = "Numero invalido de bits para la mascara de subred"
    return decMask


def getHostSegment(ip):
    return "na"


def getNetworkSegment(ip):
    return "na"


def getFirstAddress(ip):
    return "na"


def getLastAddress(ip):
    return "na"


def getNetworkAddress(ip):
    ipSub = ip.split("/")  # Splits ip between ip segments and subnet bits
    ipSegments = ipSub[0].split(".")  # Splits ip segments
    subnet = int(ipSub[1])  # Gets subnet bits
    binIp = ""  # Initializes binary ip variable
    # Converts each segment from decimal to binary
    for segment in ipSegments:
        binSeg = bin(int(segment))
        binSeg = binSeg.split("b")[1]  # Eliminates the 0b prefix
        if (len(binSeg) < 8):
            temp = ""
            for i in range(0, 8 - len(binSeg)):
                temp = temp + "0"
            binSeg = temp + binSeg
        binIp = binIp + binSeg
    netAddressBinTemp = binIp[:subnet]
    count = 32 - subnet
    while (count > 0):
        netAddressBinTemp = netAddressBinTemp + "0"
        count -= 1
    netAddress = str(int(netAddressBinTemp[0:8], 2)) + "." + str(int(netAddressBinTemp[8:16], 2)) + "." + str(
        int(netAddressBinTemp[16:24], 2)) + "." + str(int(netAddressBinTemp[24:32], 2))
    return netAddress


def getBroadcastAddress(ip):
    ipSub = ip.split("/")
    ipSegments = ipSub[0].split(".")
    subnet = int(ipSub[1])
    binIp = ""
    for segment in ipSegments:
        binSeg = bin(int(segment))
        binSeg = binSeg.split("b")[1]
        if (len(binSeg) < 8):
            temp = ""
            for i in range(0, 8 - len(binSeg)):
                temp = temp + "0"
            binSeg = temp + binSeg
        binIp = binIp + binSeg
    netAddressBinTemp = binIp[:subnet]
    count = 32 - subnet
    while (count > 0):
        netAddressBinTemp = netAddressBinTemp + "1"
        count -= 1
    netAddress = str(int(netAddressBinTemp[0:8], 2)) + "." + str(int(netAddressBinTemp[8:16], 2)) + "." + str(
        int(netAddressBinTemp[16:24], 2)) + "." + str(int(netAddressBinTemp[24:32], 2))
    return netAddress


def checkIp(ip):
    try:
        ipsegment, subnet = ip.split("/")[0], ip.split("/")[1]
        if len(ip.split("/")) > 2:
            return False
        if (int(subnet) < 1) | (int(subnet) > 32):
            return False
        if len(ipsegment.split(".")) != 4:
            return False
        for x in ipsegment.split("."):
            if int(x) > 255:
                return False
    except:
        return False
    return True

def calculateIPv4():
    while True:
        ip = input("Ingrese la dirección IPv4 a probar (ej: 192.168.0.1/24 ) o ingrese x para salir: ")
        if ip == "x":
            break
        if checkIp(ip):
            print("\nClase de la dirección: " + getClass(ip))
            print("Mascara de Subred: " + getSubnetMask(ip))
            print("Segmento Red: " + getNetworkSegment(ip))
            print("Segmento Host: " + getHostSegment(ip))
            print("Primera Dirección: " + getFirstAddress(ip))
            print("Ultima Dirección: " + getLastAddress(ip))
            print("Dirección de Red: " + getNetworkAddress(ip))
            print("Dirección de Difusión: " + getBroadcastAddress(ip) + "\n")
        else:
            print("Dirección IPv4 inválida\n")

calculateIPv4()
