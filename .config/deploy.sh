# 그환경에 있는  bash를 사용해라
#!/usr/bin/env bash
sudo rm -rf /ect/nginx/sites-enabled/*
sudo cp -f /srv/ec2-deploy/.config/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
sudo ln -sf /ect/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx.conf
sudo cp -f /srv/ec2-deploy/.config/uwsgi.service /etc/systemd/system/uwsgi.service
sudo systemctl enable uwsgi
sudo systemctl daemon-reload
sudo systemctl restart uwsgi nginx