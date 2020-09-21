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

base_path = tmp_global_obj["basepath"]
cur_path = base_path + os.sep + 'OfficeOutlook' + os.sep
sys.path.append(cur_path + 'libs')

from win32com import client

global instance
"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "connect":
    try:
        instance = client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    except Exception as e:
        PrintException()
        raise e

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

    if not type_:
        type_ = "all"

    if not instance:
        raise Exception("No Outlook connection")

    try:
        tmp = []
        if filter_:
            if "subject" in filter_.lower():
                filter_ = filter_.split(' "')[-1][:-1]
                filter_ = """@SQL="urn:schemas:httpmail:subject" like '%{tx}%'""".format(tx=filter_)
            if "from" in filter_.lower():
                filter_ = filter_.split(' "')[-1][:-1]
                filter_ = """[SenderEmailAddress] = '{tx}'""".format(tx=filter_)
        else:
            filter_ = ""
        if type_ == "unread":
            if len(filter_) > 0:
                if "SenderEmailAddress" in filter_:
                    filter_ += """ AND [UnRead] = true"""
                else:
                    filter_ += """ AND "urn:schemas:httpmail:read" = 0"""
            else:
                filter_ = "[UnRead] = true"
        inbox = instance.GetDefaultFolder(6)
        print('filter', filter_)
        table_ = inbox.GetTable(filter_)
        while not table_.EndOfTable:
            r = table_.GetNextRow()
            tmp.append(r("EntryID"))

        if result_:
            SetVar(result_, tmp)
    except Exception as identifier:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
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
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        raise e

