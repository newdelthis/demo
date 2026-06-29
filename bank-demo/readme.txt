GitHub repo: github.com/newdelthis/demo/bank-demo

Linux machine
=============
1. Install Docker
2. Install Java 21
sudo apt update
sudo apt install openjdk-21-jdk
3. Install Maven
Open Firefox browser: https://maven.apache.org/download.cgi
Download file https://dlcdn.apache.org/maven/maven-3/3.9.16/binaries/apache-maven-3.9.16-bin.tar.gz
4. Terminal
cd ~/Downloads
sudo mv apache-maven-3.9.16 /opt/
nano ~/.bashrc
Add these at the end:
export MAVEN_HOME=/opt/apache-maven-3.9.16
export PATH=$MAVEN_HOME/bin:$PATH
Save the file and exit nano
source ~/.bashrc
Check maven version: mvn -version
5. Now copy under ~/Downloads directory, the bank-demo directory of GitHub
6. In the terminal: cd ~/Downloads/bank-demo
7. mvn clean package
8. docker build -t bank-demo .
9. docker run -d -p 2222:8080 --name bank-container bank-demo
10. curl http://localhost:2222/accounts
Output should be []
11. Now use Postman to try these:
POST   http://localhost:2222/accounts
GET    http://localhost:2222/accounts
GET    http://localhost:2222/accounts/1
POST   http://localhost:2222/accounts/1/deposit?amount=1000
POST   http://localhost:2222/accounts/1/withdraw?amount=500
DELETE http://localhost:2222/accounts/1
