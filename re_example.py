import re

data = """
+--------------------------------------+-------+--------+------------+-------------+--------------------------------------------------------+
| ID                                   | Name  | Status | Task State | Power State | Networks                                               |
+--------------------------------------+-------+--------+------------+-------------+--------------------------------------------------------+
| 31b1cfcc-ca85-48a9-a84a-8b222d377080 | VM1   | ACTIVE | -          | Running     | private=10.0.2.3                                       |
| f9743f1c-caeb-4892-af83-9dc0ac757545 | VM2   | ACTIVE | -          | Running     | private=10.0.2.4                                       |
| 83b547b9-9578-4840-997a-5aa1c4e829b0 | VM3-1 | ACTIVE | -          | Running     | private2=10.0.3.3                                      |
| 17b4685e-5cbe-4dd1-862a-6f89c191e1e7 | VM3-2 | ACTIVE | -          | Running     | private2=10.0.3.4                                      |
| ee4952a3-0700-42ea-aab3-7503bc9d87e2 | VM4   | ACTIVE | -          | Running     | private2=10.0.3.5; public=172.24.4.4; private=10.0.2.5 |
+--------------------------------------+-------+--------+------------+-------------+--------------------------------------------------------+
"""


def parse(parse_this):
    ips = []

    for line in parse_this:
        if re.search('^\+', line) or re.search('^$', line) or \
                re.search('Networks', line):
	    print line
            continue
        parts = line.split('|')
        parts = [x.strip() for x in parts]
	print parts
        vm = parts[2]
        networks = parts[6].split(';')
        networks = [x.strip() for x in networks]
	print networks
        for entry in networks:
            (network, ip) = entry.split(',')[0].split('=')
            ips.append(ip)
    print ips

parse(data.splitlines())
