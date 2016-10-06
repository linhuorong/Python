import bitcoin

# Generate a random private key
valid_private_key = 'False while not valid_private_key:'
#private_key = bitcoin.random_key()

# Method 1	get address from private key
private_key = '55edfa908a5417332e4898634e2efab16c67dcf520d1a5fb35b6e4eb52b2e8ac'



decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
valid_private_key = 0 < decoded_private_key < bitcoin.N

print "Col rule                     is: |----5---10--------20--------30--------40--------50--------60--------70--------80--------90-------100|"
print "Private Key (hex)            is: ", private_key
print "Private Key (decimal)        is: ", decoded_private_key

# Convert private key to WIF format
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print "Private Key (WIF)            is: ", wif_encoded_private_key

# Method 2    get address from private key
wif_encoded_private_key = '5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn'
decoded_private_key = bitcoin.decode_privkey(wif_encoded_private_key)
print "Private Key (decimal)        is: ", decoded_private_key

#wif_encoded_private_key = 'KxFC1jmwwCoACiCAWZ3eXa96mBM6tb3TYzGmf6YwgdGWZgawvrtJ'
wif_encoded_private_key = '5J3mBbAH58CpQ3Y5RNJpUKPE62SQ5tfcvU2JpbnkeyhfsYB1Jcn'
wif_encoded_private_key = '5HpHagT65TZzG1PH3CSu63k8DbpvD8s5ip4nEB3kEsreAnchuDf'



decoded_private_key = bitcoin.decode_privkey(wif_encoded_private_key)
print "Private Key (decimal)        is: ", decoded_private_key



# Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'
print "Private Key Compressed (hex) is: ", compressed_private_key

# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
print "Private Key (WIF-Compressed) is: ", wif_compressed_private_key


# Multiply the EC generator point G with the private key to get a public key point
#public_key = bitcoin.base10_multiply(bitcoin.G, decoded_private_key)
public_key = bitcoin.multiply(bitcoin.G, decoded_private_key)
print "Public Key (x,y) coordinates is:", public_key

# Encode as hex, prefix 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key,'hex') 
print "Public Key (hex)             is:", hex_encoded_public_key

# Compress public key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
		compressed_prefix = '02' 
else:
    compressed_prefix = '03'    
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16) 
print "Compressed Public Key (hex)  is:", hex_compressed_public_key

# Generate bitcoin address from public key
print "Bitcoin Address (b58check)   is:", bitcoin.pubkey_to_address(public_key)

# Generate compressed bitcoin address from compressed public key
print "Compressed Bitcoin Address (b58check) is:", bitcoin.pubkey_to_address(hex_compressed_public_key)