# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import math
import re
import numpy as np
from time import sleep

base_path = tmp_global_obj["basepath"]
cur_path = base_path + os.sep + "OfficeOutlook" + os.sep
sys.path.append(cur_path + "libs")

from win32com import client
import pandas as pd
import tempfile

global mod_office_outlook_sessions
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_office_outlook_sessions:
        mod_office_outlook_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_office_outlook_sessions = {SESSION_DEFAULT: {}}

session = GetParams("session")

if not session:
    session = SESSION_DEFAULT

if session not in mod_office_outlook_sessions:
    mod_office_outlook_sessions[session] = {}

instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
isOpened = False
if mod_office_outlook_sessions.get(session, {}).get("instance"):
    instance = mod_office_outlook_sessions[session]["instance"]
    isOpened = mod_office_outlook_sessions[session].get("isOpened", False)

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "connect":

    whereToSave = GetParams("whereToSave")
    email = GetParams("account")
    show_app = GetParams("showApp")
    show_app = str(show_app) == "true" or str(show_app) == "True"
    connected = False
    

    try:
        
        instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")        


        if email and email not in [x.DisplayName for x in instance.Accounts]:
            SetVar(whereToSave, connected)
            raise Exception("Account not found")
            
        
        if show_app and not isOpened:
            instance.GetDefaultFolder(6).Display()
            mod_office_outlook_sessions[session]["isOpened"] = True

        for account in instance.Accounts:
            if account.DisplayName == email:
                instance = account.DeliveryStore
                
        if instance:
            # mod_office_outlook_sessions[session]["instance"] = instance
            mod_office_outlook_sessions[session] = {"instance": instance, "account": email}
            print(mod_office_outlook_sessions[session])
            connected = True

    except Exception as e:
        PrintException()
        raise e
        

    SetVar(whereToSave, connected)


if module == "makeDir":
    folder_name = GetParams("folder_name")
    result = GetParams("result")
    folder_destination = GetParams("folder_destination")
    #instance = mod_office_outlook_sessions[session]["instance"]
    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI") 
    if not instance:
        raise Exception("No Outlook connection")

    if not folder_name:
        raise Exception("No folder name provided")

    try:
        dest = instance.GetDefaultFolder(6)
        if folder_destination:
            dest = instance.GetFolderFromID(folder_destination)

        print("name", dest.Name)
        try:
            res = dest.Folders.add(folder_name)
        except:
            res = dest.Folders(folder_name)
        if result:
            SetVar(result, res.entryid)
    except Exception as identifier:
        PrintException()
        raise identifier


def getCurrentFolders(instance):
    try:
        return instance.Parent.Folders
    except:
        return instance.Folders


if module == "list_folders":
    result = GetParams("var")
    instance = mod_office_outlook_sessions[session]["instance"]
    if not instance:
        raise Exception("No Outlook connection")

    try:
        try:
            AccountId = instance.StoreID
        except:
            AccountId = None

        folders = getCurrentFolders(instance)
        # root_folder = instance.Folders.Item(1)
        # stack = [root_folder]

        def getFolders(folders, AccountId, prefix_name="", prefix_id=""):
            global getFolders
            folders_list = []
            for folder in folders:

                if AccountId is not None and folder.Store.StoreID != AccountId:
                    continue

                folder_info = {
                    "Name": prefix_name + folder.Name,
                    "EntryID": prefix_id + folder.EntryID,
                }
                folders_list.append(folder_info)
                subfolders = getFolders(
                    folder.Folders,
                    AccountId,
                    prefix_name + folder.Name + "/",
                    prefix_id + folder.EntryID + "/",
                )

                folders_list += subfolders

            return folders_list

        folders_list = getFolders(folders, AccountId)

        SetVar(result, folders_list)
    except Exception as identifier:
        PrintException()
        raise identifier


if module == "search":
    filter_ = GetParams("filter")
    type_ = GetParams("filter_type")
    result_ = GetParams("result")
    folderToSearchIn = GetParams("folderToSearchIn")
    subfolder = GetParams("subfolder")
    
    instance = mod_office_outlook_sessions[session]["instance"]

    if not instance:
        raise Exception("No Outlook connection")
    try:
        folderToSearchIn = int(folderToSearchIn)
    except:
        pass

    if not folderToSearchIn:
        folderToSearchIn = 6

    if not type_:
        type_ = "all"

    
    try:
        tmp = []
        domain = None

        """
        SUBJECT 'test' AND FROM 'd@m.c'
        """

        if not filter_:
            filter_ = ""
            inbox = instance.GetDefaultFolder("6")

        filter_ = filter_.lower()

        # if "domain" in filter_:
        #     domain = filter_
        #     filter_ = ""

        filter_2 = "@SQL="

        filter_ = filter_.replace(
            """subject """, """"urn:schemas:httpmail:subject" like """
        )
        filter_ = filter_.replace("*", "%")
        filter_ = filter_.replace("from", """"urn:schemas:httpmail:fromemail" like""")
        filter_ = filter_.replace(" and ", " AND ").replace(" or ", " OR ")
        filter_ = filter_.replace(
            """domain '""", """"urn:schemas:httpmail:fromemail" like '%@"""
        )

        filter_ = filter_2 + filter_

        if type_ == "unread":
            if len(filter_) > 5:
                filter_ += """ AND "urn:schemas:httpmail:read"=0"""
            else:
                filter_ += """"urn:schemas:httpmail:read"=0"""
        if type_ == "read":
            if len(filter_) > 5:
                filter_ += """ AND "urn:schemas:httpmail:read"=1"""
            else:
                filter_ += """"urn:schemas:httpmail:read"=1"""
        if type_ == "all":
            if len(filter_) > 5:
                filter_ += """ AND ("urn:schemas:httpmail:read"=1 OR "urn:schemas:httpmail:read"=0)"""
            else:
                filter_ += """("urn:schemas:httpmail:read"=1 OR "urn:schemas:httpmail:read"=0)"""
   
        print("filter", filter_)
        if subfolder:
            folders = getCurrentFolders(instance)

            for folder in subfolder.split("/"):
                mod_office_outlook_sessions["__private_folder"] = folder
                inbox = [
                    x
                    for x in folders
                    if x.Name == mod_office_outlook_sessions["__private_folder"]
                ][0]
                folders = inbox.Folders
            # inbox = [x for x in instance.GetDefaultFolder(folderToSearchIn).Parent.Folders if x.EntryId == subfolder][0]
        else:
            inbox = instance.GetDefaultFolder(folderToSearchIn)
        table_ = inbox.GetTable(filter_)
        while not table_.EndOfTable:
            r = table_.GetNextRow()
            # if domain:
            #     filter_ = domain.split(' "')[-1][:-1]
            #     mail_ = instance.GetItemFromID(r("EntryID"))
            #     try:
            #         if mail_.SenderEmailType == "EX":
            #             address = mail_.Sender.GetExchangeUser().PrimarySmtpAddress
            #         else:
            #             address = mail_.SenderEmailAddress

            #         if filter_ in address:
            #             tmp.append(r("EntryID"))
            #     except:
            #         continue
            # else:Le da 
            #     tmp.append(r("EntryID"))
            tmp.append(r("EntryID"))
        if result_:
            SetVar(result_, tmp)
    except Exception as identifier:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise identifier

if module == "readEmail":
    entry_id = GetParams("entry_id")
    result_ = GetParams("result")
    download_ = GetParams("download")
    subfolder = GetParams("subfolder")
    includeHTML = GetParams("includeHTML")

    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")
    
    try:
        mail_ = instance.GetItemFromID(entry_id)
        files = []
        
        for att in mail_.Attachments:
            print("propiedades")
            print(att.DisplayName)  
            print(att.Position) 
            print(att.Index)    
            if download_:
                base_name, ext = os.path.splitext(att.FileName)
                unique_name = att.FileName
                counter = 1
                while os.path.exists(os.path.join(download_, unique_name)):
                    unique_name = f"{base_name} ({counter}){ext}"
                    counter += 1
                att.SaveASFile(os.path.join(download_, unique_name))
                
                files.append(unique_name)
            # files.append(att.FileName)
        if result_:
            to_ = [
                rec.PropertyAccessor.GetProperty(
                    "http://schemas.microsoft.com/mapi/proptag/0x39FE001E"
                )
                or rec.Address
                for rec in mail_.Recipients
            ]
            from_ = mail_.SenderEmailAddress
            try:
                print(mail_.senton)
                print("Was SentOn")
            except:
                pass
            data = {
                "from": from_,
                "subject": mail_.Subject,
                "body": mail_.body,
                "date": mail_.ReceivedTime.__str__().replace("+00:00", ""),
                "files": files,
                "to": ",".join(to_),
            }
            if includeHTML == "true" or includeHTML == "True":
                data["html"] = mail_.HTMLBody

            SetVar(result_, data)
        mail_.UnRead = False
        mail_.Save()
    except Exception as e:
        PrintException()
        raise e

if module == "moveEmail":
    to_ = GetParams("to_")
    entry_id = GetParams("entry_id")

    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")


    if not to_:
        raise Exception("No destination folder provided")

    if not entry_id:
        raise Exception("No entryID provided")

    try:
       # inbox = instance.GetDefaultFolder(6)
        mail_ = instance.GetItemFromID(entry_id)
        #print(mail_)
        #mail_.Move(inbox.Folders.GetFolderFromID(to_))
        mail_.Move(instance.GetFolderFromID(to_))
    except Exception as e:
        PrintException()
        raise e

if module == "moveEmailByName":
    to_ = GetParams("to_")
    entry_id = GetParams("entry_id")

    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not to_:
        raise Exception("No destination folder provided")

    if not entry_id:
        raise Exception("No entryID provided")

    try:
        mail_ = instance.GetItemFromID(entry_id)
        mail_.Move(instance.Folders.item(1).Folders[to_])
    except Exception as e:
        PrintException()
        raise e


if module == "markAsUnread":
    entry_id = GetParams("entry_id")
    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    try:
        mail_ = instance.GetItemFromID(entry_id)
        mail_.unread = True
        mail_.Save()
    except Exception as e:
        PrintException()
        raise e

if module == "sendEmail":
    to_ = GetParams("to")
    cc = GetParams("cc")
    subject = GetParams("subject")
    body = GetParams("body")
    att_files = GetParams("attached_file")
    att_folder = GetParams("attached_folder")
    read_receipt = GetParams("read_receipt")
    instance = mod_office_outlook_sessions[session]["instance"]
    try:
        mail = instance.Application.CreateItem(0)
        mail.To = to_
        mail.BodyFormat = 2

        # get image path in body
        regex = "<\s?img\s.*src\s?=\s?['\"](.*)['\"]"
        img_path = re.findall(regex, body)
        if img_path:
            for img in img_path:
                if img.startswith(("cid:", "http")):
                    continue
                filename = img.replace(os.sep, "/").split("/")[-1]
                mail.Attachments.Add(img, 1, 0)
                att = mail.Attachments[mail.Attachments.Count - 1]
                att.PropertyAccessor.SetProperty(
                    "http://schemas.microsoft.com/mapi/proptag/0x3712001F", filename
                )
                body = body.replace(img, "cid:{}".format(filename))

        mail.HTMLBody = body
        if cc:
            mail.CC = cc
        mail.Subject = subject
        if att_files:
            mail.Attachments.Add(att_files)
        if att_folder:
            for f in os.listdir(att_folder):
                f = os.path.join(att_folder, f)
                mail.Attachments.Add(f)
        if read_receipt:
            mail.ReadReceiptRequested = True
        mail.Send()
    except Exception as e:
        PrintException()
        raise e

if module == "replyEmail":
    entry_id = GetParams("entry_id")
    to_ = GetParams("to")
    subject = GetParams("subject")
    body = GetParams("body")
    att_files = GetParams("attached_file")
    att_folder = GetParams("attached_folder")
    includeatt = eval(GetParams("includeatt")) if GetParams("includeatt") else False

    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")

    try:
        mail_ = instance.GetItemFromID(entry_id)
        mail = mail_.ReplyAll()

        # get image path in body
        regex = "<\s?img\s.*src\s?=\s?['\"](.*)['\"]"
        img_path = re.findall(regex, body)
        if img_path:
            for img in img_path:
                if img.startswith(("cid:", "http")):
                    continue
                filename = img.replace(os.sep, "/").split("/")[-1].replace(" ", "_").replace("(", "").replace(")", "")
                mail.Attachments.Add(img, 1, 0)
                att = mail.Attachments[mail.Attachments.Count - 1]
                att.PropertyAccessor.SetProperty(
                    "http://schemas.microsoft.com/mapi/proptag/0x3712001F", filename
                )
                body = body.replace(img, "cid:{}".format(filename))

        mail.HTMLBody = body + mail.HTMLBody

        mail.Subject = mail.Subject

        if includeatt is True:
            for attachment in mail_.Attachments:
                attachment.SaveAsFile(os.path.join(tempfile.gettempdir(), attachment.FileName))
                mail.Attachments.Add(os.path.join(tempfile.gettempdir(), attachment.FileName))

        if att_files:
            mail.Attachments.Add(att_files)
        if att_folder:
            for f in os.listdir(att_folder):
                f = os.path.join(att_folder, f)
                mail.Attachments.Add(f)
        mail.Send()

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e


if module == "Forward":
    entry_id = GetParams("entry_id")
    to_ = GetParams("to")
    #instance = mod_office_outlook_sessions[session]["instance"]
    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")
    try:
        mail_ = instance.GetItemFromID(entry_id)
        mail = mail_.Forward()

        mail.To = to_
        mail.Send()

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "SaveAs":
    entry_id = GetParams("entry_id")
    whereToSave = GetParams("whereToSave")
    #instance = mod_office_outlook_sessions[session]["instance"]
    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")
    mail = instance.GetItemFromID(entry_id)
    mail.SaveAs(whereToSave, 3)


if module == "extractTable":
    entry_id = GetParams("entry_id")
    result_ = GetParams("result")
    #instance = mod_office_outlook_sessions[session]["instance"]
    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")
    realData = []
    try:
        mail_ = instance.GetItemFromID(entry_id)
        if result_:
            to_ = [
                rec.PropertyAccessor.GetProperty(
                    "http://schemas.microsoft.com/mapi/proptag/0x39FE001E"
                )
                or rec.Address
                for rec in mail_.Recipients
            ]
            from_ = mail_.SenderEmailAddress
            # data = pd.read_html(mail_.HTMLBody)[0].values.tolist()
            data = pd.read_html(mail_.HTMLBody)

            for each in data:
                realData.append(each.values.tolist())
            for indxi, i in enumerate(realData):

                for indxc, cada in enumerate(i):

                    for indexu, uno in enumerate(cada):
                        if uno.__str__() == "nan":
                            realData[indxi][indxc][indexu] = ""

            SetVar(result_, realData)
    except Exception as e:
        PrintException()
        raise e

if module == "get_attachments":
    entry_id = GetParams("entry_id")
    download_ = GetParams("download")
    #instance = mod_office_outlook_sessions[session]["instance"]
    instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    if not instance:
        raise Exception("No Outlook connection")
    try:
        mail_ = instance.GetItemFromID(entry_id)
        files = []
        for att in mail_.Attachments:
            if download_:
                att.SaveASFile(os.path.join(download_, att.FileName))
            files.append(att.FileName)
        mail_.UnRead = False
        mail_.Save()
    except Exception as e:
        PrintException()
        raise e
