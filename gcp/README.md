# How GCP is setup? 
1. It was launched bare Linux Ubuntu VM
2. Installed **conda** and added to HOME path **conda**
```bash
# Setup Ubuntu
sudo apt update --yes
sudo apt upgrade --yes

# Get Miniconda and make it the main Python interpreter
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda 
rm ~/miniconda.sh

export PATH=~/miniconda/bin:$PATH
```    

3. Installed Docker
```bash
sudo apt install docker.io

# The Docker service needs to be setup to run at startup. To do so, type in each command followed by enter:
sudo systemctl start docker
sudo systemctl enable docker

``` 
