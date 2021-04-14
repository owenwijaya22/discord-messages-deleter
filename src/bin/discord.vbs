Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\owenw\vscode\projects\discord\discord.bat" & Chr(34), 0
Set WinScriptHost = Nothing