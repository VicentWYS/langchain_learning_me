
```bash
git checkout main
git pull origin main
git checkout -b feature/xxx

# 开发中反复
git add .
git commit -m "feat: xxx"

git push -u origin feature/xxx
# 去 GitHub 开 PR 并 Merge

git checkout main
git pull origin main
git branch -d feature/xxx
git push origin --delete feature/xxx
git fetch -p
```

![git 项目管理流程](../pics/git%20项目管理流程.png)


