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
AVAILABLE_PROPERTIES = ["gslb_device_cfg","gslb_geo_location_cfg","gslb_ip_list_cfg","gslb_policy_cfg","gslb_service_cfg","gslb_service_ip_cfg","gslb_service_port_cfg","gslb_site_cfg","gslb_svc_group_cfg","gslb_template_cfg","gslb_zone_cfg","health_monitor_cfg","real_port_cfg","real_server_cfg","service_group_cfg","threshold","uuid","virtual_server_cfg",]

MODULE_NAME = app-resources

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/system/resource-accounting/template/{template_name}/app-resources"
    f_dict = {}
    f_dict["template_name"] = module.params["template_name"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/system/resource-accounting/template/{template_name}/app-resources"
    f_dict = {}
    f_dict["template_name"] = module.params["template_name"]

    return url_base.format(**f_dict)