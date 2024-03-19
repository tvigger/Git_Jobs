import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')
parser.add_argument('name')
args = parser.parse_args()
try:
    file = list(map(str.rstrip, open(args.name).readlines()))
    if args.sort:
        file = list(sorted(file))
    if args.num:
        print(*map(lambda x: ' '.join((str(x[0]), x[1])), enumerate(file)), sep='\n')
    else:
        print(*file)
    if args.count:
        print('rows count:', len(file))
except Exception as ex:
    print('ERROR')