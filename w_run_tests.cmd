REM This was translated by chatGPT
REM  so I havent really tested it -_-
@echo off
setlocal

for %%F in (tests\*) do (
    echo %%F
    python main.py < "%%F"
    if errorlevel 1 (
        echo Something wrong
        exit /b 33
    )
)

echo Ended successfully
endlocal
