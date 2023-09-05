# SFTP Desktop App 🚀

Welcome to the SFTP Desktop App repository! This application provides a user-friendly interface for establishing secure SFTP connections, allowing you to easily upload and download files.

## Features 🌟
- 🔒 Secure SFTP connections
- 🔄 Easy uploading & downloading
- 💾 Save credentials for faster reconnections
- 📁 View server directory and contents

## Getting Started 🛠

### Prerequisites 📋
- Python 3.x installed on your machine.
- The `paramiko` library. Install it using:
  ```bash
  pip install paramiko
  ```
- `tkinter` for the GUI. It usually comes pre-installed with Python. If not, refer to your OS's package manager to install it.

### Running the App 🚴

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/SFTP-Desktop-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SFTP-Desktop-App
   ```
3. Run the main script:
   ```bash
   python main.py
   ```

## Testing Connection 🔌
1. Enter your SFTP server details, including hostname, port, username, and password.
2. Click on the "Connect" button.
3. If successful, you'll see a message indicating a successful connection, and you'll be able to view the server's directory and files.
4. To test an upload, click on the "Upload" button and select a file from your local machine.
5. To download, select a file from the server's list and click the "Download" button.

📌 **Note**: Ensure your SFTP server is accessible and accepts connections on the specified port. The default port is 22, but some servers might use different ports.

## ⚠️Disclaimer⚠️
This SFTP Desktop App is designed for educational and legitimate purposes only. Do not use this tool to access SFTP servers for which you do not have explicit permission to connect. Unauthorized access to computer systems and networks is illegal and can result in severe penalties. Always respect privacy and ownership rights. The creator and contributors of this tool are not responsible for any misuse or potential damage arising from its use.

## Contributing 🤝

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## License 📄

This project is licensed under the MIT License. See the `LICENSE` file for details.
