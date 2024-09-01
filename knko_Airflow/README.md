<h1>Apache Airflow 설치</h1>

<h2>1. Docker 설치</h2>

- 환경 : Google Cloud Platform
- 머신 타입 : n1-standard-4 (Disk : 50GB)
- 운영 체제 : Rocky-Linux-9

### docker 리포지토리 추가
<pre><code>sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo</code></pre>

### 필요한 패키지 설치
<pre><code>sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin</code></pre>

### systemd docker 서비스(dockerd) 시작 및 활성화
<pre><code>sudo systemctl --now enable docker</code></pre>

<h2>2. Airflow 설치</h2>

### docker-compose.yaml 가져오기
<pre><code>curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.0/docker-compose.yaml'</code></pre>

### 환경 설정
<pre><code>mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env</code></pre>

### Airflow 설치
<pre><code>sudo docker compose up airflow-init</code></pre>

### Airflow 실행
<pre><code>sudo docker compose up</code></pre>

### Airflow 컨테이너 확인 (새로운 터미널에서 실행)
<pre><code>sudo docker ps</code></pre>

### Airflow Webserver 접근
<pre><code># 방화벽 open 후 접근 가능
http://localhost:8080
ID : airflow
PW : airflow</code></pre>

<h2>3. 참고자료</h2>

1. https://docs.rockylinux.org/ko/gemstones/containers/docker/

2. https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
