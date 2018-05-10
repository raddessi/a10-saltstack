#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import salt
import salt.config

from a10_saltstack import errors as a10_ex
from a10_saltstack.axapi_http import client_factory
from a10_saltstack.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["activate","advertisement_interval","allowas_in","allowas_in_count","as_origination_interval","collide_established","connect","default_originate","description","disallow_infinite_holdtime","distribute_lists","dont_capability_negotiate","dynamic","ebgp_multihop","ebgp_multihop_hop_count","enforce_multihop","ethernet","inbound","lif","loopback","maximum_prefix","maximum_prefix_thres","neighbor_filter_lists","neighbor_prefix_lists","neighbor_route_map_lists","next_hop_self","override_capability","pass_encrypted","pass_value","passive","peer_group","peer_group_key","peer_group_remote_as","prefix_list_direction","remove_private_as","route_map","route_refresh","send_community_val","shutdown","strict_capability_match","timers_holdtime","timers_keepalive","trunk","tunnel","unsuppress_map","update_source_ip","update_source_ipv6","uuid","ve","weight",]

__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.loader.grains(__opts__)


ret = dict(
    name="a10_router_bgp_neighbor_peer_group_neighbor",
    changes={},
    original_message="",
    result=False,
    comment=""
)


def get_client(**kwargs):
    run_errors = []

    a10_host = __grains__["host"]
    a10_username = __grains__["username"]
    a10_password =__grains__["password"]
    a10_port = __grains__['port'] 
    a10_protocol = __grains__['protocol']
    version = __grains__['version']

    valid = True

    valid, validation_errors = validate(**kwargs)
    map(run_errors.append, validation_errors)

    if not valid:
        err_msg = "Validation failure\n".join(run_errors)
        ret['commment'] = err_msg
        return ret 

    return client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/bgp/{as-number}/neighbor/peer-group-neighbor/{peer-group}"
    f_dict = {}
    f_dict["peer-group"] = ""

    return url_base.format(**f_dict)

def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/bgp/{as-number}/neighbor/peer-group-neighbor/{peer-group}"
    f_dict = {}
    f_dict["peer-group"] = kwargs["peer-group"]

    return url_base.format(**f_dict)


def build_envelope(title, data):
    return {
        title: data
    }

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        if isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_json(title, **kwargs):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = kwargs.get(x)
        if v:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            if isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = kwargs[x]

    return build_envelope(title, rv)

def validate(**params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if params.get(x)])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def create(**kwargs):
    payload = build_json("peer-group-neighbor", **kwargs)
    try:
        client = get_client(**kwargs)
        post_result = client.post(new_url(), payload)
        ret["changes"].update(**post_result)
        ret["result"] = True
    except a10_ex.Exists:
        ret["result"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret

def delete(**kwargs):
    try:
        client = get_client(**kwargs)
        client.delete(existing_url(**kwargs))
        ret["result"] = True
    except a10_ex.NotFound:
        ret["result"] = False
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret

def update(**kwargs):
    payload = build_json("peer-group-neighbor", **kwargs)
    try:
        client = get_client(**kwargs)
        post_result = client.put(existing_url(**kwargs), payload)
        ret["changes"].update(**post_result)
        ret["result"] = True
    except a10_ex.ACOSException as ex:
        ret["comment"] = ex.msg
        return ret
    except Exception as gex:
        raise gex
    return ret