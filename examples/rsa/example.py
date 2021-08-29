from simple_ciphers.ciphers.rsa import RSACipher

cipher = RSACipher()

# Enryption / Decryption using the default block size
message_length, block_size, encrypted_blocks = cipher.encrypt("This is a test 123")
decrypted_message = cipher.decrypt(message_length, block_size, encrypted_blocks)
print(decrypted_message)

# Enryption / Decryption using a different block size
message_length, block_size, encrypted_blocks = cipher.encrypt("This is a test 123", blockSize=25)
decrypted_message = cipher.decrypt(message_length, block_size, encrypted_blocks)
print(decrypted_message)