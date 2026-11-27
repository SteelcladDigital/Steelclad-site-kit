"""Stop: no "done" on a site until it builds and passes the standards check.

Runs only when this session edited a client or kit code. Blocks finishing (exit 2) while a touched
site fails to build or a launched site has hard issues. Gives up after 3 tries so it can't loop forever,
and then tells the user what is still wrong.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _kit

MAX_BLOCKS = 3
data = _kit.read_input()
sid = data.get("session_id")
st = _kit.session_state(sid)
if not st["touched"]:
    sys.exit(0)

clients = [c for c in st["touched"] if c != "_shared"]
if "_shared" in st["touched"]:
    clients = _kit.all_clients(False)
clients = [c for c in clients if os.path.exists(os.path.join(_kit.ROOT, "clients", c, "site.py"))]

must, fyi = [], []
for c in clients:
    m, f = _kit.verify(c)
    must += m
    fyi += f

if must and st.get("stop_blocks", 0) < MAX_BLOCKS:
    st["stop_blocks"] = st.get("stop_blocks", 0) + 1
    _kit.save_session(sid, st)
    _kit.block("Not done yet. Fix these, then confirm the build passes:\n- " + "\n- ".join(must))

st["stop_blocks"] = 0
_kit.save_session(sid, st)
notes = []
if must:
    notes.append("Still failing after 3 attempts, needs a person:\n- " + "\n- ".join(must))
if fyi:
    notes.append("Before launch:\n- " + "\n- ".join(fyi))
if notes:
    print(json.dumps({"systemMessage": "Site Kit check\n" + "\n".join(notes)}))
sys.exit(0)
