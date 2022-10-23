# We parse the packets exactly as in Part A.
# And then use a recursive method to calculate the 
# value for the packet tree.
import time
from dataclasses import dataclass
from typing import List, Optional
from math import prod


@dataclass
class Packet:
    n_bits: int
    version: int
    packet_type: int
    val: Optional[int] = None
    sub_packets: Optional[List["Packet"]] = None


def parse_packet(bit_str: str, packet_start: int) -> Packet:
    i = packet_start
    
    version = int(bit_str[i:i+3], 2)
    i += 3

    packet_type = int(bit_str[i:i+3], 2)
    i += 3

    if packet_type == 4:
        return parse_literal_packet(bit_str, packet_start, i, version, packet_type)
    
    return parse_operator_packet(bit_str, packet_start, i, version, packet_type)


def parse_literal_packet(bit_str: str, packet_start: int, i: int, version: int, packet_type: int) -> Packet:
    lit_str = ""
    while bit_str[i] == "1":
        lit_str += bit_str[i+1:i+5]
        i += 5
    lit_str += bit_str[i+1:i+5]
    i += 5

    n_bits = i - packet_start
    val = int(lit_str, 2)
    
    return Packet(version=version, packet_type=packet_type, n_bits=n_bits, val=val)


def parse_operator_packet(bit_str: str, packet_start: int, i: int, version: int, packet_type: int) -> Packet:
    length_type = bit_str[i]
    i += 1

    if length_type == "0":
        len_sub_packets = int(bit_str[i:i+15], 2)
        i += 15

        sub_packets = []
        while len_sub_packets > 0:
            sub_packet = parse_packet(bit_str, i)
            
            i += sub_packet.n_bits
            len_sub_packets -= sub_packet.n_bits
            
            sub_packets.append(sub_packet)


        n_bits = i - packet_start
        return Packet(version=version, packet_type=packet_type, n_bits=n_bits, sub_packets=sub_packets)

    n_sub_packets = int(bit_str[i:i+11], 2)
    i += 11

    sub_packets = []
    while n_sub_packets > 0:
        sub_packet = parse_packet(bit_str, i)

        i += sub_packet.n_bits
        n_sub_packets -= 1

        sub_packets.append(sub_packet)

    n_bits = i - packet_start
    return Packet(version=version, packet_type=packet_type, n_bits=n_bits, sub_packets=sub_packets)


def value(packet: Packet) -> int:
    match packet.packet_type:
        case 0:
            return sum(map(value, packet.sub_packets))
        case 1:
            return prod(map(value, packet.sub_packets))
        case 2:
            return min(map(value, packet.sub_packets))
        case 3:
            return max(map(value, packet.sub_packets))
        case 4:
            return packet.val
        case 5:
            p1 = packet.sub_packets[0]
            p2 = packet.sub_packets[1]
            return int(value(p1) > value(p2))
        case 6:
            p1 = packet.sub_packets[0]
            p2 = packet.sub_packets[1]
            return int(value(p1) < value(p2))
        case 7:
            p1 = packet.sub_packets[0]
            p2 = packet.sub_packets[1]
            return int(value(p1) == value(p2))


if __name__ == "__main__":
    t_start = time.perf_counter()
    with open("inputs/16.txt") as f:
        line = f.readline().strip()
        bit_str = "".join(format(int(c, 16), "04b") for c in line)


    packet = parse_packet(bit_str, 0)
    print(f"Ans - {value(packet)}, Time - {(time.perf_counter() - t_start) * 1000}ms")
