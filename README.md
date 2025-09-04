# 本地已有项目
cd /你的项目
git init
git add .
git commit -m "init"
git branch -M main
git remote add origin git@github.com:<你>/<仓库>.git  # 或 https://...
git push -u origin main
