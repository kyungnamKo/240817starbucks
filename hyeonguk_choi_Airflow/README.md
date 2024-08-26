## 설치 환경
Google cloud Compute enegine
Kubernetes 기반 Airflow 설치

### Network
VPC : vpc-airflow-hugo
Subnet : sbn-airflow-hugo (10.0.2.0/24, asia-northeast3)

## Compute Engine
playground-hugo-20240408 (4core / 16GB MEM / 50GB Disk (HDD))
gcloud compute instances create vm-an3-airflow-hugo \
    --project=playground-hugo-20240408 \
    --zone=asia-northeast3-a \
    --machine-type=n1-standard-4 \
    --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=sbn-airflow-hugo \
    --create-disk=auto-delete=yes,boot=yes,device-name=vm-an3-airflow-hugo,image=projects/rocky-linux-cloud/global/images/rocky-linux-9-optimized-gcp-v20240815,mode=rw,size=50,type=pd-balanced


