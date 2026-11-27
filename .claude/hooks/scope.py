"""Approve edits the scope guard would block. Approvals last 4 hours.

  python3 .claude/hooks/scope.py allow <client>   # edit another client's folder
  python3 .claude/hooks/scope.py allow core       # edit build.py / core/
  python3 .claude/hooks/scope.py status
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _kit

args = sys.argv[1:]
if len(args) == 2 and args[0] == "allow":
    name = args[1]
    if name != "core" and name not in _kit.all_clients():
        sys.exit(f"Unknown client '{name}'. Clients: {', '.join(_kit.all_clients())}")
    _kit.approve(name)
    print(f"Approved edits to {'build.py / core/' if name == 'core' else 'clients/' + name + '/'} for {_kit.APPROVAL_HOURS} hours.")
elif args == ["status"]:
    a = _kit._load(_kit.APPROVALS, {})
    live = {k: round((_kit.APPROVAL_HOURS * 3600 - (time.time() - t)) / 60) for k, t in a.items() if _kit.approved(k)}
    print("Active approvals: " + (", ".join(f"{k} ({m} min left)" for k, m in live.items()) or "none"))
else:
    print(__doc__)
