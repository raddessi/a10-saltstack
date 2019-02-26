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
AVAILABLE_PROPERTIES = ["inside","inside_port_end","inside_port_start","nat","nat_port_end","nat_port_start","uuid",]

MODULE_NAME = 'port-reservation'

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/lsn/port-reservation/{inside}+{inside-port-start}+{inside-port-end}+{nat}+{nat-port-start}+{nat-port-end}"
    f_dict = {}
    f_dict["inside"] = ""
    f_dict["inside-port-start"] = ""
    f_dict["inside-port-end"] = ""
    f_dict["nat"] = ""
    f_dict["nat-port-start"] = ""
    f_dict["nat-port-end"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/lsn/port-reservation/{inside}+{inside-port-start}+{inside-port-end}+{nat}+{nat-port-start}+{nat-port-end}"
    f_dict = {}
    f_dict["inside"] = kwargs["inside"]
    f_dict["inside-port-start"] = kwargs["inside-port-start"]
    f_dict["inside-port-end"] = kwargs["inside-port-end"]
    f_dict["nat"] = kwargs["nat"]
    f_dict["nat-port-start"] = kwargs["nat-port-start"]
    f_dict["nat-port-end"] = kwargs["nat-port-end"]

    return url_base.format(**f_dict)