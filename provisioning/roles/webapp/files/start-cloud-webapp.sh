#!/bin/bash
set -euo pipefail
ip address add 169.254.169.254/32 dev lo 2>/dev/null || true
docker rm -f image-resizer mock-imds 2>/dev/null || true
docker run -d --name mock-imds --restart unless-stopped --network host cloud-lab/mock-imds:1.0
docker run -d --name image-resizer --restart unless-stopped --network host cloud-lab/image-resizer:1.0
