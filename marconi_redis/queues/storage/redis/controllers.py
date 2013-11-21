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
"""Exports Redis storage controllers."""
from marconi_redis.queues.storage.redis import catalogue
from marconi_redis.queues.storage.redis import claims
from marconi_redis.queues.storage.redis import messages
from marconi_redis.queues.storage.redis import queues
from marconi_redis.queues.storage.redis import shards

ClaimController = claims.ClaimController
MessageController = messages.MessageController
QueueController = queues.QueueController

CatalogueController = catalogue.CatalogueController
ShardsController = shards.ShardsController
