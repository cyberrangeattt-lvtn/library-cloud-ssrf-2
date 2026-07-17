from flask import Flask, jsonify, Response
app=Flask(__name__); ROLE="image-resizer-role"
@app.get("/latest/meta-data/instance-id")
def iid(): return Response("i-0abc123def456\n",mimetype="text/plain")
@app.get("/latest/meta-data/iam/security-credentials/")
def rn(): return Response(ROLE+"\n",mimetype="text/plain")
@app.get("/latest/meta-data/iam/security-credentials/<role>")
def creds(role):
    if role!=ROLE: return Response("Not found\n",404)
    return jsonify(Code="Success",Type="AWS-HMAC",AccessKeyId="AKIA1MDSL34K3D01",SecretAccessKey="IMDSSecretKeyForLabOnly123456789",Token="LAB-TEMPORARY-TOKEN",Expiration="2099-12-31T23:59:59Z")
if __name__=="__main__": app.run(host="169.254.169.254",port=80,use_reloader=False)
