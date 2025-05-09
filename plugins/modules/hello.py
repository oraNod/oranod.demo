#!/usr/bin/python
# Copyright: (c) 2025, Don Naro <dnaro@redhat.com>
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import annotations

__metaclass__ = type

DOCUMENTATION = r'''
---
module: hello
short_description: Module to create a greeting
version_added: "1.0.0"
description:
    - Create a greeting for a special kitty.
options:
    cat:
        description:
            - The name of the cat to greet.
        type: str
        required: true
    greeting:
        description:
            - The greeting to use.
        type: str
        required: true
author:
    - Don Naro (@oranod)
'''

EXAMPLES = r'''
# Greet a kitty
- name: Greet Nora
  hello:
    cat: Nora
    greeting: Hello
'''

RETURN = r'''
message:
    description: The generated greeting message
    type: str
    returned: always
    sample: "Hello, Nora!"
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.helper import create_greeting


def main():
    module = AnsibleModule(
        argument_spec=dict(
            cat=dict(type='str', required=True),
            greeting=dict(type='str', required=True),
        ),
        supports_check_mode=True
    )

    cat = module.params['cat']
    greeting = module.params['greeting']

    message = create_greeting(greeting, cat)

    module.exit_json(
        changed=False,
        message=message
    )


if __name__ == '__main__':
    main()
