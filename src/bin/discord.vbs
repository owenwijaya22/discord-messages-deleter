Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\owenw\vscode\projects\Discord\src\bin\discord.bat" & Chr(34), 0
Set WinScriptHost = Nothing