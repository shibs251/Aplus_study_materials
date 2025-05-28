import random
#create dictionary with common ports and their protocols
ports = {
    "20": "FTP",
    "21": "FTP",
    "22": "SSH",
    "23": "TELNET",
    "25": "SMTF",
    "53": "DNS",
    "67": "DHCP",
    "68": "DHCP",
    "80": "HTTP",
    "110": "POP3",
    "137": "NETBIOS/NETBT",
    "138": "NETBIOS/NETBT",
    "139": "NETBIOS/NETBT",
    "143": "IMAP",
    "161": "SNMP",
    "162": "SNMP",
    "389": "LDAP",
    "427": "AFP/SLP",
    "443": "HTTPS",
    "445": "SMB/CIFS",
    "548": "AFP",
    "3389": "RDP"
}

#randomize ports
list = list(ports.items())
random.shuffle(list)
# shuffled = dict(list)
list_length = len(list)
while list_length > 0:

    question1 = input("what is run on port " + str(list[1][0]) + "\n")
    # print(list[1])

    # if question1 == ports[0][0]:
    #     print(ports[0][0])
    if str(question1) == str(list[1][1]):
        print("That is Correct")
        del list[1]
        # print(list_length)
    else:
        print("That is incorrect")
    random.shuffle(list)
