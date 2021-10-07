Step 1: First the prover generates the public key by creating two 1024 bit distinct prime numbers. These numbers are used to calculate n(p*q) and the other half of the public key is selected by the prover(65537 in this case). These values are made public but the two prime numbers p and q along with the secret(plaintext) are kept safe.

Step 2: The prover then selects a random value(randon_val) and calculates ciphertexts for both the secret and the random value.

Step 3: Next the prover requests the verifier for a random exponent(r) which is chosen between 1 and e by the verifier and sent to the prover via the socket.

Step 4: The prover takes this r and calculates an encryption value(enc) involving plaintext, random_val and r. 

Step 5: The enc value with ciphertext and random_val_enc are sent to the verifier for verification. 

Note: No plaintext is ever shared by the prover with the verifier.

Step 6: At the end, the verifier computes two values from all the data received from the prover,

First value: (enc**e) % n
Second value: (random_val_enc*ciphertext**r) % n

If these two values are found equal, the prover has successfully proven that they know the plaintext.
