if exist "C:\JailbreakAndroid" rd /s /q "C:\JailbreakAndroid"
mkdir C:\JailbreakAndroid
xcopy *.* C:\JailbreakAndroid
cd C:\JailbreakAndroid
python Jailbreaking.py
