import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HEADER = ("Original Script By : EstebanZxx (github.com/EstebanZxx/X-Tools)\n"
          "Keys & Method Credit : FrontierTM (github.com/FrontierTM/Pantegnos)\n"
          "This Version Is Modified (paste input, updated keys, strict padding)\n"
          "=====================================\n"
          "Result Decrypt : ")

# Keys used by NetMod. Add more here if you find them.
KEYS = [b"<n3t5yn4^n3tm0d>", b"_netsyna_netmod_", b"nicetrybuddygoon"]


def clean_payload(text: str):
    """Return (scheme, base64_payload). Only the 'nm-xxx://' part is removed;
    anything after it (including 'sv/') is part of the base64 data."""
    text = "".join(text.split())                      # strip spaces/newlines
    scheme = ""
    if "://" in text:
        scheme, text = text.split("://", 1)
    return scheme, text + "=" * (-len(text) % 4)


def decrypt_aes_ecb_128(ciphertext: bytes, key: bytes) -> str:
    plaintext = unpad(AES.new(key, AES.MODE_ECB).decrypt(ciphertext), 16)  # strict PKCS7
    return plaintext.decode("utf-8")


def decrypt_config(text: str) -> str:
    scheme, payload = clean_payload(text)
    ciphertext = base64.b64decode(payload)

    if len(ciphertext) % 16:
        raise ValueError("invalid config: data length is wrong (check you pasted the whole link)")

    for key in KEYS:
        try:
            result = decrypt_aes_ecb_128(ciphertext, key)
            return f"{scheme}://{result}" if scheme else result
        except (UnicodeDecodeError, ValueError):
            continue
    raise ValueError("no known key could decrypt this config")


def main():
    print("NM Config Decryptor")
    print("Paste your config (nm-xxx://... or base64) and press Enter.")
    print("Leave it empty and press Enter to quit.\n")

    while True:
        try:
            config = input("Config > ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not config:
            break
        try:
            print("\n" + HEADER + decrypt_config(config) + "\n")
        except Exception as e:
            print(f"\n[FAIL] {e}\n")

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
