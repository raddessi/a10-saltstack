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
AVAILABLE_PROPERTIES = ["category_list_list","cloud_query_disable","database_server","db_update_time","enable","port","proxy_server","remote_syslog_enable","rtu_update_disable","rtu_update_interval","server","server_timeout","ssl_port","use_mgmt_port","uuid",]

REF_PROPERTIES = {
    "category_list_list": "/axapi/v3/web-category/category-list/{name}",
    "proxy_server": "/axapi/v3/web-category/proxy-server",
}

MODULE_NAME = "web-category"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/web-category"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/web-category"
    f_dict = {}

    return url_base.format(**f_dict)