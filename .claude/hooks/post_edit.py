"""PostToolUse (Edit|Write|MultiEdit): rebuild right after a change so mistakes surface immediately.

- Client file edited  -> deploy build + standards scan for that client.
- build.py / core/ edited -> deploy build of EVERY client, so a kit change can't quietly break another site.
Problems are fed back to Claude (exit 2). The edit itself is never undone.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _kit

data = _kit.read_input()
ti = data.get("tool_input") or {}
path = _kit.rel(ti.get("file_path"))
if not path:
    sys.exit(0)

client = _kit.client_of(path)
shared = _kit.is_shared(path)
if not client and not shared:
    sys.exit(0)

sid = data.get("session_id")
st = _kit.session_state(sid)
targets = _kit.all_clients() if shared else [client]
if client and client not in st["touched"]:
    st["touched"].append(client)
if shared and "_shared" not in st["touched"]:
    st["touched"].append("_shared")
_kit.save_session(sid, st)

must, fyi = [], []
for c in targets:
    if shared:   # kit change: only care whether every site still builds
        ok, out = _kit.build(c)
        if not ok:
            must.append(f"[{c}] build failed:\n{out}")
    else:
        m, f = _kit.verify(c)
        must += m
        fyi += f

if must or fyi:
    msg = []
    if must:
        msg.append("FIX BEFORE FINISHING:\n- " + "\n- ".join(must))
    if fyi:
        msg.append("Standards to fix before launch (not blocking yet):\n- " + "\n- ".join(fyi))
    _kit.block(f"Build check after editing {path}:\n" + "\n\n".join(msg))
