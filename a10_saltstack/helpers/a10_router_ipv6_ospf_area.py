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
AVAILABLE_PROPERTIES = ["area_ipv4","area_num","default_cost","no_summary","range_list","stub","uuid","virtual_link_list",]

MODULE_NAME = area

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/ipv6/ospf/{ospf_process_id}/area/{area-ipv4}+{area-num}"
    f_dict = {}
    f_dict["area-ipv4"] = ""
    f_dict["area-num"] = ""
    f_dict["ospf_process_id"] = module.params["ospf_process_id"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/ipv6/ospf/{ospf_process_id}/area/{area-ipv4}+{area-num}"
    f_dict = {}
    f_dict["area-ipv4"] = module.params["area-ipv4"]
    f_dict["area-num"] = module.params["area-num"]
    f_dict["ospf_process_id"] = module.params["ospf_process_id"]

    return url_base.format(**f_dict)