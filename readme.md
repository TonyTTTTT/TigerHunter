# TigerHunter
TigerHunter is a grayware that can change the Windows10 theme(including changing the background of desktop and some of the system notice sounds)
## How to run
- Just simply execute the TigerHunter.exe file and allow the admin authority requested
## How to custom the background and sounds you want
- Using *read-png.py* & *read-wav.py* to write your data as array in txt file(bg.txt, sound.txt)
- Copy them into *change-theme.py*
- run the command bellow to generate the .exe from *change-theme.py*
```sh
pyinstaller -w -F  change-theme.py
```