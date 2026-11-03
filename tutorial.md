# ℹ️ My LINUX Documentation

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=linux,ubuntu,js,html,css,py,vscode" />
  </a>
</p>


I've bought an Thinkcentre M710S and I installed Ubuntu 24 on it.<br>
There are so many commands thats why I've created this file!


# ℹ️ Linux Commands
| Command  | Usage | Explaination |
|-------|------------|----------------|
| pwd   | `pwd` | Shows where you are   |
| shutdown   | `sudo shutdown -h now ` | Stops the server   |
| clear  | `clear`    | Clears the terminal  |
| mkdir   | `mkdir (path)`    | Creates an directory  |
| touch  | `touch (fileName)`    | Creates an File  |
| nano  | `nano (fileName)`    | Edit an File  |
| rm  | `rm (file/Path)`    | Remove an File/Dir  |
| rmdir  | `rmdir (path)`    | Deletes empty folder  |
| uptime  | `uptime`    | Shows the uptime  |
| hostname  | `hostname`    | shows the Name  |
| whoami  | `whoami`    | Shows who you are  |
| htop  | `htop`    | CPU&RAM Monitor  |
| ps aux  | `ps aux`    | Shows all processes  |
| adduser | `adduser (name)` | Creates an new user  |
| usermod  | `sudo usermod -aG sudo (name)`     | Gives the user admin rights |
| su  | `su -(name)`    | switches to user  |
| cp | cp -r `(pathA) (pathB)` | Copys Files from A to B (Uses -r to copy all the files inside foldes) |
| venv  |  `python3 -m venv (name)`  | Creates a virtual environment  |
| activate | `source (name)/bin/activate` | Activates the virtual environment |
| deactivate | `deactivate` | deactivates the virtual enviroment |


# 🛜 NGINX 
<br>
NGINX is a web server that can host websites
and act as a reverse proxy.

First, create a directory where your website files will be stored:

`sudo mkdir -p /var/www/(name)`

Second, create a configuration file:

`sudo nano /etc/nginx/sites-available/(name)`
<br>
**⚙️Example Configuration:**
```
server {
    listen PORT;
    server_name _;

    root /var/www/WEBSITE_NAME;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

# 🏗️ NGINX Commands
| Command | Usage | Explanation |
|---|---|---|
| install | `sudo apt install nginx` | Installs NGINX |
| start | `sudo systemctl start nginx` | Starts NGINX |
| stop | `sudo systemctl stop nginx` | Stops NGINX |
| restart | `sudo systemctl restart nginx` | Restarts NGINX |
| reload | `sudo systemctl reload nginx` | Reloads configuration |
| status | `sudo systemctl status nginx` | Shows NGINX status |
| enable | `sudo systemctl enable nginx` | Starts NGINX on boot |
| disable | `sudo systemctl disable nginx` | Disables autostart |
| test | `sudo nginx -t` | Tests configuration |
| version | `nginx -v` | Shows NGINX version |
| logs | `sudo tail -f /var/log/nginx/error.log` | Shows error logs |
| access logs | `sudo tail -f /var/log/nginx/access.log` | Shows access logs |

# 🏗️ NGINX Configuration Commands
| Command | Usage | Explanation |
|---|---|---|
| sites | `ls /etc/nginx/sites-available/` | Lists available websites |
| enabled | `ls /etc/nginx/sites-enabled/` | Lists enabled websites |
| create | `sudo nano /etc/nginx/sites-available/(name)` | Creates website config |
| enable | `sudo ln -s /etc/nginx/sites-available/(name) /etc/nginx/sites-enabled/` | Enables website |
| disable | `sudo rm /etc/nginx/sites-enabled/(name)` | Disables website |
| reload | `sudo systemctl reload nginx` | Applies configuration changes |





# <img src="https://skillicons.dev/icons?i=py"/> Python
I've created an Backend with **Python** and I ran into an issue.<br>
I had to start the Python-File after an reboot but now it is automated! <br>
And here is how <br>
# 🏎️ Autostart of Files
| Command | Usage | Explanation |
|---|---|---|
| create | `sudo nano /etc/systemd/system/(name).service` | Creates a systemd service file |
| daemon-reload | `sudo systemctl daemon-reload` | Reloads systemd configuration files |
| enable | `sudo systemctl enable (name)` | Enables autostart on boot |
| disable | `sudo systemctl disable (name)` | Disables autostart |
| start | `sudo systemctl start (name)` | Starts the service |
| stop | `sudo systemctl stop (name)` | Stops the service |
| restart | `sudo systemctl restart (name)` | Restarts the service |
| status | `sudo systemctl status (name)` | Shows the service status |
| logs | `sudo journalctl -u (name)` | Shows service logs |
