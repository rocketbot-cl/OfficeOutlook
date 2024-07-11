



# OfficeOutlook
  
Module to connect to Outlook Desktop application.  

*Read this in other languages: [English](Manual_OfficeOutlook.md), [Português](Manual_OfficeOutlook.pr.md), [Español](Manual_OfficeOutlook.es.md)*
  
![banner](imgs/Banner_OfficeOutlook.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
In order to use this module, you have to add an account to Outlook and then you can connect successfully.


## Description of the commands

### Connect to Outlook
  
Connect to an Outlook application instance
|Parameters|Description|example|
| --- | --- | --- |
|Email|Optional. Email of the Outlook account. Must be an email that is linked in the Outlook Application.|rocketbot@outlook.com|
|Variable to save connection's result|Save the result of conection.|result|
|Outlook Session|Assign a session to the Outlook connection.|session|

### Create folder
  
Create a folder on Outlook
|Parameters|Description|example|
| --- | --- | --- |
|Folder name|Name of the folder you want to create.|New folder|
|Destination dir|Folder where you want to create the new folder inside (optional).|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEE4E12200|
|Set to variable|Save the result of the creation of the folder.|Variable|

### List Folders
  
List all Folders
|Parameters|Description|example|
| --- | --- | --- |
|Outlook Session|Assign a session to the Outlook connection.|session|
|Asign result to var||Variable|

### Search Email by Filter
  
Search by filter provided
|Parameters|Description|example|
| --- | --- | --- |
|Filter|Filter you want to use.|(domain 'rocketbot.com' or domain 'gmail.com') and subject 'Notification'|
|Search in|Filter for emails read and unread.|All|
|Folder|Folder you want to search in.|Inbox|
|Subfolder|Path to the subfolder you want to search in. To get the path to the subfolder, you must use the 'List folders' module.|rocketbot@outlook.com/RocketFolder|
|Outlook Session|Assign a session to the Outlook connection.|session|
|Set to variable|Save the result of search.|Variable|

### Read email by EntryID
  
Read email data by EntryID provided
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of the email that you want to obtain.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Set to variable|Save the read email.|Variable|
|Outlook Session|Assign a session to the Outlook connection.|session|
|Include HTML|Include the email HTML in the result.|True|
|Download attachments|Path to folder where to save attachments.|C:\User\|

### Move email to folder
  
Move email data by EntryID provided
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of the email that you want to move.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Destination folder|Folder where you want to move in.|0014182A9615CE201001B40B98EB45D6B4A70D3F4F050000D5955FDE0000|

### Move email to folder by Name
  
Move email data by Name provided. (Only folder into Inbox)
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of the email that you want to move.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Destination folder|Folder where you want to move in.|my_folder|

### Mark email as unread
  
Mark email as unread by EntryID provided
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of email that you want to mark as unread.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|

### Send Email
  
Send email, before you must configurate the server
|Parameters|Description|example|
| --- | --- | --- |
|To|Emails of recipients.|to@mail.com, to2@mail.com|
|Cc|Emails of recipients.|cc@mail.com, cc2@mail.com|
|Subject|Subject to send it with.|New mail|
|Body|You can use html to style your email. Example <b>Bold text</b>. For local images, use <img src='png image path'>|This is a test message|
|Attached File|Attached file that you want to send.|C:\User\Desktop\test.txt|
|Folder (Multiple files)|Folder that contains attached files which you want to send.|C:\User\Desktop\Files|
|Read Receipt||True|

### Reply Email
  
Reply mail from Entry ID
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of the email that you want to reply.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Body|Body of the email.|This is a test|
|Attached File|Attached file that you want to send with.|C:\User\Desktop\test.txt|
|Folder (Multiple files)|Folder that contains attached files which you want to send with.|C:\User\Desktop\Files|

### Forward Email
  
Forward mail from Entry ID
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of the email that you want to forward.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|To|Emails of recipients.|to@mail.com, to2@mail.com|

### Save Email
  
Saves a mail from Entry ID
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of email that you want to save.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Path to save file|Path in which to save the file.|C:/Users/Documents/mail.msg|

### Extract table from email by EntryID
  
Extract the content of a table by email EntryID provided
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of email that you want to extract the table.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Set to variable|Save the result of the read of the table.|Variable|

### Download attachments by EntryID
  
Download attachments by EntryID in a folder
|Parameters|Description|example|
| --- | --- | --- |
|EntryID|ID of email that you want to obtain.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Download attachments|Path to folder where to save attachments.|C:\User\|

### Read .msg file
  
Read .msg file and store the information in a variable
|Parameters|Description|example|
| --- | --- | --- |
|Path to .msg file|Path of the .msg file that you want to read.|C:/Users/User/Desktop/file.msg|
|Asignar resultado a variable|Name of the variable where the information of the .msg file will be stored.|Variable|
