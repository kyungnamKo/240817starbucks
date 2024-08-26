<h1>Apache Airflow 설치</h1>

<h2>1. Docker 설치</h2>
- 운영 체제 : Rocky-Linux-8

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
<pre><code>docker compose up airflow-init</code></pre>

### Airflow 실행
<pre><code>docker compose up</code></pre>