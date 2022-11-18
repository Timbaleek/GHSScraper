from HP_format import *

name = input('name?\n')
cid = get_cid_from_name(name)

print('\n'.join(format_for_word(cid, name, False)))
