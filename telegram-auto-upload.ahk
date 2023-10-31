F3::
{

    skipCopyEnter := InputBox("skipCopyEnter", "is skip copy name and skip enter", "", 0).value
    skipCopyName := InputBox("skipCopyName", "is skip copy name", "", 0).value
    skipCopyFullName := InputBox("skipCopyFullName", "is skip copy full name", "", 1).value
    loopNum := InputBox("loopNum", "loop number", "", 0).value

    If (loopNum = 0)
    {
        Return
    }

    Sleep 3000

    Loop loopNum
    {
        Send "{Ctrl down}"
        Send "{c}"
        Send "{Ctrl up}"
        Sleep 200

        Send "{ALT down}"
        Send "{TAB}"
        Send "{ALT up}"
        Sleep 200

        Send "{Ctrl down}"
        Send "{v}"
        Send "{Ctrl up}"
        Sleep 200


        If (skipCopyEnter = 0)
        {
            If (skipCopyName = 0)
            {
                Send "{ALT down}"
                Send "{TAB}"
                Send "{ALT up}"
                Sleep 200

                Send "{F2}"
                Sleep 200


                Send "{Ctrl down}"
                If (skipCopyFullName = 0)
                {
                    Send "{a}"
                    Sleep 200
                }
                Send "{c}"
                Send "{Ctrl up}"
                Sleep 200
            }

            Send "{ALT down}"
            Send "{TAB}"
            Send "{ALT up}"
            Sleep 200

            Send "{Ctrl down}"
            Send "{v}"
            Send "{Ctrl up}"
            Sleep 200

            Send "{Enter}"
            Sleep 200
        }

        Send "{ALT down}"
        Send "{TAB}"
        Send "{ALT up}"
        Sleep 200

        Send "{Down}"
        Sleep 200


    }

}


F8:: ExitApp

F12::Pause
