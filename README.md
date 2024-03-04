# House-price-prediction-using-flask
In this project, I developed the predictive power of a model trained on house price data. It deploys with flask API and uses Linear Regression to predict the price value. Deploy Machine Learning Model Using Flask to take a model from python code.

If you want to more clear explonation, see my blog [House Price Prediction using Flask for Beginners](https://techyscientists.blogspot.com/2021/07/house-price-prediction-using-flask.html)

## Installation

To run the web app on your local computer, install the required libraries. These packages are include in the requirement.txt file. This project used Python 3.8.0 and Flask 2.0.1.

##### Linux (Ubuntu)
Python 3 is usually installed by default on Ubuntu. If you need to install or upgrade to Python 3.8, run the following commands in the Terminal:


```
sudo apt update
sudo apt install python3.8
```

#### Creating a Virtual Environment
Navigate to the project directory and run the following command to create a virtual environment. Replace venv with your desired environment name.

##### Windows

```
python -m venv venv
```
To activate the virtual environment:
```
.\venv\Scripts\activate
```
```
python3 -m venv venv
```
To activate the virtual environment:
```
source venv/bin/activate
```
 Run the following command in the terminal to install the required packages.

```
pip install -r requirement.txt
```
<br>

## Getting Started

To run code on your computer, following command in terminal<br><br>
```
python app.py
```
<br>

## Preview
<img src='/static/images/form.png'></img>
<br>
<br>
<img src='/static/images/prediction.png'></img>
<br>

## Deployment on EC2
Deploying a Flask app on an `AWS EC2` instance using `Nginx` and `Gunicorn` with systemd involves several steps. 
Below is a comprehensive guide to help you through the process. .

### Step 1: Connect to Your EC2 Instance
- Connect to your EC2 Instance using AWS management Console 

#### OR

- Use SSH to connect to your EC2 instance. You’ll need your instance's public DNS or IP address and your private key file (`.pem` file). The command looks like this:
  ```
  ssh -i /path/to/your-key.pem ubuntu@your-instance-public-dns
  ```
<img src='/img/pic1.png'></img>

### Step 2: Update Your Instance
- Change your user to `root`
```
sudo -i
```
- Update your package lists and upgrade the packages to their latest versions:
  ```
  sudo apt-get update && sudo apt-get upgrade -y
  ```
  <img src='/img/pic2.png'></img>

### Step 3: Install Python, pip, and Virtualenv

- Install Python3, pip (Python package installer), and Virtualenv to create a virtual environment:
  ```
  sudo apt-get install python3-pip python3-dev python3-venv -y

  ```
  <img src='/img/pic3.png'></img>

### Step 4: Clone the Repository

 - Clone the repository using
 ```
 git clone https://github.com/Hassan-Shakoor/Pycon-ML-Model-.git
 ```

  - Create a virtual environment and activate it:
    ```
    python3 -m venv myenv
    source myenv/bin/activate
    ```
  - Install Dependencies:
    ```
    pip install -r requirements.txt
    ```
  <img src='/img/pic4.png'></img>


### Step 5: Test Your Flask App Locally

- Run your Flask app to ensure it works locally:
  ```
  python app.py
  ```
- If your app runs correctly, proceed to the next steps.

  <img src='/img/pic5.png'></img>

### Step 6: Install and Configure Gunicorn

-  While in your virtual environment and app directory, run:
  ```
  gunicorn --workers 3 --bind 0.0.0.0:8000 app:app
  ```
- Replace `app:app` with your Python file name and the Flask app variable name, respectively.

Now go to the web browser and type your public ip address followed by the port number
like this 
```
<IP>:8000
```
it will show your app running

### Step 7: Install and Configure Nginx

- Install Nginx:
  ```
  sudo apt-get install nginx -y
  ```
- Remove the default Nginx configuration:
  ```
  sudo rm /etc/nginx/sites-enabled/default
  ```
- Create a new configuration file for your app in `/etc/nginx/sites-available/` and link it to `sites-enabled`:
  - Use 
  `sudo nano /etc/nginx/sites-available/myapp` 
  to create a file and add the following configuration (adjust the `server_name` to your domain or IP, and the proxy_pass port to match Gunicorn's):
    ```
    server {
        listen 80;
        server_name your-instance-public-dns;

        location / {
            proxy_pass http://unix:/root/Pycon-ML-Model-/myapp.sock;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
    ```
  - Create a symbolic link:
    ```
    sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled
    ```
- Test the Nginx configuration and restart Nginx:
  ```
  sudo nginx -t
  sudo systemctl restart nginx
  ```
  <img src='/img/pic7.png'></img>


### Step 8: Configure Gunicorn to Start on Boot with systemd

- Create a Gunicorn systemd service file:
  ```
  sudo nano /etc/systemd/system/myapp.service
  ```
- Add the following configuration, adjusting paths and names as necessary:
  ```
    [Unit]
    Description=Gunicorn instance to serve myapp
    After=network.target

    [Service]
    User=root
    Group=root
    WorkingDirectory=/root/Pycon-ML-Model-
    Environment="PATH=/root/Pycon-ML-Model-/venv/bin"
    ExecStart=/root/Pycon-ML-Model-/venv/bin/gunicorn --workers 3 --bind unix:myapp.sock -m 007 app:app

    [Install]
    WantedBy=multi-user.target

  ```
- Enable and start the Gunicorn service:
  ```
  sudo systemctl enable myapp
  sudo systemctl start myapp
  ```
- Check the status to ensure it’s running without issues:
  ```
  sudo systemctl status myapp
  ```
  <img src='/img/pic6.png'></img>

### Step 9: Change Nginx User

Change `www-data` to `root` using
```
sudo nano /etc/nginx/nginx.conf
```

<img src='/img/pic8.png'></img>

- Test the Nginx configuration and restart Nginx:
  ```
  sudo nginx -t
  sudo systemctl restart nginx
  ```



### Conclusion

Your Flask app should now be successfully deployed on your EC2 instance, accessible via the public DNS/IP of the instance, served by Gunicorn, and fronted by Nginx. If you opted to secure your app with an SSL certificate, it will also be accessible via HTTPS.

## License
MIT License
<br>
<br>

### Thank you
