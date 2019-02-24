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
AVAILABLE_PROPERTIES = ["record_name","sampling_enable","ttl","txt_data","uuid",]

MODULE_NAME = dns-txt-record

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service_service_port}+{{service_port}_service_name}/dns-txt-record/{record-name}"
    f_dict = {}
    f_dict["record-name"] = ""
    f_dict["service_port_service_name"] = module.params["service_port_service_name"]
    f_dict["service_service_port"] = module.params["service_service_port"]
    f_dict["zone_name"] = module.params["zone_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service_service_port}+{{service_port}_service_name}/dns-txt-record/{record-name}"
    f_dict = {}
    f_dict["record-name"] = module.params["record-name"]
    f_dict["service_port_service_name"] = module.params["service_port_service_name"]
    f_dict["service_service_port"] = module.params["service_service_port"]
    f_dict["zone_name"] = module.params["zone_name"]

    return url_base.format(**f_dict)