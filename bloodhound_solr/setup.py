# -*- coding: UTF-8 -*-

#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from setuptools import setup, find_packages


PKG_INFO = {
    'bhsolr': ['../README', '../TESTING_README'],
    'bhsolr.search_resources' : [],
    'bhsolr.tests': ['*.*'],
    'bhsolr.tests.search_resources': ['*.*'],
    }


ENTRY_POINTS = {
    'trac.plugins': [
    'bhsolr.admin = bhsolr.admin',
    'bhsolr.schema = bhsolr.schema',
    'bhsolr.solr_backend = bhsolr.solr_backend',
    'bhsolr.search_resources.ticket_search = \
                                        bhsolr.search_resources.ticket_search',
    'bhsolr.search_resources.milestone_search = \
                                    bhsolr.search_resources.milestone_search',
    'bhsolr.search_resources.changeset_search = \
                                    bhsolr.search_resources.changeset_search',
    'bhsolr.search_resources.wiki_search = bhsolr.search_resources.wiki_search'
    ],}


setup(
    name = 'BloodhoundSolrPlugin',
    version = '0.1',
    description = "Apache Solr support for Apache(TM) Bloodhound.",
    author = "Apache Bloodhound",
    license = "Apache License v2",
    url = "http://bloodhound.apache.org/",
    requires = ['trac', 'lxml', 'sunburnt', 'httplib2'],
    packages = find_packages(),
    package_data = PKG_INFO,
    include_package_data=True,
    entry_points = ENTRY_POINTS,
    test_suite='bhsolr.tests.test_suite',
    )