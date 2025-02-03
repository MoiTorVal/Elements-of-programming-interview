# Precompute a lookup table to reverse the bits of an 8-bit integer
def generate_reverse_lookup_table():
    table = {}
    for i in range(65536): 
        reversed_bits = int(format(i, '016b')[::-1],2)
        table[i] = reversed_bits
    return table



PRECOMPUTED_REVERSE = generate_reverse_lookup_table()

def reverse_bit(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3 * mask_size) | PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2 * mask_size) | PRECOMPUTED_REVERSE[(x >> (2 * mask_size)) & bit_mask] << mask_size | PRECOMPUTED_REVERSE[(x >> (3 * mask_size)) & bit_mask])

print(reverse_bit(1))