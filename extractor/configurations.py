# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("Source Data Extractor")

MAPPING_NAMES = {
    "labels": "2_training_annotations",
    "train": "2_training_set",
    "test": "1_test-std_set"
}
