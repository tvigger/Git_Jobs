import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('server', type=str)
parser.add_argument('port', type=str)
parser.add_argument('names', nargs='*', type=str)
parser.add_argument('--unmult', default=7, type=int)
parser.add_argument('--mult', default=0, type=int)

args = parser.parse_args()
address = 'http://' + args.server + ':' + args.port
data = json.loads(requests.get(address).text)
for par in args.names:
    if par in data:
        for i in range(len(data[par])):
            if args.unmult:
                if data[par][i] % args.unmult != 0:
                    data[par][i] = data[par][i] // args.unmult * args.unmult
                elif args.mult:
                    if data[par][i] % args.mult == 0:
                        c = 0
                        for cif in str(data[par][i]):
                            c += int(cif)
                        data[par][i] = c
rez = []
for key in data:
    nv = dict()
    nv['bakery'] = key
    nv['summary'] = sum(data[key])
    c = 0
    for el in data[key]:
        if el % 2 == nv['summary'] % 2:
            c += 1
    nv['number'] = c
    rez.append(nv)
print(list(sorted(rez, key=lambda x: x['bakery'])))
