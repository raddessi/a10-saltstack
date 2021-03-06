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
AVAILABLE_PROPERTIES = ["basic_mapping_rule","default_mapping_rule","description","health_check_gateway","mtu","name","sampling_enable","tcp","user_tag","uuid",]

REF_PROPERTIES = {
    "basic_mapping_rule": "/axapi/v3/cgnv6/map/translation/domain/{name}/basic-mapping-rule",
    "default_mapping_rule": "/axapi/v3/cgnv6/map/translation/domain/{name}/default-mapping-rule",
    "health_check_gateway": "/axapi/v3/cgnv6/map/translation/domain/{name}/health-check-gateway",
}

MODULE_NAME = "domain"

PARENT_KEYS = []

CHILD_KEYS = ["name",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/map/translation/domain/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/map/translation/domain/{name}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]

    return url_base.format(**f_dict)