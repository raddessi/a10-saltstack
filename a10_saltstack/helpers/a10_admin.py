# Copyright 2019 A10 Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["access","access_list","action","passwd_string","password","password_key","privilege_global","privilege_list","ssh_pubkey","trusted_host","trusted_host_acl_id","trusted_host_cidr","unlock","user","user_tag","uuid",]

REF_PROPERTIES = {
    "access": "/axapi/v3/admin/{user}/access",
    "password": "/axapi/v3/admin/{user}/password",
    "ssh_pubkey": "/axapi/v3/admin/{user}/ssh-pubkey",
}

MODULE_NAME = "admin"

PARENT_KEYS = []

CHILD_KEYS = ["user",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/admin/{user}"
    f_dict = {}
    f_dict["user"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/admin/{user}"
    f_dict = {}
    f_dict["user"] = kwargs["user"]

    return url_base.format(**f_dict)