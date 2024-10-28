git add .
git commit -m "%*"
git push
ssh claudia@34.65.22.12 "cd /home/claudia_daneder/projects/videoflix_backend/ && sudo git pull"