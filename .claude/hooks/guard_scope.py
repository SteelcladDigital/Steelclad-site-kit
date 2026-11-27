"""PreToolUse (Edit|Write|MultiEdit|NotebookEdit): keep each session on one client.

- The first client folder a session edits becomes that session's client.
- Edits to any other client's folder are blocked until the user approves.
- Edits to shared kit code (build.py, core/) are blocked until the user approves,
  because they change every client's site, including the live ones.
Approve with:  python3 .claude/hooks/scope.py allow <client>   (or: allow core)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _kit

data = _kit.read_input()
ti = data.get("tool_input") or {}
path = _kit.rel(ti.get("file_path") or ti.get("notebook_path") or ti.get("path"))
if not path:
    sys.exit(0)

sid = data.get("session_id")
st = _kit.session_state(sid)

if _kit.is_shared(path):
    if _kit.approved("core"):
        sys.exit(0)
    live = [c for c in _kit.all_clients(False) if _kit.config(c).get("launched")]
    _kit.block(
        f"Blocked: {path} is shared kit code. Changing it changes every client's site, "
        f"including {len(live)} live one(s): {', '.join(live) or 'none'}.\n"
        "If this client needs something different, do it in its own site.py instead.\n"
        "If a kit change is really needed, explain it to the user and ask first. "
        "Once they approve, run: python3 .claude/hooks/scope.py allow core")

client = _kit.client_of(path)
if not client:
    sys.exit(0)

if not st.get("client"):
    st["client"] = client
    _kit.save_session(sid, st)
    sys.exit(0)

if client == st["client"] or _kit.approved(client):
    sys.exit(0)

_kit.block(
    f"Blocked: this session is working on '{st['client']}', and {path} belongs to '{client}'. "
    "Editing it would change another client's website.\n"
    f"Ask the user first. Once they approve, run: python3 .claude/hooks/scope.py allow {client}")
