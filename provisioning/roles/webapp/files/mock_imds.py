# from flask import Flask, jsonify, Response
# app=Flask(__name__); ROLE="image-resizer-role"
# @app.get("/latest/meta-data/instance-id")
# def iid(): return Response("i-0abc123def456\n",mimetype="text/plain")
# @app.get("/latest/meta-data/iam/security-credentials/")
# def rn(): return Response(ROLE+"\n",mimetype="text/plain")
# @app.get("/latest/meta-data/iam/security-credentials/<role>")
# def creds(role):
#     if role!=ROLE: return Response("Not found\n",404)
#     return jsonify(Code="Success",Type="AWS-HMAC",AccessKeyId="AKIA1MDSL34K3D01",SecretAccessKey="IMDSSecretKeyForLabOnly123456789",Token="LAB-TEMPORARY-TOKEN",Expiration="2099-12-31T23:59:59Z")
# if __name__=="__main__": app.run(host="169.254.169.254",port=80,use_reloader=False)

from flask import Flask, jsonify, Response

app = Flask(__name__)

ROLE = "image-resizer-role"


def text_response(value: str, status: int = 200) -> Response:
    """Trả kết quả dạng text giống AWS IMDS."""
    return Response(
        value.rstrip("\n") + "\n",
        status=status,
        mimetype="text/plain",
    )


# Có thể bắt đầu khám phá từ /latest/
@app.get("/latest/", strict_slashes=False)
def latest_index():
    return text_response("meta-data/")


# Liệt kê các mục ở tầng metadata
@app.get("/latest/meta-data/", strict_slashes=False)
def metadata_index():
    return text_response(
        "instance-id\n"
        "iam/"
    )


# Trả về instance ID
@app.get("/latest/meta-data/instance-id")
def instance_id():
    return text_response("i-0abc123def456")


# Liệt kê nội dung trong nhánh IAM
@app.get("/latest/meta-data/iam/", strict_slashes=False)
def iam_index():
    return text_response("security-credentials/")


# Trả về tên IAM Role
@app.get(
    "/latest/meta-data/iam/security-credentials/",
    strict_slashes=False,
)
def role_name():
    return text_response(ROLE)


# Trả về credential của IAM Role
@app.get("/latest/meta-data/iam/security-credentials/<role>")
def credentials(role: str):
    if role != ROLE:
        return text_response("Not found", status=404)

    return jsonify(
        Code="Success",
        Type="AWS-HMAC",
        AccessKeyId="AKIA1MDSL34K3D01",
        SecretAccessKey="IMDSSecretKeyForLabOnly123456789",
        Token="LAB-TEMPORARY-TOKEN",
        Expiration="2099-12-31T23:59:59Z",
    )


if __name__ == "__main__":
    app.run(
        host="169.254.169.254",
        port=80,
        use_reloader=False,
    )