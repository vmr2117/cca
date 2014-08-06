def fnv32_hash(string):
    """
    32 bit FNV hash of the given string.
   
    Parameters
    ----------
    string: str
        string to hash.
   
    Return
    ------
    h: int
        32 bit FNV hash of the input string.
   
    """
    h = 2166136261
    prime_32 = 16777619
    uint32_max = 2**32
    for octet in string:
        h = h ^ ord(octet)
        h = (h * prime_32) % uint32_max
    return h;

def fnv64_hash(string):
    """
    64 bit FNV hash of the given string.
   
    Parameters
    ----------
    string: str
        string to hash.
   
    Return
    ------
    h: int
        64 bit FNV hash of the input string.
   
    """
    h = 14695981039346656037L
    prime_64 = 1099511628211
    uint64_max = 2**64
    for octet in string:
        h = h ^ ord(octet)
        h = (h * prime_64) % uint64_max
    return h;

def fnv_hash(string, bits=32):
    """
    'bits'-bit FNV hash of string . XOR folds the the next larger FNV hash
    to achieve the desired bit width.
   
    Parameters
    ----------
    string: str
        string to hash.
    bits: int
        bit width of the hash.
   
    Return
    ------
    h: int
        'bits'-bit FNV hash of the input string.
    """
    assert ((bits > 1) and (bits <= 64)), 'Unsupported bit width {}'.format(bits)
   
    h = None
    if bits > 32: h = fnv64_hash(string)
    else: h = fnv32_hash(string)

    if bits not in [32, 64]:
        mask = (1 << bits) - 1
        h = (h >> bits) ^ (h & mask)
    return h
