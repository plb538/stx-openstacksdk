# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Copyright (c) 2016 Wind River Systems, Inc.
#

from openstack.network import network_service
from openstack import resource2 as resource


class Providernet(resource.Resource):
    resource_key = 'providernet'
    resources_key = 'providernets'
    base_path = '/wrs-provider/providernets'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    _query_mapping = resource.QueryParameters(
        'type',
    )

    # Properties
    status = resource.Body('status')
    description = resource.Body('description')
    mtu = resource.Body('mtu', type=int)
    ranges = resource.Body('ranges', type=list)
    vlan_transparent = resource.Body('vlan_transparent', type=bool)
    type = resource.Body('type')
    id = resource.Body('id')
    name = resource.Body('name')