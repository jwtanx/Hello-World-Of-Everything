from numpy import uint32


def fnv1a32(data: bytes):
    hash = uint32(2166136261)
    for byte in data:
        hash ^= uint32(byte)
        hash *= uint32(16777619)
    return hash


print(fnv1a32("foo"))

