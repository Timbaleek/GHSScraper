from HP_format import *

namelist = []
cidlist = []

while True:
    tempname = input('name?\n')

    namelist.append(tempname)
    cidlist.append(get_cid_from_name(tempname))

    if input('continue?').upper() == 'N':
        break

for name, cid in zip(namelist, cidlist):
    print('\n'.join(format_for_word(cid, name, False)))
    print()
