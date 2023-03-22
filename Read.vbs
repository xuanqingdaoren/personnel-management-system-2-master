
Dim msg, sapi

msg=InputBox("Íõ†´ìÊ","Talk it")

Set sapi=CreateObject("sapi.spvoice")

sapi.Speak msg