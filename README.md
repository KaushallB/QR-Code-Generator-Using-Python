I came up with this idea to create a QR code generator because QR codes are extremely useful in everyday life, whether for sharing website links, Wi-Fi credentials, contact information, or plain text. My goal was to design a tool that is both practical and easy to use, allowing anyone to generate custom QR codes offline and keep them organized for quick access.

QR-Code-Generator-Using-Python
This project enables users to generate and organize QR code images for URLs, plain text, email addresses, Wi-Fi credentials, and vCard contacts. Generated QR code images are saved in organized folders on the user's Desktop for convenient access.

Features
Multiple QR Code Types: Supports generation of QR codes for URLs, plain text, email addresses (mailto), Wi-Fi credentials, and vCard contact information.

Customizable Appearance: Users can select QR code color, background color, box size, and border size.

Automatic Organization: Generated QR codes are sorted into subfolders by type on your Desktop.

Offline Operation: The tool works entirely offline; no internet connection is required for QR code generation.

User-Friendly: Interactive prompts and automatic file organization make it easy for anyone to use.


Prerequisites
1. Python Installation
Recommended Method (Windows):

Install Python via the Microsoft Store:

Open the Microsoft Store application.

Search for "Python 3.11" (or the latest available version).

Click "Get" to install.

After installation, you should be able to run python from the Command Prompt.

Alternative Method:

Download and install Python from the official website:

bash
https://www.python.org/downloads/
During installation, ensure that the "Add Python to PATH" option is selected.

Verification:

After installation, open Command Prompt and run:

bash
python --version
You should see the installed Python version displayed.

2. Required Python Packages
This project requires the following third-party Python packages:

qrcode

Pillow (for image handling)

To install these packages, open Command Prompt and execute:

bash
pip install qrcode
pip install Pillow
If you encounter a "pip not found" error, use the following commands:

bash
python -m pip install qrcode
python -m pip install Pillow
Usage Instructions
1. Download or Clone the Repository
Download the repository as a ZIP file and extract it, or clone it using Git:

bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
2. Navigate to the Project Directory
Open Command Prompt and change the directory to where the script is located:

bash
cd path/to/your/project
3. Run the Script
Execute the following command:

bash
python qrgenerator.py
4. Follow the On-Screen Prompts
Select the desired QR code type.

Enter the required information.

Customize the QR code appearance as desired, or press Enter to use default settings.

The script will generate and save the QR code image in a folder named QR_Codes_Offline_Images on your Desktop, organized by QR code type.

5. Accessing Generated QR Codes
The script will attempt to open the generated image automatically.

You can also manually browse to the QR_Codes_Offline_Images folder on your Desktop to view and manage your QR codes.
