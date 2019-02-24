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
AVAILABLE_PROPERTIES = ["mx_name","priority","sampling_enable","ttl","uuid",]

MODULE_NAME = 'dns-mx-record'

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service_port}+{service-name}/dns-mx-record/{mx-name}"
    f_dict = {}
    f_dict["mx-name"] = ""
    f_dict["service-name"] = module.params["service-name"]
    f_dict["service_port"] = module.params["service_port"]
    f_dict["zone_name"] = module.params["zone_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service_port}+{service-name}/dns-mx-record/{mx-name}"
    f_dict = {}
    f_dict["mx-name"] = module.params["mx-name"]
    f_dict["service-name"] = module.params["service-name"]
    f_dict["service_port"] = module.params["service_port"]
    f_dict["zone_name"] = module.params["zone_name"]

    return url_base.format(**f_dict)