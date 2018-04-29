@echo off 
echo 删除3天前的备分文件和日志

forfiles /p "D:\oraclebackup" /m *.dmp /d -3 /c "cmd /c del @path" 
forfiles /p "D:\oraclebackup" /m *.log /d -3 /c "cmd /c del @path"

echo 正在备份 Oracle 数据库，请稍等…… 
exp system/oracle@orcl file=D:/oraclebackup/mdb%date:~0,4%%date:~5,2%%date:~8,2%.dmp log=D:/oraclebackup/mdb%date:~0,4%%date:~5,2%%date:~8,2%.log full=y buffer=65535 
echo 任务完成!
