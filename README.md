# Netmod Config Unlocker

A small Python tool that decrypts NetMod `.nm` configs and `nm-xxx://` links
(for example `nm-trojan://`, `nm-vless://`, `nm-vmess://`). Paste the config, get the plain text.

## Features
- Decrypts `nm-xxx://...` links and raw base64 configs
- Tries several known NetMod keys automatically
- Works on Windows, Linux, macOS and Android (Termux)
- Nothing is saved to disk. Everything stays in the terminal.

## Installation
```bash
git clone https://github.com/suchira2000h/Netmod-Config-Unlocker-Oct-2026
cd Netmod-Config-Unlocker-Oct-2026
pip install -r requirements.txt
```
On Termux: `pkg install python -y` first.

## Usage
```bash
python nm_decrypt.py
```
1. Paste your `nm-xxx://...` link (or base64 config) and press Enter.
2. The decrypted config is printed.
3. Paste another one, or press Enter on an empty line to quit.

## How it works
NetMod encrypts configs with AES-128-ECB and PKCS7 padding, then base64-encodes them.
The script removes the `nm-xxx://` prefix, base64-decodes the rest, and tries each known key
until the padding check succeeds.

## Disclaimer
For educational purposes and for recovering configs you own or have permission to open.
Do not use it to access, share or resell other people's private configs.
Never post real configs or decrypted output publicly. They contain server addresses and credentials.

## Credits
This is a **modified version** of the original script. Full credit to the original authors:

- Original script idea: [EstebanZxx/X-Tools](https://github.com/EstebanZxx/X-Tools) (GPL-3.0)
- Key list and method: [FrontierTM/Pantegnos](https://github.com/FrontierTM/Pantegnos) (AGPL-3.0)

## License
GPL-3.0. See [LICENSE](LICENSE).
