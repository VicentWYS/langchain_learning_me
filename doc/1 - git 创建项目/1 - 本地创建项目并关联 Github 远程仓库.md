
## 第一次创建项目
### 在 GitHub 上新建一个仓库（Repository）
- 注意不要勾选 README；

### 本地配置 Git（只做一次）
- 在电脑本地，安装Git Bash；
- 在Git Bash中设置用户名和邮箱：

```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub注册邮箱"
```

- 检查是否成功：`git config --list`

### 本地创建项目目录
- 进入本地项目目录；
- 使用vscode打开该项目，打开终端；
- 初始化：`git init`, 这一步相当于告诉 Git: “这个文件夹以后要被版本管理”;

### 关联 GitHub 远程仓库（只做一次）
- 在 GitHub 页面中，复制仓库地址（HTTPS）：`https://github.com/你的用户名/my-project.git`
- 在本地项目中，vscode终端中执行：

```bash
git branch -M main
git remote add origin https://github.com/你的用户名/my-project.git
```

- 验证：`git remote -v`

## 日常操作
- 看到哪些文件被修改、新增、删除：`git status`
- 将改动加入暂存区：`git add .`
- 提交本地版本：`git commit -m "简要说明这次做了什么"`
- 推送到Github: `git push -u origin main`

## 在别的电脑上拉取项目
- 克隆仓库，即可获得最新完整版本：`git clone https://github.com/你的用户名/my-project.git`
- 本地进入目录：`cd my-project`

## 注意事项
- push 之前一定要 commit；
- 一个 commit = 一个有意义的阶段；
- 注意，不要把 `.idea`、`venv`、`__pycache__` 提交了（设置 `.gitignore`）；
- Git不适合存储大文件。
