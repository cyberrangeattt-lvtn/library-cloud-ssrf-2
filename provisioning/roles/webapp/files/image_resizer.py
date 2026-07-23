from flask import Flask, request, Response, render_template_string
import threading, requests
from urllib.parse import urlsplit
app=Flask(__name__); admin=Flask("admin")
PAGE="""<!doctype html><title>ImageResizer</title><h1>ImageResizer - Upload from URL</h1><form method=post action=/fetch><input name=url style='width:600px'><button>Fetch</button></form>"""
@app.get("/")
def index(): return render_template_string(PAGE)
@app.post("/fetch")
def fetch():
    target=request.form.get("url","").strip()
    if not target: return Response("Missing URL\n",400)
    if (urlsplit(target).hostname or "").lower()=="169.254.169.254": return Response("Blocked metadata address\n",403)
    s=requests.Session(); s.trust_env=False
    try: r=s.get(target,timeout=5,allow_redirects=False)
    except Exception as e: return Response(f"Fetch failed: {e}\n",502)
    out=Response(r.content,r.status_code)
    for h in ("Content-Type","X-Admin-Panel"):
        if h in r.headers: out.headers[h]=r.headers[h]
    out.headers["X-Fetched-URL"]=target
    return out
@admin.get("/admin")
def ap():
    r=Response("ImageResizer administration panel\n"); r.headers["X-Admin-Panel"]="FLAG{5SRF_c0nf1rm3d}"; return r
if __name__=="__main__":
    threading.Thread(target=lambda: admin.run(host="127.0.0.1",port=8080,use_reloader=False),daemon=True).start()
    app.run(host="0.0.0.0",port=5000,use_reloader=False)
