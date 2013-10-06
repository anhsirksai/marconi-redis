# Copyright (c) 2013 Rackspace, Inc.
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

from marconi.tests.queues.storage import base as testing


@testing.requires_redis  # NOTE(cabrera): it's fine to define this here
class RedisDriverTest(testing.TestBase):

    def setUp(self):
        super(RedisDriverTest, self).setUp()
        self.load_conf('wsgi_redis.conf')

    def test_db_instance(self):
        driver = redis.Driver()
        # check we can obtain a DB instance


@testing.requires_redis
class RedisQueueTests(base.QueueControllerTests):

    driver_class = redis.Driver
    controller_class = controllers.QueueController

    def setUp(self):
        super(RedisQueueTests, self).setUp()
        self.load_conf('wsgi_redis.conf')

    def tearDown(self):
        self.controller.drop()
        super(RedisQueueTests, self).tearDown()


@testing.requires_redis
class RedisMessageTests(base.MessageControllerTests):

    driver_class = redis.Driver
    controller_class = controllers.MessageController

    def setUp(self):
        super(RedisMessageTests, self).setUp()
        self.load_conf('wsgi_redis.conf')

    def tearDown(self):
        self.controller.drop()
        super(RedisMessageTests, self).tearDown()


@testing.requires_redis
class RedisClaimTests(base.ClaimControllerTest):

    driver_class = redis.Driver
    controller_class = controllers.ClaimController

    def setUp(self):
        super(RedisClaimTests, self).setUp()
        self.load_conf('wsgi_redis.conf')

    def tearDown(self):
        self.controller.drop()
        super(RedisClaimTests, self).tearDown()