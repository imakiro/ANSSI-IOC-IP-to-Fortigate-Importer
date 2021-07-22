import pandas as pd

# Variables
interface_name = "any" #name of the interface in your FortiGate configuration

# This project is only intended to be able to run IF
## signature_component.type is "ip-dst"
# Source of the demo file : https://www.cert.ssi.gouv.fr/ioc/CERTFR-2021-IOC-003/
data = pd.read_csv('Examples/CERTFR-2021-IOC-003-IOC.csv')
df = pd.DataFrame(data, columns= ['event.apts','signature.type','signature_component.value'])
df = df.loc[df['signature.type'] == "ip-dst"]

# Generating the fortigate command files
if not df.empty:
    with open("Examples/generated_fortigate_commands.txt", "w+") as genFile:
        genFile.write("config firewall address\n")
        for index, row in df.iterrows():
            genFile.write("    edit IOC_"+row["event.apts"]+"_"+str(index+1)+"\n")
            genFile.write("        set associated-interface \""+interface_name+"\"\n")
            genFile.write("        set subnet "+row["signature_component.value"]+" 255.255.255.255\n")
            genFile.write("    next\n")
        genFile.write("end\n")
