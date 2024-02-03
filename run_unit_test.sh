#!/bin/bash
# echo
# echo Running TestApplicationConfig.test_initialise_config_file...
# python3 -m unittest Unit_tests.application_config_test.TestApplicationConfig.test_initialise_config_file

# echo
# echo Running TestApplicationConfig.test_get_config...
# python3 -m unittest Unit_tests.application_config_test.TestApplicationConfig.test_get_config

# echo
# echo Running TestApplicationConfig.test_update_config...
# python3 -m unittest Unit_tests.application_config_test.TestApplicationConfig.test_update_config

echo
echo Running TestMainPage.test_update_config...
python3 -m unittest Unit_tests.main_page_test.TestMainPage.test_update_config

echo
echo Running test_fly_drones.py
python3 test_fly_drones.py

echo
echo test_coord_conversion.py
python3 test_coord_conversion.py