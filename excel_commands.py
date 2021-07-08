from interface_specs.main import g1ls, gig1_ls, gig10_ls, gig25_ls, gig40_ls
from int_properties import int_properties

commands = ['config t']

for g1int in g1ls:

	# commands += int_properties(g1int, commands)

	int_id = str(g1int.attributes[0])
	name = str(g1int.attributes[1])
	mode = str(g1int.attributes[2])
	access = str(g1int.attributes[3])
	speed = str(g1int.attributes[4])
	duplex = str(g1int.attributes[5])
	shutdown = str(g1int.attributes[6])

	

	commands.append(f'int g1/0/{int_id}')
	commands.append(f'description {name}')

	if mode == 'none':
		commands.append('no switchport mode')
	else:
		commands.append(f'switchport mode {mode}')

	if access == 'none':
		commands.append('no switchport access')
	else:
		commands.append(f'switchport access vlan {access}')

	if speed == 'none':
		commands.append('no speed')
	else:
		commands.append(f'speed {speed}')

	commands.append(f'duplex {duplex}')
	commands.append(f'shutdown {shutdown}')

	if g1int.attributes[2] == 'trunk':
		access = g1int.attributes[7]
		commands.append(f'switchport trunk native vlan {access[0]}')
		for vlan in range(1,len(access)): commands.append(f'switchport trunk allowed vlan {access[vlan]}')

for gig1 in gig1_ls:

	int_id = str(gig1.attributes[0])
	name = str(gig1.attributes[1])
	mode = str(gig1.attributes[2])
	access = str(gig1.attributes[3])
	speed = str(gig1.attributes[4])
	duplex = str(gig1.attributes[5])
	shutdown = str(gig1.attributes[6])

	

	commands.append(f'int g1/1/{int_id}')
	commands.append(f'description {name}')

	if mode == 'none':
		commands.append('no switchport mode')
	else:
		commands.append(f'switchport mode {mode}')

	if access == 'none':
		commands.append('no switchport access')
	else:
		commands.append(f'switchport access vlan {access}')

	if speed == 'none':
		commands.append('no speed')
	else:
		commands.append(f'speed {speed}')

	commands.append(f'duplex {duplex}')
	commands.append(f'shutdown {shutdown}')

	if gig1.attributes[2] == 'trunk':
		access = gig1.attributes[7]
		commands.append(f'switchport trunk native vlan {access[0]}')
		for vlan in range(1,len(access)): commands.append(f'switchport trunk allowed vlan {access[vlan]}')

for gig10 in gig10_ls:

	int_id = str(gig10.attributes[0])
	name = str(gig10.attributes[1])
	mode = str(gig10.attributes[2])
	access = str(gig10.attributes[3])
	speed = str(gig10.attributes[4])
	duplex = str(gig10.attributes[5])
	shutdown = str(gig10.attributes[6])

	

	commands.append(f'int teng1/1/{int_id}')
	commands.append(f'description {name}')

	if mode == 'none':
		commands.append('no switchport mode')
	else:
		commands.append(f'switchport mode {mode}')

	if access == 'none':
		commands.append('no switchport access')
	else:
		commands.append(f'switchport access vlan {access}')

	if speed == 'none':
		commands.append('no speed')
	else:
		commands.append(f'speed {speed}')

	commands.append(f'duplex {duplex}')
	commands.append(f'shutdown {shutdown}')

	if gig10.attributes[2] == 'trunk':
		access = gig10.attributes[7]
		commands.append(f'switchport trunk native vlan {access[0]}')
		for vlan in range(1,len(access)): commands.append(f'switchport trunk allowed vlan {access[vlan]}')
	print('g10\'s done')

for gig25 in gig25_ls:

	int_id = str(gig25.attributes[0])
	name = str(gig25.attributes[1])
	mode = str(gig25.attributes[2])
	access = str(gig25.attributes[3])
	speed = str(gig25.attributes[4])
	duplex = str(gig25.attributes[5])
	shutdown = str(gig25.attributes[6])

	

	commands.append(f'int twentyfiveg1/1/{int_id}')
	commands.append(f'description {name}')

	if mode == 'none':
		commands.append('no switchport mode')
	else:
		commands.append(f'switchport mode {mode}')

	if access == 'none':
		commands.append('no switchport access')
	else:
		commands.append(f'switchport access vlan {access}')

	if speed == 'none':
		commands.append('no speed')
	else:
		commands.append(f'speed {speed}')

	commands.append(f'duplex {duplex}')
	commands.append(f'shutdown {shutdown}')

	if gig25.attributes[2] == 'trunk':
		access = gig25.attributes[7]
		commands.append(f'switchport trunk native vlan {access[0]}')
		for vlan in range(1,len(access)): commands.append(f'switchport trunk allowed vlan {access[vlan]}')
	print('g25\'s done')

for gig40 in gig40_ls:

	int_id = str(gig40.attributes[0])
	name = str(gig40.attributes[1])
	mode = str(gig40.attributes[2])
	access = str(gig40.attributes[3])
	speed = str(gig40.attributes[4])
	duplex = str(gig40.attributes[5])
	shutdown = str(gig40.attributes[6])

	commands.append(f'int fortyg1/1/{int_id}')
	commands.append(f'description {name}')

	if mode == 'none':
		commands.append('no switchport mode')
	else:
		commands.append(f'switchport mode {mode}')

	if access == 'none':
		commands.append('no switchport access')
	else:
		commands.append(f'switchport access vlan {access}')

	if speed == 'none':
		commands.append('no speed')
	else:
		commands.append(f'speed {speed}')

	commands.append(f'duplex {duplex}')
	commands.append(f'shutdown {shutdown}')

	if gig40.attributes[2] == 'trunk':
		access = gig40.attributes[7]
		commands.append(f'switchport trunk native vlan {access[0]}')
		for vlan in range(1,len(access)): commands.append(f'switchport trunk allowed vlan {access[vlan]}')
	print('g40\'s done')

commands.append('end')
commands.append('write')
# commands.append('copy running-config startup-config')