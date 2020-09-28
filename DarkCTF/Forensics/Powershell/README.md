# PowerShell
> Points: 430

## Description
>I want to know what is happening in my Windows Powershell.<br>
[File](https://mega.nz/file/DmwQASKa#7iYMLa9urXYWdIls49MeMx_Qno8O6RCIBqXVqIqY6cM)

## Solution
> We are given a mp3 file. Used `binwalk` to extract embedded files.
```bash
⚡ root@ignite ~/Documents/darkCTF> binwalk -e file.mp3 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
199140        0x309E4         Zip archive data, at least v2.0 to extract, compressed size: 9881019, uncompressed size: 176524482, name: Suspicious.reg
10080203      0x99CFCB        Zip archive data, at least v2.0 to extract, compressed size: 1180, uncompressed size: 13863, name: PowerShell.xml
10081711      0x99D5AF        End of Zip archive, footer length: 22
```
As the challenege name suggests I opened the `PowerShell.xml` and found this
```bash
        CommandLine=</Data></EventData></Event><Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='PowerShell'/><EventID Qualifiers='0'>600</EventID><Level>4</Level><Task>6</Task><Keywords>0x80000000000000</Keywords><TimeCreated SystemTime='2020-09-20T06:30:07.000000000Z'/><EventRecordID>12</EventRecordID><Channel>Windows PowerShell</Channel><Computer>WIN-6CNOVHMFLR0</Computer><Security/></System><EventData><Data>Environment</Data><Data>Started</Data><Data>    ProviderName=Environment
        NewProviderState=Started

        SequenceNumber=3

        HostName=ConsoleHost
        HostVersion=2.0
        HostId=a539e857-7bd0-4885-b64c-5fa903ac0f86
        EngineVersion=
        RunspaceId=
        PipelineId=
        CommandName=
echo "ZGFya0NURntDMG1tNG5kXzBuX3AwdzNyc2gzbGx9" | base64 -d     CommandType=
        ScriptName=
        CommandPath=
```
Running the command gives the flag
```bash
⚡ root@ignite ~/Documents/darkCTF/_file.mp3.extracted> echo "ZGFya0NURntDMG1tNG5kXzBuX3AwdzNyc2gzbGx9" | base64 -d
darkCTF{C0mm4nd_0n_p0w3rsh3ll}
```
## Flag
>darkCTF{C0mm4nd_0n_p0w3rsh3ll}
