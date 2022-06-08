ECHO "Creating test file"
powershell "Get-ChildItem -Path .\*.py,.\runTest.sh | Compress-Archive -DestinationPath .\script.zip"
ECHO "You should now upload test file script.zip to WeTest Cloud"