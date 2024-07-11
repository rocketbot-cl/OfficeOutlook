from win32com import client
import pandas as pd


class OutlookApp:
    """A class to interact with the Outlook application"""

    def __init__(self):
        self.app = client.Dispatch("Outlook.Application")
        self.instance = self.app.GetNamespace("MAPI")

    @classmethod
    def from_account(cls, account):
        """Create an instance of OutlookApp with the specified account"""
        outlook_instance = cls()
        for account in outlook_instance.instance.Accounts:
            if account.DisplayName == account:
                outlook_instance.instance.CurrentUser = account
                break
        return outlook_instance

    def get_folders(self, account_id=None):
        """Get the folders of the specified account"""
        # folders = self._get_current_folders()
        folders = self.instance.Folders
        return self._get_folders(folders, account_id)



    def _get_folders(self, folders, account_id, prefix_name="", prefix_id=""):
        """Get the folders of the specified account"""
        folders_list = []
        for folder in folders:
            if account_id is not None and folder.Store.StoreID != account_id:
                continue

            folder_name = prefix_name + folder.Name
            folder_id = prefix_id + folder.EntryID
            folders_list.append(
                {
                    "Name": folder_name,
                    "EntryID": folder_id,
                    "AccountID": folder.StoreID,
                    "AccountName": folder.Store.DisplayName,
                }
            )

            subfolders = self._get_folders(
                folder.Folders,
                account_id,
                prefix_name + folder_name + "/",
                prefix_id + folder_id + "/",
            )

            folders_list += subfolders

        return folders_list

if __name__ == "__main__":
    outlook = OutlookApp.from_account("mail@gmail.com")
    print([folder.Name for folder in outlook.instance.Folders])
    print(outlook.get_emails())