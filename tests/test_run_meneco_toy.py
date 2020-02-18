# Feature: meneco
# 	Script to run meneco
#
# Scenario: Run meneco on toy example
# 	Given toy example
# 	And output directory
# 	When run meneco
# 	Then have repaired network
# 	And it contains expected reactions

import os
from pathlib import Path  # noqa: F401
from pyasp.term import *
import tempfile

import meneco

def reaction_ids(prediction):
    return set([p.arg(0) for p in prediction if p.pred() == "xreaction"])
    
def test_run_meneco_toy():
    toy = Path('.') / "toy"

    unprod, recon_targets, one_min, intersection, union, enum = meneco.run_meneco(
        str(toy / "draft.sbml"),
        str(toy / "seeds.sbml"),
        str(toy / "targets.sbml"),
        str(toy / "repair.sbml"),
        False
    )

    assert len(unprod) == 31
    assert reaction_ids(recon_targets) == set([])
    assert reaction_ids(one_min) == set(['"R_CU2tpp"', '"R_CLt3_2pp"'])
    assert reaction_ids(intersection) == set(['"R_CU2tpp"', '"R_CLt3_2pp"'])
    assert reaction_ids(union) == set(['"R_CU2tpp"', '"R_CLt3_2pp"'])
