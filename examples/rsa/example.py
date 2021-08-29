from simple_ciphers.ciphers.rsa import RSACipher

cipher = RSACipher()

# Enryption / Decryption using the default block size
blocks, block_size, message_length = cipher.encrypt("This is a test 123")
decrypted_message = cipher.decrypt(blocks, block_size, message_length)
print(decrypted_message)

# Enryption / Decryption using a different block size
blocks, block_size, message_length = cipher.encrypt(
    "This is a test 123",
    block_size=25
)
decrypted_message = cipher.decrypt(blocks, block_size, message_length)
print(decrypted_message)
