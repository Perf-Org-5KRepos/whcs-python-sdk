# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import configparser
import watson_health_cognitive_services.annotator_for_clinical_data as wh

CONFIG = configparser.RawConfigParser()
CONFIG.read('./tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_url')
VERSION = CONFIG.get('settings', 'version')
LEVEL = CONFIG.get('settings', 'logging_level')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
ACD = wh.AnnotatorForClinicalDataV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_annotators():
    response = ACD.list_annotators()
    assert response is not None
    for key in response:
        annotator = response[key]
        assert annotator is not None

def test_get_annotator():
    annotator = ACD.get_annotator('concept_detection')
    assert annotator.description is not None
    
def test_get_bad_annotator():
    try:
        annotator = ACD.get_annotator('concept_discovery')
    except wh.ACDException as acde:
        assert acde.code == 404