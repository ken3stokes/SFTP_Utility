import paramiko
from tkinter import Tk, filedialog, simpledialog, messagebox, Label, Entry, Toplevel, Button, Listbox

class SFTPClient:
    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, port=self.port, username=self.username, password=self.password)

    def disconnect(self):
        if self.client:
            self.client.close()

    def list_directory(self, path="."):
        sftp = self.client.open_sftp()
        files = sftp.listdir(path)
        sftp.close()
        return files

    def download_file(self, remote_path, local_path):
        sftp = self.client.open_sftp()
        sftp.get(remote_path, local_path)
        sftp.close()

    def upload_file(self, local_path, remote_path):
        sftp = self.client.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()

class SFTPDialog(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.sftp_client = None
        self.create_widgets()

    def create_widgets(self):
        self.host_label = Label(self, text="Host:")
        self.host_label.grid(row=0, column=0)

        self.host_entry = Entry(self)
        self.host_entry.grid(row=0, column=1)

        self.username_label = Label(self, text="Username:")
        self.username_label.grid(row=1, column=0)

        self.username_entry = Entry(self)
        self.username_entry.grid(row=1, column=1)

        self.password_label = Label(self, text="Password:")
        self.password_label.grid(row=2, column=0)

        self.password_entry = Entry(self, show="*")
        self.password_entry.grid(row=2, column=1)

        self.port_label = Label(self, text="Port:")
        self.port_label.grid(row=3, column=0)

        self.port_entry = Entry(self)
        self.port_entry.insert(0, "22")
        self.port_entry.grid(row=3, column=1)

        self.connect_button = Button(self, text="Connect", command=self.connect_to_sftp)
        self.connect_button.grid(row=4, column=0, columnspan=2)

        self.listbox = Listbox(self, width=40, height=10)
        self.listbox.grid(row=5, column=0, columnspan=2)

        self.download_button = Button(self, text="Download", command=self.download_file_from_sftp)
        self.download_button.grid(row=6, column=0)

        self.upload_button = Button(self, text="Upload", command=self.upload_file_to_sftp)
        self.upload_button.grid(row=6, column=1)

    def connect_to_sftp(self):
        host = self.host_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        port = int(self.port_entry.get())

        self.sftp_client = SFTPClient(host, username, password, port)
        try:
            self.sftp_client.connect()
            self.refresh_file_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect. Error: {e}")

    def refresh_file_list(self):
        files = self.sftp_client.list_directory()
        self.listbox.delete(0, "end")
        for file in files:
            self.listbox.insert("end", file)

    def download_file_from_sftp(self):
        selected_file = self.listbox.get(self.listbox.curselection())
        if not selected_file:
            messagebox.showerror("Error", "Please select a file to download.")
            return

        save_path = filedialog.asksaveasfilename(title="Save File As", initialfile=selected_file)
        if save_path:
            try:
                self.sftp_client.download_file(selected_file, save_path)
                messagebox.showinfo("Success", "File downloaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download file. Error: {e}")

    def upload_file_to_sftp(self):
        file_path = filedialog.askopenfilename(title="Select File to Upload")
        if file_path:
            filename = file_path.split('/')[-1]
            try:
                self.sftp_client.upload_file(file_path, filename)
                messagebox.showinfo("Success", "File uploaded successfully!")
                self.refresh_file_list()  # Refresh the list after uploading.
            except Exception as e:
                messagebox.showerror("Error", f"Failed to upload file. Error: {e}")

def main():
    root = Tk()
    root.title("SFTP Client App")
    SFTPDialog(root)
    root.mainloop()

if __name__ == "__main__":
    main()
