from merklelib import MerkleTree, beautify, export
import os
from dirhash import dirhash
from checksumdir import dirhash as checksumhash

if __name__ == '__main__':
    # find the folder to merklize
    folder = os.environ.get('MERKLIZE_ROOT_FOLDER')

    # hash
    dir_sha256_all = dirhash(folder, "sha256")
    dir_sha256_js = dirhash(folder, "sha256", match=["*.js"])
    dir_sha256_js_none = dirhash(folder, "sha256", ignore=["*.js"])

    # checksums
    checksum_sha256_all = checksumhash(folder, "sha256")

    # merklize
    tree = MerkleTree([
        dir_sha256_all,
        dir_sha256_js,
        dir_sha256_js_none,
        checksum_sha256_all
    ])
    beautify(tree)

    # export
    export(tree, filename='transactions', ext='jpg')

