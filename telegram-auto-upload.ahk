; This script was created using Pulover's Macro Creator
; www.macrocreator.com

#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1
SetWinDelay 0
SetKeyDelay -1
SetMouseDelay -1
SetBatchLines -1


F3::
Macro1:
InputBox, skipCopyFullName, skipCopyFullName, , , , , , , , , 1
InputBox, skipCopyName, skipCopyName, , , , , , , , , 0
InputBox, loopNum, loopNum, , , , , , , , , 0
If (%loopNum%=0)
{
    Return
}
Sleep, 5000
Loop, %loopNum%
{
    If (1=1)
    {
        Send, {LControl Down}
        Sleep, 200
        Send, {c}
        Sleep, 200
        Send, {LControl Up}
    }
    Sleep, 1000
    If (1=1)
    {
        Send, {LAlt Down}
        Sleep, 200
        Send, {Tab}
        Sleep, 200
        Send, {LAlt Up}
    }
    Sleep, 2000
    If (1=1)
    {
        Send, {LControl Down}
        Sleep, 200
        Send, {v}
        Sleep, 200
        Send, {LControl Up}
    }
    Sleep, 1000
    If (0=%skipCopyName%)
    {
        If (1=1)
        {
            Send, {LAlt Down}
            Sleep, 200
            Send, {Tab}
            Sleep, 200
            Send, {LAlt Up}
        }
        Sleep, 2000
        If (1=1)
        {
            Send, {F2}
        }
        Sleep, 1000
        If (1=1)
        {
            Send, {LControl Down}
            Sleep, 200
            If (0=%skipCopyFullName%)
            {
                Send, {a}
            }
            Sleep, 1000
            Send, {c}
            Sleep, 200
            Send, {LControl Up}
        }
        Sleep, 1000
        If (1=1)
        {
            Send, {LAlt Down}
            Sleep, 200
            Send, {Tab}
            Sleep, 200
            Send, {LAlt Up}
        }
        Sleep, 2000
        If (1=1)
        {
            Send, {LControl Down}
            Sleep, 200
            Send, {v}
            Sleep, 200
            Send, {LControl Up}
        }
        Sleep, 1000
    }
    If (1=1)
    {
        Send, {Enter}
    }
    Sleep, 1000
    If (1=1)
    {
        Send, {LAlt Down}
        Sleep, 200
        Send, {Tab}
        Sleep, 200
        Send, {LAlt Up}
    }
    Sleep, 2000
    If (1=1)
    {
        Send, {Down}
    }
    Sleep, 1000
}
Return


F8::ExitApp

F12::Pause
