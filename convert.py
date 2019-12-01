import ipaddress

with open('china_ip_list/china_ip_list.txt') as f:
    networkList = f.readlines()

networkList = [x.strip() for x in networkList]

for networkItem in networkList:
    networkObj = ipaddress.IPv4Network(networkItem)
    minIp = int(networkObj[0])
    maxIp = int(networkObj[-1])
    print(f'[{minIp},{maxIp}],')
