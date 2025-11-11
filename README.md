![welcome](https://github.com/user-attachments/assets/6a58ea1e-b5ce-4d88-85db-a6e90d746dc4)

# AToolsFix

Version: 1.1.0b

Author: RedPiar

Development time for this version: 6 hours

Comment:

This script currently cannot replace the old AminoTools, but our version works reliably and will continue to improve over time!

## Contents

1. [Dependencies](#installation)
2. [Running the Script](#running)
3. [Class and Method Descriptions](#class-and-method-descriptions)
    1. [AToolsFix Class](#atoolsfix)
        1. [login](#login)
        2. [Functions](#functions)
4. [Change Log](#change-log)
5. [Contacts](#contacts)

## Installation

Before running the script, make sure to install the necessary dependencies. The script will automatically install them if they are missing.

```python
try:
    from colorama import Fore, init
    from utils.Users import Users
except:
    os.system("pip install colorama")
    os.system("pip install sqlite3")
    input("Press Enter to restart script: ")
    sys.exit()
```

## Running
To run the script, execute the following command in CMD:

```
python AToolsFix.py
```

## Class and Method Descriptions
### AToolsFix Class
A class that provides functionality for interacting with the Amino API.

### login
Checks for the presence of the sid.txt file for authentication. If the file is not found, it prompts the user for their email and password to log in.

After a successful login, the sid.txt file is created. For subsequent logins, your SID will be used for authentication. When the SID expires, you will need to re-enter your email and password.

```python
def login(self):
    if os.path.exists("./sid.txt"):
        self.loginSID()
    else:
        email = input("[!] Enter your Email(AccountEmail): ")
        password = input("[!] Enter your Password(AccountPassword): ")
        print("Trying to log in to your account...")
        clientDATA = self.client.login(email, password)
        status = self.checkAccountLogin(LoginBySid=False)
        if status:
            os.system("cls")
            self.CreateSidFile(data=clientDATA)
            self.Functions()
```

Additionally, after each login attempt, a test request will be sent to Amino servers via checkAccountLogin.

```python
def checkAccountLogin(self, LoginBySid):
    try:
        self.client.get_wallet_info().totalCoins
        print("Login checked is True!")
        return True
    except:
        print("Login failed! Trying again...")
        time.sleep(3)
        if LoginBySid:
            os.remove("sid.txt")
        os.system("cls")
        self.login()
        return False
```

### Functions
Provides a menu for performing various tasks.

To select a function, enter the corresponding number.

```python
def Functions(self):
    os.system("cls")
    print("""
____ObjectIDs____
1. get my communities
2. get Community ID from link
3. get UserID from link
4. get UserID from community
5. get PostID from community
______Users______
6. get all users(saved to file)
7. get online users(saved to file)
8. get user followers
9. get user following
10. get user info
_____Scripts_____
11. Parse communities users
""")
```

# Change-Log

The project on GitHub updates with a delay (5-10 minutes)

## [1.1.0] - 2024-08-05
### Added
- New Section: Account
- New Feature: ProfileInfo
- New Feature: wallet
- New Feature: GetChatThreads
- logging
- settings
- settings[logging]
- settings[QuickLogin]

### Fixed
- Updated code readbility and understanding/ The functions were divided into sections

### Innovations
- You can now enable and disable logging through the settings.ini file. By default, logging is enabled (True), but you can disable it (False).
- You can set up quick login to your account in case the SID expires. To do this, go to settings.ini and change status to True, and also provide your email and password.

### Description
Functions:
- ProfileInfo - The first version of the function, displays some information (for example, your UserId).
- Wallet - Shows the balance of your wallet.
- GetChatThreads - Displays your global chats (Maximum=25).

Logging:

Logging is used to display warnings and for debugging, but currently, logging does not respond to exceptions.

Settings:

- logging:
    - Status: There are two statuses (True, False). Set the flag to True to enable, and set the flag to False to disable.
    - log_to_file: Log_to_file: There are two statuses (True, False). If enabled, logging will be written to a .log file.
- QuickLogin - You can set up quick login to your account in case the SID expires:
    - Status: There are two statuses (True, False). Set the flag to True to enable, and set the flag to False to disable.
    - Email: Your email for quick login.
    - Password: Your account password.

## [1.0.5] - 2024-08-03
### Added
- New Feature: get my communities
- New Section: Scripts
- New Script: Parse communities users
- Check version && Notification for new version AToolsFix

### Description
- Get my communities - Retrieves all your communities and the necessary information about them, then outputs it to the console.
- Section Scripts - Section for future embedded scripts.
- Parse communities users - Retrieves all users from all your communities (up to 10K users per community), then records them in the DataBase.db file in the All_users table.
- Check version && Notification for new version AToolsFix - When a new version appears on GitHub, the script will notify you about it upon launch.

# Contacts
| **Category**   | **Description** | **Link** |
|----------------|-----------------|----------|
| **My Contacts**|                 |          |
| Telegram       |                 | [Telegram](https://t.me/Redpiar) |
| TG Channel     |                 | [TG Channel](https://t.me/BotesForTelegram) |
| TikTok         |                 | [TikTok](https://www.tiktok.com/@redpiar) |
| **Reference**  | **AminoFixFix** |          |
| Author         |                 | [Author](https://github.com/imperialwool) |
| GitHub         |                 | [GitHub](https://github.com/imperialwool/Amino.fix.fix/tree/main) |
| Docs           |                 | [Docs](https://aminofixfix.readthedocs.io/en/latest/) |


