from checksumdir import dirhash as checksumhash
from dirhash import dirhash
import os
from merklelib import MerkleTree, beautify, export, hashlib


def build_dir_hash(folder):
    # init
    HASH_TYPE = "sha256"

    # hash
    dir_sha256_all = dirhash(folder, HASH_TYPE)
    dir_sha256_js = dirhash(folder, HASH_TYPE, match=["*.js"])
    dir_sha256_js_none = dirhash(folder, HASH_TYPE, ignore=["*.js"])

    # checksums
    checksum_sha256_all = checksumhash(folder, HASH_TYPE)

    # return
    return [dir_sha256_all, dir_sha256_js, dir_sha256_js_none, checksum_sha256_all]

def build_file_hash(file):
    sha256_hash = hashlib.sha256()
    with open(file, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def prove(x, y):
    if x == y:
        print("proved!")


if __name__ == '__main__':
    # find the folder to merklize
    folder = os.environ.get('MERKLIZE_ROOT_FOLDER')
    logs = os.environ.get("MERKLIZE_COMMIT_FILE")

    # hashes
    hash_log = build_file_hash(logs)
    hash_folder = build_dir_hash(folder)
    print(hash_folder)

    # merkle tree
    tree = MerkleTree(hash_folder)

    # merklize
    beautify(tree)

    # export
    export(tree, filename='transactions', ext='jpg')


