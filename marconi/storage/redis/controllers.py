# Copyright (c) 2013 Rackspace Hosting, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Exports Redis storage controllers.

Field Mappings:

    In order to reduce memory space used, fields name will be, most of
    the time, the first letter of their long name. Fields mapping will
    be updated and documented in each controller class.
"""

from marconi.storage.redis import claims
from marconi.storage.redis import messages
from marconi.storage.redis import queues

ClaimController = claims.ClaimController
MessageController = messages.MessageController
QueueController = queues.QueueController
