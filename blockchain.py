#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha256


def updatehash(*args):
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return str(
            "Block#: %s\n"
            "Hash: %s\n"
            "Previous hash: %s\n"
            "Data: %s\n"
            "Nonce: %s\n"
            % (
                self.number,
                self.hash(),
                self.previous_hash,
                self.data,
                self.nonce
            )
        )


class Blockchain():
    # The difficulty is a measure of how difficult it is to mine a Bitcoin block
    difficulty = 4

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append(
            {
                'hash': block.hash(),
                'previous': block.previous_hash,
                'number': block.number,
                'data': block.data,
                'nonce': block.nonce
            }
        )


def main():
    test_block = Block("Hello!!!", 1)
    print(test_block)


if __name__ == "__main__":
    main()
