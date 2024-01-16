# README
English | [Português](README_pt.md)


## OSINT-Steam

This repository contains a Python script designed for Open Source Intelligence (OSINT) on Steam profiles. It extracts detailed information such as name/nickname, avatar, real name, location, recent activity, level, and status of the Steam profile.

[![Visualizações do Repositório](https://667b0caf-a9d5-4b83-ae7c-c08ab5ecc45d-00-2ptar1l9fkkhe.kirk.replit.dev/link/kik)](https://github.com/kensdy/OSINT-Steam)

### Usage

1. **Clone the Repository:**
   - Clone this repository to your local environment using the following command:

   ```bash
   git clone https://github.com/kensdy/OSINT-Steam/
   cd OSINT-Steam
   ```

2. **Install Dependencies:**
   - Before running the script, install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   - Execute the script in a Python environment.
   - The script will prompt you to enter the desired Steam profile URL.

   ```bash
   python main.py
   ```

4. **Enter the Steam Profile URL:**
   - Input the Steam profile URL when prompted.

### Extracted Information

- **Name/Nickname:** Steam profile name or nickname.
- **Avatar:** Direct link to the avatar image.
- **Real Name:** Real name associated with the profile (if available).
- **Location:** Location indicated on the Steam profile (if available).
- **Recent Activity:** Time of the most recent activity on the Steam profile.
- **Level:** Steam profile level.
- **Status:** Current status of the Steam profile.

### Notes

- Ensure compliance with Steam's Terms of Service when using this script to avoid violations.
- In case of an error accessing the Steam profile, the corresponding status code will be displayed.

We hope this script proves useful for efficiently obtaining specific information from Steam profiles. If you have any questions or suggestions for improvement, feel free to contribute or get in touch.
