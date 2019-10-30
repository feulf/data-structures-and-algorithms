import hashlib

hashed_list = [None] * 10  # create an array of None


def key_position(key):
    string = key.encode()  # convert to bits
    hashed_key = hashlib.sha256(string)  # hash the string
    hex_digest = hashed_key.hexdigest()  # get the hex value
    int_digest = int(hex_digest, 16)  # convert to int
    return int_digest % len(hashed_list)  # run the modulo of the length of the array


def insert(key, value):
    index = key_position(key)
    hashed_list[index] = value


def read(key):
    index = key_position(key)
    return hashed_list[index]


insert("Satoshi Nakamoto", "Unknown")
insert("Federico", "5.7")
insert("Joe", "6.1")

print(read("Satoshi Nakamoto"))
print(read("Federico"))
print(read("Joe"))
