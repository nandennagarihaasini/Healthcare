@echo off
title Upload Healthcare Project to GitHub
color 0A
cd /d "D:\Healthcare project\healthcare"
echo ===================================================
echo   Pushing Healthcare REST API to GitHub Repository
echo   https://github.com/nandennagarihaasini/Healthcare
echo ===================================================
echo.
"C:\Program Files\Git\cmd\git.exe" push -u origin main
echo.
if %ERRORLEVEL% equ 0 (
    echo ===================================================
    echo   SUCCESS! Your project is now live on GitHub!
    echo ===================================================
) else (
    echo.
    echo If GitHub asked you to sign in, please complete the login in your browser and run this file again.
)
echo.
pause
