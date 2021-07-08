possible_values = {'id' : [x for x in range(1,5)],
					'name' : 'for name',
					'vlan_mode':['access', 'autostate', 'block', 'host', 'mode', 'nonegotioate', 'port-security', 'priority', 'private-vlan', 'protected', 'trunk', 'vepa', 'voice', '<cr>', 'none'],
					'Access': [178, 100, 1, 10, 101, 500, 'none'],
					'Speed': ['auto', '100', '1000', '10000'],
					'duplex': ['auto', 'half', 'full'],
					'shutdown':['yes','no']
					}

class gig1_int():

	def __init__(self, *args):
		i = 0
		self.attributes = []

		for attribute, value in possible_values.items():
			if args[0][i] not in value and i != 1:
				print(f'Invalid {attribute} please check for errors (type in all lowercase for properties that are not interface name)\n for allowed seperate vlans with a comma and space ex: \', \'')
				i += 1
				break
			self.attributes.append(args[0][i])
			i += 1
		if self.attributes[2] == 'trunk': self.attributes.append(str(args[0][i]).split(', '))
		self.prefix = 'g1/1/'