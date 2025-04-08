
🧩 Tool Check Puzzle By Mr Ciphers
================================================

🔐 DESCRIPTION:
The tool checks if the Bitcoin private key matches the list of wallets available in `base_balance.txt`. If found, the tool will send a Telegram alert, save the result and automatically transfer BTC (if any).

▶️ HOW TO RUN THE TOOL:
1. Install Python 3.8+ and PyQt5:

pip install -r requirements.txt

2. Run the tool with the command:
python main.py

3. Open the interface and click “Start Scan” to check the private key.

🛠 Note:
- The `base_balance.txt` file must contain a list of wallet addresses (1 address per line).
- Matching results will be saved to `balance_found.txt` and sent to Telegram.
- The tool scans using the random key brute-force algorithm (for research purposes).

📦 REQUIREMENTS:
- Python 3.8+
- PyQt5
- bit

💼 COPYRIGHT:
Copyright © 2025 Mr Ciphers. All rights reserved.
Not for commercial use without permission.

❤️ Made with love by Mr Ciphers.
"""

# Write README.txt file
with open("README.txt", "w", encoding="utf-8") as f:
f.write(readme_content.strip())

"✅ Created README.txt file with instructions and copyright Mr Ciphers."
