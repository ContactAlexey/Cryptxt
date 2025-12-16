#!/usr/bin/env python3

import random
import os
import sys

def encrypt_file(file_name):
    input_path = os.path.abspath(file_name)

    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    encryption_number = random.randint(1, 99)
    result = []

    for char in content:
        code = ord(char)
        binary = bin(code)[2:]
        result.append(str(int(binary, 2) * encryption_number))

    encrypted_text = " ".join(result) + f" {encryption_number}"

    output_path = os.path.join(os.path.dirname(input_path), "hidden_message.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(encrypted_text)

    return output_path


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: cryptxt <file>")
        sys.exit(1)

    try:
        output = encrypt_file(sys.argv[1])
        print(f"Encryption completed: {output}")
    except Exception as e:
        print(f"Error: {e}")
