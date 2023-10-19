import PySimpleGUI as sg
import paramiko

# sg.theme_previewer()
sg.theme('DarkTeal12')
class SFTPClient:

    def __init__(self, host, username, password, port=22):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(host, port, username, password)
        self.sftp = self.client.open_sftp()

    def list_files(self, path='.'):
        return self.sftp.listdir(path)

    def download(self, remote_path, local_path):
        self.sftp.get(remote_path, local_path)

    def upload(self, local_path, remote_path):
        self.sftp.put(local_path, remote_path)

    def close(self):
        self.sftp.close()
        self.client.close()

class SFTPDialog:

    def __init__(self):
        layout = [
            [sg.Text("Host:"), sg.Input(key="host")],
            [sg.Text("Username:"), sg.Input(key="username")],
            [sg.Text("Password:"), sg.Input(key="password", password_char="*")],
            [sg.Text("Port:"), sg.Input(key="port", default_text="22")],
            [sg.Button("Connect")],
            [sg.Listbox(values=[], size=(40, 10), key="filelist")],
            [sg.Button("Download"), sg.Button("Upload")]
        ]

        self.window = sg.Window("SFTP Client", layout)
        self.client = None

    def connect(self):
        values = self.window.read()[1]
        host = values["host"]
        username = values["username"]
        password = values["password"]
        port = int(values["port"])

        self.client = SFTPClient(host, username, password, port)
        filelist = self.client.list_files()
        self.window["filelist"].update(filelist)

    def download(self):
        # Implement the download logic, for simplicity, let's assume downloading to the current directory
        selected_file = self.window["filelist"].get()[0]
        self.client.download(selected_file, selected_file)

    def upload(self):
        # Implement the upload logic, for simplicity, assume uploading a file from the current directory
        selected_file = self.window["filelist"].get()[0]
        self.client.upload(selected_file, selected_file)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == "Connect":
                self.connect()

            if event == "Download":
                self.download()

            if event == "Upload":
                self.upload()

            if event == sg.WINDOW_CLOSED:
                break

        if self.client:
            self.client.close()

        self.window.close()

def main():
    dialog = SFTPDialog()
    dialog.run()

if __name__ == "__main__":
    main()
