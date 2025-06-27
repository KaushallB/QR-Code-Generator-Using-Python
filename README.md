# QR-Code-Generator-Using-Python

I came up with this idea to create a QR code generator because QR codes are extremely useful in everyday life whether for sharing website links, Wi-Fi credentials, contact information, or plain text. My goal was to design a tool that is both practical and easy to use, allowing anyone to generate custom QR codes offline and keep them organized for quick access.

---

##  Features

- Generate QR codes for:
  - URLs
  - Plain text
  - Email addresses (mailto)
  - Wi-Fi credentials
  - Virtual Card contact information
- Customize QR code color, background color, box size, and border size
- All QR codes are automatically sorted into subfolders by type on your Desktop
- Works entirely offline—no internet connection required
- Interactive, user-friendly prompts

---

##  How to Setup and Run

### 1. Install Python

**Recommended (Windows):**

- Open the Microsoft Store
- Search for **Python 3.11** (or latest)
- Click **Get** to install
- After installation, you should be able to run `python` from Command Prompt

**Alternative:**  
Download from [python.org](https://www.python.org/downloads/) and ensure "Add Python to PATH" is selected.

**Verify installation:**
```bash
python --version
```

#### **macOS**
- Open Terminal and run:
```bash
brew install python
```
(If you do not have Homebrew, install it from [brew.sh](https://brew.sh/), or download Python directly from [python.org](https://www.python.org/downloads/).)

#### **Linux (Ubuntu/Debian)**
- Open Terminal and run:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

- For other distributions, use your package manager or download from [python.org](https://www.python.org/downloads/).

**Verify installation (all platforms):**
```bash
python --version
or
python3 --version
```

---


### 2. Install Required Packages
```bash
pip install qrcode Pillow
```

### If you encounter a "pip not found" error, use:
```bash
python -m pip install qrcode
python -m pip install Pillow
```

### 3. Clone or Download the Repository

```bash
git clone https://github.com/KaushallB/QR-Code-Generator-Using-Python
cd QR-Code-Generator-Using-Python
```

Or download the ZIP and extract it.

---

### 4. Run the Script

python qrgenerator.py


---

### 5. Follow the Prompts

- Select the QR code type (URL, Text, Email, Wi-Fi, vCard)
- Enter the required information
- Customize the QR code appearance or press Enter to use defaults
- The QR code image will be saved in a folder named `QR_Codes_Offline_Images` on your Desktop, organized by type

---

### 6. Access Your QR Codes

- The script will attempt to open the generated image automatically
- You can also browse to the `QR_Codes_Offline_Images` folder on your Desktop to view and manage your QR codes

---

