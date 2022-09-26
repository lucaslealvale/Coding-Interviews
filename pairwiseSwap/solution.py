def swap_odd_even_bits(x: int) -> int: 
    odd = (x & 0b10101010101010101010101010101010) >> 1
    even = (x & 0b01010101010101010101010101010101) << 1
    return odd | even
