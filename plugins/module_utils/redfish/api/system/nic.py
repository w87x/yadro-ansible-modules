# -*- coding: utf-8 -*-

# YADRO OpenBmc Ansible Collection
# Version 1.0.0
# Copyright (c) 2021 YADRO (KNS Group LLC)

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

try:
    from typing import Optional, ClassVar, Dict
except ImportError:
    # Satisfy Python 2 which doesn't have typing.
    Optional = ClassVar = Dict = None

from ansible_collections.yadro.obmc.plugins.module_utils.redfish.api.base import RedfishAPIObject


class NetworkInterface(RedfishAPIObject):

    @classmethod
    def select_version(cls, version):  # type: (str) -> Optional[ClassVar[Processor]]
        if version == "#NetworkInterface.v1_2_1.NetworkInterface":
            return NetworkInterface_v1_2_1

    def get_id(self):  # type: () -> str
        raise NotImplementedError("Method not implemented")
    
    def get_name(self): # type: () -> str
        raise NotImplementedError("Method not implemented")

    def get_mac(self): # type: () -> str
        raise NotImplementedError("Method not implemented")

    def get_health(self): #type: () -> str
        raise NotImplementedError("Method not implemented")    

    def get_state(self): #type: () -> str
        raise NotImplementedError("Method not implemented")

class NetworkInterface_v1_2_1(NetworkInterface):

    def __init__(self, *args, **kwargs):
        super(NetworkInterface_v1_2_1, self).__init__(*args, **kwargs)

    def get_id(self):  # type: () -> str
        return self._get_field("Id")

    def get_name(self): # type: () -> str
        return self._get_field("Name")

    def get_mac(self): # type: () -> str                
        f = self._client.get(self._get_field("NetworkDeviceFunctions")["@odata.id"]).json        
        if f["Members"]:       
            fn_data = self._client.get(f["Members"][0]["@odata.id"]).json
            return fn_data["Ethernet"]["PermanentMACAddress"]        

    def get_health(self): #type: () -> str
        f = self._client.get(self._get_field("NetworkDeviceFunctions")["@odata.id"]).json        
        if f["Members"]:       
            fn_data = self._client.get(f["Members"][0]["@odata.id"]).json
            return fn_data["Status"]["Health"]     

    def get_state(self): #type: () -> str
        f = self._client.get(self._get_field("NetworkDeviceFunctions")["@odata.id"]).json        
        if f["Members"]:       
            fn_data = self._client.get(f["Members"][0]["@odata.id"]).json
            return fn_data["Status"]["State"]     