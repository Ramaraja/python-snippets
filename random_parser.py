# parser

data = """
NAME: "1", "DESCR": "C1000"
PID: EC1K-TEST          , VID: V00  ,  SN: 193823648
OID: 1.2.3.4.5.6

NAME: "2", "DESCR": "C1000"
PID: EC1K-TEST          , VID: V00  ,  SN: 193823648
OID: 1.2.3.4.5.6
"""

def oid_parser(data):
    # assumed that the double newlines are seperate records
    records = data.split('\n\n')
    result = [] # to store the final result
    for item in records:
        # remove space, newline, tabs and flatterning
        flat_val = item.strip(' \n\t\"').replace("\n",",").replace('"', '')
        # still some spaces?? one more strip - Need to find a better way to do this.
        rec = [x.strip() for x in flat_val.split(',')]
        # convert to dict and store
        result.append(dict(r.strip(' ').split(':') for r in rec))
    return result


res = oid_parser(data)
print(res)

# test searching name and fetch oid

for item in res:
    if str(item.get("NAME")).strip() == "1":
        print(item.get("OID"))
