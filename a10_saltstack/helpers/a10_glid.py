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
AVAILABLE_PROPERTIES = ["action_value","conn_limit","conn_rate_limit","conn_rate_limit_interval","dns","dns64","lockout","log","log_interval","num","over_limit_action","request_limit","request_rate_limit","request_rate_limit_interval","use_nat_pool","user_tag","uuid",]

REF_PROPERTIES = {
}

MODULE_NAME = "glid"

PARENT_KEYS = []

CHILD_KEYS = ["num",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/glid/{num}"
    f_dict = {}
    f_dict["num"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/glid/{num}"
    f_dict = {}
    f_dict["num"] = kwargs["num"]

    return url_base.format(**f_dict)