import pandas as pd
import numpy as np
import pytest
from unittest.mock import patch
from src.ragscope.utils.categorical import detect_mismatches



#### DETECTING MISMATCHES TESTS
@pytest.fixture
def sample_mismatches():
    ref_df=pd.DataFrame({
        "color":["red","blue","blue","red","yellow","yellow"]
    })

    ana_df=pd.DataFrame({
        "color":["red","red","blue","blue"]
    })

    return ref_df,ana_df

def test_detect_mistaches(sample_mismatches):
    ref_data,ana_data=sample_mismatches

    ref_miss,ana_miss=detect_mismatches(ref_data,ana_data,feature="color")

    assert ref_miss=={"yellow"}
    assert ana_miss==set()
