
Dim msg, sapi

msg=InputBox("������","Talk it")

Set sapi=CreateObject("sapi.spvoice")

sapi.Speak msg