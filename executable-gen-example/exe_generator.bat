call "C:\Program Files (x86)\Python37-32\Scripts\pyinstaller" --icon=MFH_FT_Monitor.ico --clean -n MFH_FT_Monitor -w .\main.py  

@echo copy  UI file in dist file
copy .\*.ui dist\MFH_FT_Monitor\

pause
