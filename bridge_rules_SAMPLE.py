'''
The following is an example for your bridge_rules file. Note, all bridging is ONE-WAY!
Rules for an IPSC network indicate destination IPSC network for the Group ID specified
(allowing transcoding of the Group ID to a different value). Group IDs are specified
as hex strings.

The IPSC name must match an IPSC name from dmrlink.cfg.

The example below cross-patches TGID 1 on an IPSC network named "IPSC_FOO" with TGID 2
on an IPSC network named "IPSC_BAR".

THIS EXAMPLE WILL NOT WORK AS IT IS - YOU MUST SPECIFY NAMES AND GROUP IDS!!!

NOTE: Timeslot transcoding does not yet work (SRC_TS) and (DST_TS) are ignored
'''

RULES = {
    'IPSC_FOO': {
        'GROUP_VOICE': [
            {'SRC_GROUP': b'\x00\x00\x01', 'SRC_TS': 1, 'DST_NET': 'IPSC_BAR', 'DST_GROUP': b'\x00\x00\x02', 'DST_TS': 1},
            # Repeat the above line for as many rules for this IPSC network as you want.
        ],
        'PRIVATE_VOICE': [
        ],
        'GROUP_DATA': [            
        ],
        'PRIVATE_DATA': [
        ]
    },
    'IPSC_BAR:' {
        'GROUP_VOICE': [
            {'SRC_GROUP': b'\x00\x00\x02', 'SRC_TS': 1, 'DST_NET': 'IPSC_FOO', 'DST_GROUP': b'\x00\x00\x01', 'DST_TS': 1},
            # Repeat the above line for as many rules for this IPSC network as you want.
        ],
        'PRIVATE_VOICE': [
        ],
        'GROUP_DATA': [            
        ],
        'PRIVATE_DATA': [
        ]
    }
}