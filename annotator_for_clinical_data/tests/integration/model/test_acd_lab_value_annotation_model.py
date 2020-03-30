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

import watson_health_cognitive_services.annotator_for_clinical_data as wh

def test_LabValueAnnotation_model():
    model = wh.LabValueAnnotation(id="id", type="type", uid=1, begin=2, end=3, covered_text="covered",
                                  negated=False, hypothetical=False, loinc_id="loinc", low_value="1",
                                  date_in_milliseconds="20", lab_type_surface_form="ltsf",
                                  lab_type_normalized_name="ltnn", lab_value="labValue",
                                  section_normalized_name="snn", section_surface_form="ssf", extra="more")
    assert model.__str__() is not None