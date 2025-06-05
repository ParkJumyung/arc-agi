from arc_agi_core import *
from importlib.util import find_spec

if find_spec("arc_agi_dsl"):
    import arc_agi_dsl as dsl

if find_spec("arc_agi_llm"):
    import arc_agi_llm as llm
