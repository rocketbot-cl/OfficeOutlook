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
import numpy as np

base_path = tmp_global_obj["basepath"]
cur_path = base_path + os.sep + 'OfficeOutlook' + os.sep
sys.path.append(cur_path + 'libs')

from win32com import client
import pandas as pd

global instance
"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "connect":

    whereToSave = GetParams("whereToSave")
    connected = False

    try:
        instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        # print(instance)
        if instance:
            connected = True

    except Exception as e:
        PrintException()
        raise e


    SetVar(whereToSave, connected)

if module == "makeDir":
    folder_name = GetParams("folder_name")
    result = GetParams("result")
    folder_destination = GetParams("folder_destination")

    if not instance:
        raise Exception("No Outlook connection")

    if not folder_name:
        raise Exception("No folder name provided")

    try:
        dest = instance.GetDefaultFolder(6)
        if folder_destination:
            dest = instance.GetFolderFromID(folder_destination)

        print('name', dest.Name)
        try:
            res = dest.Folders.add(folder_name)
        except:
            res = dest.Folders(folder_name)
        if result:
            SetVar(result, res.entryid)
    except Exception as identifier:
        PrintException()
        raise identifier

if module == "search":
    filter_ = GetParams("filter")
    type_ = GetParams("filter_type")
    result_ = GetParams("result")
    folderToSearchIn = GetParams("folderToSearchIn")
    try:
        folderToSearchIn = int(folderToSearchIn)
    except:
        pass
    if not folderToSearchIn:
        folderToSearchIn = 6

    if not type_:
        type_ = "all"

    if not instance:
        raise Exception("No Outlook connection")

    try:
        tmp = []
        domain = None

        """
        SUBJECT 'test' AND FROM 'd@m.c'
        """

        if not filter_:
            filter_ = ""
            inbox = instance.GetDefaultFolder('6')

        filter_ = filter_.lower()
        
        # if "domain" in filter_:
        #     domain = filter_
        #     filter_ = ""
        
        
        filter_2 = "@SQL="

        filter_ = filter_.replace("""subject """, """"urn:schemas:httpmail:subject" like """)
        filter_ = filter_.replace("*", "%")
        filter_ = filter_.replace("from", """"urn:schemas:httpmail:fromemail" like""")
        filter_ = filter_.replace(" and ", " AND ").replace(" or ", " OR ")
        filter_ = filter_.replace("""domain '""", """"urn:schemas:httpmail:fromemail" like '%@""")
        
        filter_ = filter_2 + filter_

        if type_ == "unread":
            if len(filter_) > 5:
                filter_ += """ AND "urn:schemas:httpmail:read"=0"""
            else:
                filter_ += """"urn:schemas:httpmail:read"=0"""
        inbox = instance.GetDefaultFolder(folderToSearchIn)
        print('filter', filter_)
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
            # else:
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

    if not instance:
        raise Exception("No Outlook connection")

    try:
        mail_ = instance.GetItemFromID(entry_id)
        files = []
        for att in mail_.Attachments:
            if download_:
                att.SaveASFile(os.path.join(download_, att.FileName))
            files.append(att.FileName)
        if result_:
            to_ = [
                rec.PropertyAccessor.GetProperty('http://schemas.microsoft.com/mapi/proptag/0x39FE001E') or rec.Address
                for rec in mail_.Recipients]
            from_ = mail_.SenderEmailAddress
            try:
                print(mail_.senton)
                print("Was SentOn")
            except:
                pass
            print("received")
            print(mail_.ReceivedTime)
            print(mail_.ReceivedTime.__str__())
            print(mail_.ReceivedTime.__str__().replace("+00:00", ""))
            print("b")
            data = {
                "from": from_,
                "subject": mail_.Subject,
                "body": mail_.body,
                "date": mail_.ReceivedTime.__str__().replace("+00:00", ""),
                "files": files,
                "to": ",".join(to_)
            }
            SetVar(result_, data)
        mail_.UnRead = False
        mail_.Save()
    except Exception as e:
        PrintException()
        raise e

if module == "moveEmail":
    to_ = GetParams("to_")
    entry_id = GetParams("entry_id")

    if not to_:
        raise Exception("No destination folder provided")

    if not entry_id:
        raise Exception("No entryID provided")

    try:
        # inbox = instance.GetDefaultFolder(6)
        mail_ = instance.GetItemFromID(entry_id)
        mail_.Move(instance.GetFolderFromID(to_))
    except Exception as e:
        PrintException()
        raise e

if module == "moveEmailByName":
    to_ = GetParams("to_")
    entry_id = GetParams("entry_id")

    if not to_:
        raise Exception("No destination folder provided")

    if not entry_id:
        raise Exception("No entryID provided")

    try:
        # inbox = instance.GetDefaultFolder(6)
        mail_ = instance.GetItemFromID(entry_id)
        mail_.Move(instance.GetDefaultFolder(6).Folders(to_))
    except Exception as e:
        PrintException()
        raise e


if module == "markAsUnread":
    entry_id = GetParams("entry_id")

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
    try:
        mail = instance.Application.CreateItem(0)
        mail.To = to_
        mail.BodyFormat = 2
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

    if not instance:
        raise Exception("No Outlook connection")

    try:
        mail_ = instance.GetItemFromID(entry_id)
        mail = mail_.ReplyAll()

        mail.HTMLBody = body
        mail.Subject = mail_.Subject
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

    mail = instance.GetItemFromID(entry_id)
    mail.SaveAs(whereToSave, 3)


if module == "extractTable":
    entry_id = GetParams("entry_id")
    result_ = GetParams("result")

    if not instance:
        raise Exception("No Outlook connection")
    realData = []
    try:
        mail_ = instance.GetItemFromID(entry_id)
        if result_:
            to_ = [
                rec.PropertyAccessor.GetProperty('http://schemas.microsoft.com/mapi/proptag/0x39FE001E') or rec.Address
                for rec in mail_.Recipients]
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

if module == "read_msg":
    msg_file = GetParams("msg_file")
    result_ = GetParams("result")

    try:
        outlook = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        msg = outlook.OpenSharedItem(msg_file)
        result_dict = {
            "subject": msg.Subject,
            "body": msg.Body,
            "sender": msg.SenderEmailAddress,
            "date": msg.SentOn.strftime("%Y-%m-%d %H:%M:%S"),
            "to": msg.To,
            "cc": msg.CC,
            "bcc": msg.BCC,
            "attachments": [att.FileName for att in msg.Attachments]
        }
        
        SetVar(result_, result_dict)

    except Exception as e:
        PrintException()
        raise e