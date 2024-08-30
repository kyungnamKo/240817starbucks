## 설치 환경
Google cloud Compute enegine
Kubernetes 기반 Airflow 설치

### Network
VPC : vpc-airflow-hugo
Subnet : sbn-airflow-hugo (10.0.2.0/24, asia-northeast3)

### Compute Engine
playground-hugo-20240408 (4core / 16GB MEM / 50GB Disk (HDD))
gcloud compute instances create vm-an3-airflow-hugo \
    --project=playground-hugo-20240408 \
    --zone=asia-northeast3-a \
    --machine-type=n1-standard-4 \
    --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=sbn-airflow-hugo \
    --create-disk=auto-delete=yes,boot=yes,device-name=vm-an3-airflow-hugo,image=projects/rocky-linux-cloud/global/images/rocky-linux-9-optimized-gcp-v20240815,mode=rw,size=50,type=pd-balanced

### air flow install
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube


minikube version

minikube start --vm-driver=none

curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

#### 참고 사이트
https://zerohertz.github.io/k8s-airflow/
https://velog.io/@jskim/Airflow-On-K8s-Kubernetes-Airflow-Cluster-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0
