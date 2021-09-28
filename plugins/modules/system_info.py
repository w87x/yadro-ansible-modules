#!/usr/bin/python
# -*- coding: utf-8 -*-

# YADRO OpenBmc Ansible Collection
# Version 1.0.0
# Copyright (c) 2021 YADRO (KNS Group LLC)

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: system_info
short_description: Returns OpenBmc system information.
version_added: "1.0.0"
description: Returns OpenBmc system information.
extends_documentation_fragment:
  - yadro.obmc.auth_options
requirements:
    - "python >= 2.7.5"
author: "Radmir Safin (@radmirsafin)"
'''

RETURN = r'''
---
message:
  type: str
  description: Operation details.
  returned: always
  sample: System information successfully fetched.
system_info:
  type: dict
  description: Contains dictionary with system information.
  returned: success
  sample: {
    "bios_version": "1.3-gdace7e"
  }
'''

EXAMPLES = r'''
---
- name: Get server information
  yadro.obmc.system_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
  register: system_info
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.yadro.obmc.plugins.module_utils.client import OpenBmcClient


def main():
    module = AnsibleModule(
        argument_spec={
            "hostname": {"required": True, "type": "str"},
            "username": {"required": True, "type": "str"},
            "password": {"required": True, "type": "str", "no_log": True},
            "port": {"required": False, "default": 443, "type": 'int'},
            "verify_certs": {"required": False, "default": True, "type": "bool"},
        },
        supports_check_mode=True
    )

    try:
        client = OpenBmcClient(
            base_url=module.params["hostname"],
            username=module.params["username"],
            password=module.params["password"],
            verify_certs=module.params["verify_certs"],
        )
    except ImportError as e:
        module.fail_json(msg=e.msg)

    try:
        system_info = client.get_system_info()
    except Exception as e:
        module.fail_json(msg=e.msg)
    else:
        module.exit_json(msg="System information successfully read.", system_info=system_info)


if __name__ == '__main__':
    main()
