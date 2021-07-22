# ANSSI-IOC-IP-to-Fortigate-Importer
This tool extracts IPs from the IOCs published by the ANSSI for insertion into Fortigate firewalls

# How to
you'll need python3 and the pandas library, and you'll want to edit 
- the input file location
- the output file location
- the interface name that will be assocaited to the IP addresses in your fortigate ("show system interface" to help you, but this command doesn't show SDWAN interfaces, the script defaults to "any") 

'''
python -m pip install -r requirements.txt
python3 extractor.py
'''
