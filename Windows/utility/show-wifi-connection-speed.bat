
start cmd.exe /k "wmic NIC where NetEnabled=true get Name, Speed"
::shows all registered connections ("user/group profiles" in Windows) on the wlan interface