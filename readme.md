# TigerHunter
TigerHunter is a grayware that can change the Windows10 theme(including changing the background of desktop and some of the system notice sounds)
## How to run
- Just simply execute the TigerHunter.exe file and allow the admin authority requested
- After running the .exe, you'll see there's three new file(qq.theme, qq.png, qq.wav) been created under your C:\\, qq.theme is the new theme apply to Windows10 that use qq.png as background and qq.wav as system notice sound
## How to custom the background and sound you want
- Using *read-png.py* & *read-wav.py* to write your data as array in txt file(*bg.txt*, *sound.txt*), notice that the sound file and background file should be named *sound.wav* and *bg.png* respectively.
- Copy them into *change-theme.py*(paste *sound.txt* to sound, *bg.txt* to bg
- Run the command bellow to generate the .exe from *change-theme.py*
```sh
pyinstaller -w -F  change-theme.py --icon=TigerHunter.ico --uac-admin
```