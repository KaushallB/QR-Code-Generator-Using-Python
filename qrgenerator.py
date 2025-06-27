import qrcode
import os
from datetime import datetime
from PIL import Image
from pathlib import Path

def get_user_choice():
    print("Choose QR code type:")
    print("1. URL")
    print("2. Plain Text")
    print("3. Email (mailto)")
    print("4. Wi-Fi Credentials")
    print("5. VirtualCard Contact")
    choice = input("Enter your choice (1-5): ")
    return choice

def get_data(choice):
    if choice == "1":
        url = input("Enter the URL: ")
        return url
    elif choice == "2":
        text = input("Enter the text: ")
        return text
    elif choice == "3":
        email = input("Enter email address: ")
        subject = input("Enter subject (optional): ")
        body = input("Enter body (optional): ")
        mailto_link = (
            f"mailto:{email}"
            f"?subject={subject}"
            f"&body={body}"
        )
        return mailto_link
    elif choice == "4":
        ssid = input("Wi-Fi SSID: ")
        password = input("Wi-Fi Password: ")
        wifi_format = (
            f"WIFI:T:WPA;"
            f"S:{ssid};"
            f"P:{password};;"
        )
        return wifi_format
    elif choice == "5":
        name = input("Full Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        vcard = (
            "BEGIN:VCARD\n"
            "VERSION:3.0\n"
            f"FN:{name}\n"
            f"TEL:{phone}\n"
            f"EMAIL:{email}\n"
            "END:VCARD"
        )
        return vcard
    else:
        print("Invalid choice, defaulting to plain text.")
        text = input("Enter the text: ")
        return text

def get_subfolder_name(choice):
    if choice == "1":
        return "Url_QR"
    elif choice == "2":
        return "Text_QR"
    elif choice == "3":
        return "Email_QR"
    elif choice == "4":
        return "Wifi_QR"
    elif choice == "5":
        return "Virtualcard_QR"
    else:
        return "Text_QR"


def customize_qr():
    fill_color = input("Enter QR color (Default Black): ")
    if not fill_color:
        fill_color = "black"
    else:
        fill_color = fill_color.lower() 

    back_color = input("Enter background color (Default White): ")
    if not back_color:
        back_color = "white"
    else:
        back_color = back_color.lower()

    box_size_input = input("Box size (Default 10): ")
    if not box_size_input:
        box_size = 10
    else:
        box_size = int(box_size_input)

    border_input = input("Border size (Default 4): ")
    if not border_input:
        border = 4
    else:
        border = int(border_input)

    return fill_color, back_color, box_size, border

def main():
    try:
        #getting Desktop path and main qr_codes folder
        desktop_path = Path.home() / 'Desktop'
        main_folder = desktop_path / 'QR_Codes_Offline_Images'

        #getting user choices and data
        choice = get_user_choice()
        data = get_data(choice)
        fill_color, back_color, box_size, border = customize_qr()

        #subfolder based on QR type
        subfolder_name = get_subfolder_name(choice)
        output_folder = main_folder / subfolder_name
        os.makedirs(output_folder, exist_ok=True)

        #generating a unique filename using timestamp
        date_str = datetime.now().strftime('%H_%M_%d_%m')
        filename = f"{subfolder_name}_{date_str}.png"
        file_path = output_folder / filename


        #creating and configuring QR code
        qr = qrcode.QRCode(box_size=box_size, border=border)
        qr.add_data(data)
        qr.make(fit=True)

        #generating QR image with custom colors
        image = qr.make_image(fill_color=fill_color, back_color=back_color)
        image.save(file_path)

        print(f"QR code saved to: {file_path}")

    except Exception as e:
        print("Error occurred:", e)

    #trying to open the image automatically
    try:
        Image.open(file_path).show()
    except Exception as e:
        print("Could not open image automatically:", e)

if __name__ == "__main__":
    main()
