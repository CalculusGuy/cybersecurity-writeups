 picoCTF Challenge Writeups

## 1. Tiny E RSA
**Category:** Cryptography | **Flag:** `picoCTF{t1ny_e_837d7226}`

**Vulnerability:** e = 20 is tiny. Took the 20th root of ciphertext directly.

```python
import gmpy2
m, exact = gmpy2.iroot(c, e)
print(bytes.fromhex(hex(m)[2:]))
```

---

## 2. ClusterRSA
**Category:** Cryptography | **Flag:** `picoCTF{mul71_rsa_3dd22eb2}`

**Vulnerability:** n has 4 small prime factors, fully factorable via factordb.com. Computed phi(n) for all 4 primes then standard RSA decryption.

---

## 3. Shift Registers (LFSR)
**Category:** Cryptography | **Flag:** `picoCTF{l1n3ar_f33dback_sh1ft_r3g}`

**Vulnerability:** LFSR seed = key & 0xFF — only 256 possible states. Brute forced all 256 and checked for `picoCTF{` prefix.

```python
for i in range(256):
    result = decrypt_lfsr(ct_bytes, i)
    if result.startswith(b'picoCTF{'):
        print(result.decode())
        break
```

---

## 4. Enhance
**Category:** Forensics | **Flag:** `picoCTF{3nh4nc3d_d0a757bf}`

**Vulnerability:** SVG file with flag hidden as white text at font-size 0.003px — invisible visually. Found by reading raw XML/page source.
