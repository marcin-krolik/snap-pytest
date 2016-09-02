#http://www.apache.org/licenses/LICENSE-2.0.txt
#
#
#Copyright 2016 Intel Corporation
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import logging
import os


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s [ %(levelname)s ] %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    log_lvl = os.environ.get('LARGE_TEST_DEBUG_LVL', 'INFO')
    logger.setLevel(log_lvl)
    logger.addHandler(handler)
    return logger

log = setup_custom_logger("logger")




