@echo off
set source="E:\code\python\pythonProject1\Game\*.py"
set destination="E:\code\python\pythonTest"

xcopy %source% %destination% /Y

echo 所有 .py 文件已从 %source% 拷贝到 %destination%
pause