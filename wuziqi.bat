

@echo off&setlocal enabledelayedexpansion
set li0=������������������������������������������
set li1=�����ЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩЩ���1
for /l %%a in (2,1,18) do (set li%%a=����������������������ȩ�%%a)
set li19=�����ةةةةةةةةةةةةةةةةة���19
set li20=������������������������������������������
set li21=   A B C D E F G H I J K L M N O P Q R S
for %%a in (%li21%) do (set/a .+=1,%%a=.&set z!.!=%%a)
set z0= &set z20= &set "z21= "

set li5=!li5!   �� �� �� �� �� �� ս
set li7=!li7!        �� �� ��
set li9=!li9!   �� �� ˮ ƽ �� ��
set li12=!li12!  �� netbenton ��д���
set li14=!li14!  ������Ʋ����� batman
title   ������������


set str=###################
set .=0
for /l %%a in (1,1,19) do (
        set he%%a=!str!&set sh%%a=!str!
        for /l %%b in (1,1,19) do set [%%a.%%b=0
)

set .=33
for /l %%a in (5,1,19) do (
        set pi%%a=!str:~,%%a!&set ni%%a=!str:~,%%a!
        set pi!.!=!str:~,%%a!&set ni!.!=!str:~,%%a!
        set/a .-=1
)


set ��=��&set a��=����
set ��=��&set a��=���

::���õ���IQ
set idea=@@@@#1 #@@@@5 @#@@@4 @@@#@2 @@#@@3 $#$$$4 $$#$$3 $$$#$2 $$$$#1 #$$$$5 #$$#$#3 #$#$$#4 #@@@##2 ##@@@#5 #@@#@#3 #@#@@#4 #@@@#1
set idea=!idea! ##@@@4 @@@##2 ##$$$#5 #$$$##2 #$$$#1 ##@@#4 #@@##2 ##$$#4 #$$##2 #$#$#3 @@###3 ###@@3
set idea=!idea! ##@##2 ###@#3 #@###3 @####4 ####@2 ##############7 ###########6 ########4 #####3 ####2
set ttr=!idea:@=��!&set ttr=!ttr:$=��!
for %%a in (!ttr!) do (set var=%%a&set !var:~,-1!=!var:~-1!&set idea=!idea! !var:~,-1!)
set ttr=
::���õ���IQ

:restart
for /l %%a in (0,1,21) do (echo    !z%%a!!li%%a!)
setlocal enabledelayedexpansion
set li21=!li21!      reboot���¿�ʼ,exit�˳���
set /p var=ѡ��˭����[ W,���  D,����  Q,�˳� ]:
if /i "!var!" equ "Q" goto :eof
if /i "!var!" equ "W" (set zhi=��) else (set zhi=��)
echo.


:loop
if %zhi% equ �� goto :men
set .=&set put1=
for %%a in (!idea!) do (
        for %%b in (he sh) do (
                for /l %%c in (1,1,19) do (
                        if "!%%b%%c:%%a=!" neq "!%%b%%c!" set/a .+=1&set put!.!=%%b %%c
        )        )
        for %%b in (pi ni) do (
                for /l %%c in (5,1,33) do (
                        if "!%%b%%c:%%a=!" neq "!%%b%%c!" set/a .+=1&set put!.!=%%b %%c
        )        )
if defined put1 set put=%%a&goto :get
)

echo. �Ѿ�������
pause
goto :restart

:men
for /l %%a in (0,1,21) do (echo    !z%%a!!li%%a!)
set /p user=[��ǰ���к�]:
echo.
if "!user!" equ "reboot" endlocal&goto :restart
if "!user!" equ "exit" exit
set/a pos=!user:~0,1!,poh=!user:~1,2!,var=pos-1 2>nul
if not defined [!poh!.!pos! echo ����㲻����&goto :men
if "!he%poh%:~%var%,1!" neq "#" echo �õ��Ѿ�����&goto men
goto :getok

:get
set /a .=!random!%%.+1
set put=!put%.%! !put!
::���ȡ��ѵ��߷�

for /f "tokens=1-3" %%a in ("%put%") do (
        set var=!%%a%%b:*%%c=!srqponmlkjihgfedcba0
        set/a var=!var:~19,1!+%%c
        if "%%a" equ "he" (set/a poh=%%b,pos=20-var)
        if "%%a" equ "sh" (set/a poh=20-var,pos=%%b)
        if %%b lss 19 (set/a var=%%b-var+1) else (set/a var=38-%%b-var+1)
        if "%%a" equ "pi" (if %%b lss 19 (set/a pos=var,poh=%%b-var+1) else (set/a poh=20-var,pos=%%b-19+var))
        if "%%a" equ "ni" (if %%b lss 19 (set/a pos=var,poh=19-%%b+var) else (set/a poh=var,pos=%%b-19+var))
)
echo  ����������ڣ�!z%pos%!!z%poh%!(%poh%)

:getok
set zhi=!%zhi%!&set win=!zhi!!zhi!!zhi!!zhi!!zhi!
set/a piph=poh+pos-1,lips=pos+1,niph=19+pos-poh

if !piph! lss 19 (set/a pips=pos) else (set/a pips=20-poh)
if !niph! lss 19 (set/a nips=pos) else (set/a nips=poh)


for %%a in ("li!poh! !lips!" "he!poh! !pos!" "sh!pos! !poh!" "pi!piph! !pips!" "ni!niph! !nips!") do (
        for /f "tokens=1,2" %%b in (%%a) do (
                if defined %%b (
                        set/a .=%%c-1
                        for %%d in (!.!) do (set %%b=!%%b:~0,%%d!%zhi%!%%b:~%%c!)
                if "!%%b:%win%=!" neq "!%%b!" set win=y
                )
        )
)
set/a asc%zhi%+=1
if !win! neq y goto :loop
for /l %%a in (0,1,21) do (echo    !z%%a!!li%%a!)
set/p=   !a%zhi%! %zhi%�� ��!asc%zhi%!��  ʤ��     <nul
pause
endlocal&goto :restart
