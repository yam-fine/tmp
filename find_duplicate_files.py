import os
import hashlib


def find_duplicate_files(directory):
    file_hash_map = {}

    # Iterate through all files in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            # Calculate the hash of the file's contents
            with open(filepath, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()

            # Add the file path to the dictionary using its hash as the key
            if file_hash in file_hash_map:
                file_hash_map[file_hash].append(filepath)
            else:
                file_hash_map[file_hash] = [filepath]

    # Print
    for file_paths in file_hash_map.values():
        if len(file_paths) > 1:
            print(" ".join(file_paths))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python duplicate_finder.py <directory>")
    else:
        directory = sys.argv[1]
        find_duplicate_files(directory)
