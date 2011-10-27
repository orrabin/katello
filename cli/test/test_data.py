try:
    import json
except ImportError:
    import simplejson as json


ORGS = [
  {
    "name": "ACME_Corporation",
    "created_at": "2011-08-23T08:10:52Z",
    "updated_at": "2011-08-23T08:10:52Z",
    "id": 1,
    "cp_key": "ACME_Corporation",
    "description": "ACME Corporation Organization"
  }
]

ENVS = [
  {
    "name": "Locker",
    "prior": None,
    "created_at": "2011-08-23T08:10:53Z",
    "locker": True,
    "updated_at": "2011-08-23T08:10:53Z",
    "id": 1,
    "organization": "ACME_Corporation",
    "description": None,
    "organization_id": 1
  },
  {
    "name": "Dev",
    "prior": "Locker",
    "created_at": "2011-08-24T08:25:52Z",
    "locker": False,
    "updated_at": "2011-08-24T08:25:52Z",
    "id": 2,
    "organization": "ACME_Corporation",
    "description": None,
    "organization_id": 1
  },
  {
    "name": "Prod",
    "prior": "Dev",
    "created_at": "2011-08-24T08:26:01Z",
    "locker": False,
    "updated_at": "2011-08-24T08:26:01Z",
    "id": 3,
    "organization": "ACME_Corporation",
    "description": None,
    "organization_id": 1
  }
]

LOCKER = ENVS[0]

PROVIDERS = [
  {
    "name": "porkchop",
    "created_at": "2011-08-29T08:19:02Z",
    "updated_at": "2011-08-29T08:19:02Z",
    "id": 1,
    "sync_state": "not_synced",
    "repository_url": "http://download.fedoraproject.org/pub/fedora/linux/releases/",
    "last_sync": None,
    "description": None,
    "organization_id": 1,
    "provider_type": "Custom"
  },
  {
    "name": "redhat",
    "created_at": "2011-08-29T08:19:03Z",
    "updated_at": "2011-08-29T08:19:03Z",
    "id": 2,
    "sync_state": "not_synced",
    "repository_url": "https://somehost.example.com/content/",
    "last_sync": None,
    "description": None,
    "organization_id": 1,
    "provider_type": "Red Hat"
  },
  {
    "name": "prov_a1",
    "created_at": "2011-08-29T08:22:30Z",
    "updated_at": "2011-08-29T08:22:30Z",
    "id": 3,
    "sync_state": "not_synced",
    "repository_url": None,
    "last_sync": "2011-08-29T14:03:02+02:00",
    "description": None,
    "organization_id": 1,
    "provider_type": "Custom"
  },
  {
    "name": "prov_a2",
    "created_at": "2011-08-29T08:22:31Z",
    "updated_at": "2011-08-29T08:22:31Z",
    "id": 4,
    "sync_state": "not_synced",
    "repository_url": None,
    "last_sync": None,
    "description": None,
    "organization_id": 1,
    "provider_type": "Custom"
  }
]

SLA_VALUE = "1"

PRODUCTS = [
  {
    "last_sync": None,
    "name": "prod_a1",
    "created_at": "2011-08-25T11:50:59Z",
    "productContent": [
      {
        "enabled": False,
        "content": {
          "label": "1314273058712_prod_a1_dummy_repos_zoo",
          "name": "prod_a1_dummy_repos_zoo",
          "contentUrl": "http://tstrachota.fedorapeople.org/dummy_repos/zoo",
          "id": "1314273063319",
          "type": "yum",
          "gpgUrl": "",
          "vendor": "Custom",
          "modifiedProductIds": [

          ],
          "updated": "2011-08-25T11:51:03.319+0000",
          "created": "2011-08-25T11:51:03.319+0000"
        }
      }
    ],
    "provider_id": 3,
    "multiplier": 1,
    "attributes": [
      {
        "name": "sla",
        "value": SLA_VALUE
      }
    ],
    "multiplier": 1,
    "updated_at": "2011-08-25T11:50:59Z",
    "sync_plan_id": 25,
    "id": 1,
    "provider_name": "prov_a1",
    "description": None,
    "sync_state": "not_synced",
    "id": "1314273058712"
  },
  {
    "last_sync": None,
    "name": "prod_a2",
    "created_at": "2011-08-25T11:51:06Z",
    "productContent": [
      {
        "enabled": False,
        "content": {
          "label": "1314273066523_prod_a2_fakerepos_fewupdates",
          "name": "prod_a2_fakerepos_fewupdates",
          "contentUrl": "http://lzap.fedorapeople.org/fakerepos/fewupdates",
          "id": "1314273077303",
          "type": "yum",
          "gpgUrl": "",
          "vendor": "Custom",
          "modifiedProductIds": [

          ],
          "updated": "2011-08-25T11:51:17.304+0000",
          "created": "2011-08-25T11:51:17.304+0000"
        }
      },
      {
        "enabled": False,
        "content": {
          "label": "1314273066523_prod_a2_fakerepos_zoo",
          "name": "prod_a2_fakerepos_zoo",
          "contentUrl": "http://lzap.fedorapeople.org/fakerepos/zoo",
          "id": "1314273074824",
          "type": "yum",
          "gpgUrl": "",
          "vendor": "Custom",
          "modifiedProductIds": [

          ],
          "updated": "2011-08-25T11:51:14.824+0000",
          "created": "2011-08-25T11:51:14.824+0000"
        }
      }
    ],
    "provider_id": 3,
    "multiplier": 1,
    "attributes": [

    ],
    "multiplier": 1,
    "updated_at": "2011-08-25T11:51:06Z",
    "sync_plan_id": 25,
    "id": 2,
    "provider_name": "prov_a1",
    "description": None,
    "sync_state": "not_synced",
    "id": "1314273066523"
  }
]

COMMON_ASYNC_RESULT_SUCCESS = [
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": None,
    "uuid": "6d3d8711-cf28-11e0-b10e-f0def13c24e5",
    "updated_at": None,
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "finished",
    "start_time": "2011-08-25T14:42:16Z"
  }
]


SYNC_RESULT_NOT_SYNCED = [
  {
    "result": None,
    "created_at": None,
    "uuid": None,
    "updated_at": None,
    "progress": {
      "size_left": 0,
      "total_size": 0,
      "total_count": 0,
      "items_left": 0
    },
    "finish_time": None,
    "organization_id": None,
    "state": "not_synced",
    "start_time": None
  },
  {
    "result": None,
    "created_at": None,
    "uuid": None,
    "updated_at": None,
    "progress": {
      "size_left": 0,
      "total_size": 0,
      "total_count": 0,
      "items_left": 0
    },
    "finish_time": None,
    "organization_id": None,
    "state": "not_synced",
    "start_time": None
  }
]


SYNC_RESULT_WITHOUT_ERROR = [
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": None,
    "uuid": "6d3d8711-cf28-11e0-b10e-f0def13c24e5",
    "updated_at": None,
    "progress": {
      "error_details": [

      ],
      "size_left": 0,
      "total_size": 17872,
      "total_count": 8,
      "items_left": 0
    },
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "finished",
    "start_time": "2011-08-25T14:42:16Z"
  },
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": None,
    "uuid": "6d523975-cf28-11e0-b196-f0def13c24e5",
    "updated_at": None,
    "progress": {
      "error_details": [

      ],
      "size_left": 0,
      "total_size": 3170837,
      "total_count": 7,
      "items_left": 0
    },
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "finished",
    "start_time": "2011-08-25T14:42:16Z"
  }
]


SYNC_RESULT_WITH_ERROR = [
  {
    "result": "{\"errors\":[\"some error 1\",\"some error 2\"]}",
    "created_at": None,
    "uuid": "6d3d8711-cf28-11e0-b10e-f0def13c24e5",
    "updated_at": None,
    "progress": {
      "error_details": [

      ],
      "size_left": 17872,
      "total_size": 17872,
      "total_count": 8,
      "items_left": 8
    },
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "error",
    "start_time": "2011-08-25T14:42:16Z"
  },
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": None,
    "uuid": "6d523975-cf28-11e0-b196-f0def13c24e5",
    "updated_at": None,
    "progress": {
      "error_details": [

      ],
      "size_left": 3170837,
      "total_size": 3170837,
      "total_count": 7,
      "items_left": 7
    },
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "canceled",
    "start_time": "2011-08-25T14:42:16Z"
  }
]

SYNC_RESULT_CANCELLED = [
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": None,
    "uuid": "6d3d8711-cf28-11e0-b10e-f0def13c24e5",
    "updated_at": None,
    "progress": {
      "error_details": [

      ],
      "size_left": 17872,
      "total_size": 17872,
      "total_count": 8,
      "items_left": 8
    },
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "canceled",
    "start_time": "2011-08-25T14:42:16Z"
  },
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": None,
    "uuid": "6d523975-cf28-11e0-b196-f0def13c24e5",
    "updated_at": None,
    "progress": {
      "error_details": [

      ],
      "size_left": 3170837,
      "total_size": 3170837,
      "total_count": 7,
      "items_left": 7
    },
    "finish_time": "2011-08-25T14:42:21Z",
    "organization_id": None,
    "state": "canceled",
    "start_time": "2011-08-25T14:42:16Z"
  }
]


SYNC_RUNNING_RESULT = [
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": "2011-08-25T14:44:17Z",
    "uuid": "b57a9d75-cf28-11e0-8a7a-f0def13c24e5",
    "updated_at": "2011-08-25T14:44:17Z",
    "progress": {
      "error_details": [

      ],
      "size_left": 9883,
      "total_size": 17872,
      "total_count": 8,
      "items_left": 5
    },
    "id": 3,
    "finish_time": None,
    "organization_id": 1,
    "state": "running",
    "start_time": None
  },
  {
    "result": "{\"errors\":[null,null]}",
    "created_at": "2011-08-25T14:44:17Z",
    "uuid": "b58a9635-cf28-11e0-8ae3-f0def13c24e5",
    "updated_at": "2011-08-25T14:44:17Z",
    "progress": {
      "error_details": [

      ],
      "size_left": 0,
      "total_size": 0,
      "total_count": 0,
      "items_left": 0
    },
    "id": 4,
    "finish_time": None,
    "organization_id": 1,
    "state": "waiting",
    "start_time": None
  }
]


EMPTY_CHANGESET ={
    "name": "CS",
    "products": [

    ],
    "created_at": "2011-08-26T09:02:01Z",
    "errata": [

    ],
    "updated_at": "2011-08-26T09:02:01Z",
    "task_status_id": None,
    "promotion_date": None,
    "repos": [

    ],
    "packages": [

    ],
    "id": 1,
    "environment_id": 2,
    "description": None,
    "state": "new"
}

CHANGESETS = [
    EMPTY_CHANGESET
]


REPOS = [
    {
    "package_count": 0,
    "name": "prod_a2_fakerepos_zoo",
    "clone_ids": [

    ],
    "keys": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/keys/",
    "uri_ref": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/",
    "use_symlinks": False,
    "content_types": "yum",
    "packagegroupcategories": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/packagegroupcategories/",
    "consumer_cert": None,
    "errata": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/errata/",
    "files": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/files/",
    "notes": None,
    "relative_path": "fakerepos/zoo",
    "arch": "noarch",
    "checksum_type": "sha256",
    "_id": "1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation",
    "packages": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/packages/",
    "next_scheduled_time": None,
    "sync_state": "not_synced",
    "id": "1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation",
    "publish": True,
    "last_sync": None,
    "comps": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/comps/",
    "filters": [

    ],
    "sync_schedule": None,
    "files_count": 82,
    "groupid": [
        "product:1314606161997",
        "env:1",
        "org:1"
    ],
    "packagegroups": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/packagegroups/",
    "distribution": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_zoo-ACME_Corporation/distribution/",
    "distributionid": [

    ],
    "consumer_ca": None,
    "source": {
        "url": "http://lzap.fedorapeople.org/fakerepos/zoo",
        "type": "remote"
    },
    "feed_cert": None,
    "feed_ca": None
    },
    {
    "package_count": 0,
    "name": "prod_a2_fakerepos_fewupdates",
    "clone_ids": [

    ],
    "keys": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/keys/",
    "uri_ref": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/",
    "use_symlinks": False,
    "content_types": "yum",
    "packagegroupcategories": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/packagegroupcategories/",
    "consumer_cert": None,
    "errata": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/errata/",
    "files": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/files/",
    "notes": None,
    "relative_path": "fakerepos/fewupdates",
    "arch": "noarch",
    "checksum_type": "sha256",
    "_id": "1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation",
    "packages": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/packages/",
    "next_scheduled_time": None,
    "sync_state": "not_synced",
    "id": "1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation",
    "publish": True,
    "last_sync": None,
    "comps": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/comps/",
    "filters": [

    ],
    "sync_schedule": None,
    "files_count": 89,
    "groupid": [
        "product:1314606161997",
        "env:1",
        "org:1"
    ],
    "packagegroups": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/packagegroups/",
    "distribution": "/pulp/api/repositories/1314606161997-prod_a2_fakerepos_fewupdates-ACME_Corporation/distribution/",
    "distributionid": [

    ],
    "consumer_ca": None,
    "source": {
        "url": "http://lzap.fedorapeople.org/fakerepos/fewupdates",
        "type": "remote"
    },
    "feed_cert": None,
    "feed_ca": None
    }
]

PACKAGE_GROUPS = [
{"name": "katello",
  "conditional_package_names": {},
  "mandatory_package_names": [],
  "default": True,
  "_id": "123",
  "langonly": None,
  "id": "123",
  "immutable": False,
  "optional_package_names": [],
  "default_package_names": ["pulp-test-package-0.2.1-1.fc11.x86_64.rpm"],
  "translated_description": {},
  "user_visible": True,
  "display_order": 1024,
  "repo_defined": False,
  "description": "Katello related packages",
  "translated_name": {}
  }
]

PACKAGE_GROUP_CATEGORIES = [
{"name": "Development",
  "_id": "development",
  "id": "development",
  "immutable": False,
  "translated_description": {},
  "display_order": 99,
  "repo_defined": False,
  "description": "",
  "packagegroupids": ["123"],
  "translated_name": {}}
]


TEMPLATES = [
{
  "name": "tpl_a1",
  "products": [
    {
      "productContent": [

      ],
      "name": "prod_a1",
      "multiplier": 1,
      "created_at": "2011-09-06T11:43:43Z",
      "product_id": 1,
      "provider_id": 3,
      "sync_state": "finished",
      "attributes": [

      ],
      "multiplier": 1,
      "updated_at": "2011-09-06T11:43:43Z",
      "sync_plan_id": 25,
      "last_sync": "2011-09-06T13:44:16+02:00",
      "id": 1,
      "system_template_id": 2,
      "description": None,
      "id": "1315309422793"
    },
    {
      "productContent": [

      ],
      "name": "prod_a2",
      "multiplier": 1,
      "created_at": "2011-09-06T11:43:54Z",
      "product_id": 2,
      "provider_id": 3,
      "sync_state": "finished",
      "attributes": [

      ],
      "multiplier": 1,
      "updated_at": "2011-09-06T11:43:54Z",
      "sync_plan_id": 25,
      "last_sync": "2011-09-06T13:44:33+02:00",
      "id": 2,
      "system_template_id": 2,
      "description": None,
      "id": "1315309434001"
    }
  ],
  "package_groups":
    [{"id":1,
      "system_template_id":1,
      "repo_id":"1316523009485-base-one-ACME_Corporation",
      "package_group_id":"test"}],
   "pg_categories":
    [{"pg_category_id":"test",
      "id":1,
      "system_template_id":1,
      "repo_id":"1316523009485-base-one-ACME_Corporation"}],
  "created_at": "2011-09-06T11:47:44Z",
  "updated_at": "2011-09-06T11:51:07Z",
  "packages": [
    {
      "system_template_id": 2,
      "id": 1,
      "package_name": "walrus",
      "version": "0.1",
      "release": "0.2",
      "epoch": "1",
      "arch": "noarch"
    },
    {
      "system_template_id": 2,
      "id": 2,
      "package_name": "cheetah",
      "version": None,
      "release": None,
      "epoch": None,
      "arch": None
    }
  ],
  "id": 2,
  "revision": 2,
  "parent_id": None,
  "environment_id": 1,
  "description": "template in ACME_Corporation in a locker",
  "parameters_json": "{\"param_1\":\"param_value\"}",
  "parameters": {
    "param_1": "param_value"
  },
  "package_groups": [],
  "pg_categories": [],
}
]

POOL = {
  "href": "/pools/40288ae9333fe87201334033dd21001b",
  "sourceEntitlement": None,
  "productId": "1319632099512",
  "accountNumber": "",
  "quantity": -1,
  "restrictedToUsername": None,
  "attributes": [

  ],
  "subscriptionId": "40288ae9333fe87201334033da7e001a",
  "startDate": "2011-10-26T00:00:00.000+0000",
  "id": "40288ae9333fe87201334033dd21001b",
  "productAttributes": [

  ],
  "productName": "first",
  "activeSubscription": True,
  "updated": "2011-10-26T12:28:20.641+0000",
  "contractNumber": "",
  "endDate": "2041-10-18T00:00:00.000+0000",
  "providedProducts": [

  ],
  "created": "2011-10-26T12:28:20.641+0000",
  "consumed": 0,
  "owner": {
    "href": "/owners/ACME_Corporation",
    "displayName": "ACME_Corporation",
    "id": "40288ae9333fe87201333fe956790018",
    "key": "ACME_Corporation"
  }
}
