Set WshShell = CreateObject("WScript.Shell")

' Get the folder path of the running script
strScriptPath = WScript.ScriptFullName
Set fso = CreateObject("Scripting.FileSystemObject")
strFolderPath = fso.GetParentFolderName(strScriptPath)

' Combine folder path and batch file name
strBatchPath = """" & strFolderPath & "\file_manager.bat" & """"

' Run the batch file hidden and asynchronously
WshShell.Run strBatchPath, 0
, False

Set WshShell = Nothing
Set fso = Nothing
