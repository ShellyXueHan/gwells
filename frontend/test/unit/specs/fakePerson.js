const fakePerson = JSON.parse(JSON.stringify({
  'person_guid': 'db0802c8-681e-4c65-8f2b-fd6dd3d2717a',
  'first_name': 'Corine',
  'surname': 'Navarro',
  'companies': [{
    'contact_at_guid': 'dcc8d473-6d43-4353-9edd-83d87957d3b8',
    'organization_name': 'Jasper Drilling Co.',
    'street_address': '4374 Cinder Common',
    'city': 'Sullivan Bay',
    'province_state': 'BC',
    'person_name': 'Corine Navarro',
    'person': 'db0802c8-681e-4c65-8f2b-fd6dd3d2717a',
    'org': '9f9937dc-8559-4418-ba22-9b9f0a94d456',
    'contact_tel': '(604) 135-2080',
    'contact_email': null
  }],
  'applications': [{
    'application_guid': '0c3fcd58-28b5-483d-ac69-e4d57cf43d0a',
    'person': 'db0802c8-681e-4c65-8f2b-fd6dd3d2717a',
    'file_no': null,
    'over19_ind': true,
    'registrar_notes': null,
    'reason_denied': null,
    'registrations': [{
      'activity': 'Well Driller',
      'activity_code': 'DRILL',
      'status': 'Active',
      'registration_no': 'WD 06179496',
      'registration_date': '2004-06-19',
      'register_removal_reason': null,
      'register_removal_date': null
    }],
    'classificationappliedfor_set': [{
      'registries_subactivity': {
        'registries_subactivity_guid': '1f6c30c2-018c-11e8-ba89-0ed5f89f718b',
        'code': 'GEOTECH',
        'description': 'Geotechnical/Environmental Driller',
        'qualificationcode_set': [{
          'code': 'GEO',
          'description': 'Geotechnical well'
        },
        {
          'code': 'MON',
          'description': 'Monitoring well'
        },
        {
          'code': 'REM',
          'description': 'Remediatation well'
        }
        ]
      },
      'primary_certificate_authority': null
    },
    {
      'registries_subactivity': {
        'registries_subactivity_guid': '1f6c2aaa-018c-11e8-ba89-0ed5f89f718b',
        'code': 'WATER',
        'description': 'Water Well Driller',
        'qualificationcode_set': [{
          'code': 'DEWAT',
          'description': 'Dewatering well'
        },
        {
          'code': 'GEO',
          'description': 'Geotechnical well'
        },
        {
          'code': 'RECH',
          'description': 'Recharge/Injection well'
        },
        {
          'code': 'REM',
          'description': 'Remediatation well'
        },
        {
          'code': 'MON',
          'description': 'Water supply well'
        },
        {
          'code': 'WAT',
          'description': 'Water supply well'
        }
        ]
      },
      'primary_certificate_authority': null
    }
    ],
    'registriesapplicationstatus_set': [{
      'status': 'Pending',
      'status_code': 'P',
      'notified_date': null,
      'effective_date': '2004-12-20',
      'expired_date': '2005-04-15'
    },
    {
      'status': 'Approved',
      'status_code': 'A',
      'notified_date': '2005-01-08',
      'effective_date': '2005-01-05',
      'expired_date': null
    }
    ]
  }],
  'create_user': 'DATALOAD_USER',
  'create_date': '2018-01-01T08:00:00Z',
  'update_user': 'DATALOAD_USER',
  'update_date': '2018-01-01T08:00:00Z'

}))

export default fakePerson
