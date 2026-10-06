import hmac,hashlib
from prbot.core import *
def test_sig():
 b=b"{}";s="x";assert verify(s,b,"sha256="+hmac.new(s.encode(),b,hashlib.sha256).hexdigest())
def test_files():assert pyfiles("+++ b/a.py\n+++ b/x.md")==["a.py"]
def test_funcs():assert funcs("def f(x):return x")==["f"]
def test_patch_generation():assert "test_f_edge_case" in generate_test_patch("pkg/a.py","def f():pass")
def test_commit():assert commit_request("o/r","t.py","x","feature","tok")["method"]=="PUT"
def test_delta():assert coverage_delta(60,85)==25
