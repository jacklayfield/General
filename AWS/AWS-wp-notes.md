## Simple AWS EC2 instance hosting Wordpress, MySQL and Apache 2

visit: http://18.218.83.139/ to view sample site

### To set up:

#### Create an EC2 instance

- Ubuntu
- Create key pair and store locally
- Make sure to allow http / https traffic
- (Default storage)

#### Assign Elastic IP Address

- Do this to make ipv4 static (So TNS sever can know)
- Create Elastic IP Address and asign to your instance

#### Connect to EC2 via SSH client

- On Windows, use something like MobaXTerm
- New session, enter IP, username, key

#### Getting everything set up in SSH client

- Get Apache web server by installing via: sudo apt install apache2
- Install php runtime and php my sql to work with Apache server:
  sudo apt install php libapache2-mod-php php-mysql
- Install and setup MySQL:
  - Install: sudo apt install mysql-server
  - Login: sudo mysql -u root
  - Change password: ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password by 'PUTPASSWORDHERE';
  - Create new user: CREATE USER 'wp_user'@localhost IDENTIFIED BY 'PUTPASSWORDHERE';
  - Create DB: CREATE DATABASE wp;
  - Grant perms: GRANT ALL PRIVILEGES ON wp.\* TO 'wp_user'@localhost;
- Download wordpress in /tmp (use wget)
  - Unzip in tmp
  - Move to /var/www/html: sudo mv wordpress/ /var/www/html
  - Restart Apache: sudo systemctl restart apache2
- Extra - Connect domain and install certbot in order to provide certs for https
