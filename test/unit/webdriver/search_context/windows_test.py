#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import httpretty
from selenium.webdriver.common import by

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement as MobileWebElement
from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body


class TestWebDriverWindowsSearchContext:
    @httpretty.activate
    def test_find_element_by_windows_uiautomation(self):
        driver = android_w3c_driver()
        element = MobileWebElement(driver, 'element_id')
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element/element_id/element'),
            body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "win-element-id"}}',
        )
        el = element.find_element(by=AppiumBy.WINDOWS_UI_AUTOMATION, value='win_element')

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['using'] == '-windows uiautomation'
        assert el.id == 'win-element-id'
