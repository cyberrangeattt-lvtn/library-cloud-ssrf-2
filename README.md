# Cloud SSRF & Container Escape

A linear CyberRangeCZ lab implementing the chain:

`SSRF → mock IMDSv1 → IAM credential → MinIO backup → SSH key → docker.sock → host root`

| Host | Image | Flavor |
|---|---:|---|
| attacker | kali | standard.kali |
| webapp-vm | debian-12-x86_64 | standard.small |
| docker-host | debian-12-x86_64 | standard.small |
| minio-storage | debian-12-x86_64 | standard.small |
| router | debian-12-x86_64 | standard.small |

Trainee account: `user` / `Password123`.

Quá trình triển khai yêu cầu quyền truy cập Internet chiều ra để tải xuống các image container và tệp nhị phân MinIO/Docker. Chỉ sử dụng trong môi trường mô phỏng an ninh mạng (cyber range) cô lập.
