$exclude = @("venv", "desafio03.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desafio03.zip" -Force