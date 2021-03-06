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
AVAILABLE_PROPERTIES = ["admin_ip","as_backup","as_replace","disable","dns_a_record_ip","no_resp","sampling_enable","static","ttl","uuid","weight","service_name","service_port","zone_name",]

REF_PROPERTIES = {
}

MODULE_NAME = "dns-a-record-ipv4"

PARENT_KEYS = ["service-name","service_port","zone_name",]

CHILD_KEYS = ["dns-a-record-ip",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service_port}+{service-name}/dns-a-record/dns-a-record-ipv4/{dns-a-record-ip}"
    f_dict = {}
    f_dict["dns-a-record-ip"] = ""
    f_dict["service-name"] = kwargs["service-name"]
    f_dict["service_port"] = kwargs["service_port"]
    f_dict["zone_name"] = kwargs["zone_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service_port}+{service-name}/dns-a-record/dns-a-record-ipv4/{dns-a-record-ip}"
    f_dict = {}
    f_dict["dns-a-record-ip"] = kwargs["dns-a-record-ip"]
    f_dict["service-name"] = kwargs["service-name"]
    f_dict["service_port"] = kwargs["service_port"]
    f_dict["zone_name"] = kwargs["zone_name"]

    return url_base.format(**f_dict)