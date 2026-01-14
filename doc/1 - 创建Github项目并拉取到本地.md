
## 一、你要实现的目标（先建立正确认知）

你想要的是：

> **本地写代码 → 保存一次关键修改 → 同步到 GitHub → 任何地方都能看到最新版本**

这在 Git/GitHub 中对应的是一条非常清晰的流程：

```
工作区(写代码)
   ↓
暂存区 (git add)
   ↓
本地仓库 (git commit)
   ↓
远程仓库 GitHub (git push)
```

记住一句话就够了：

> **Git 负责“版本管理”，GitHub 负责“远程备份 + 协作”**


## 二、一次性准备工作（只做一次）

### 1️⃣ 注册 GitHub 账号

👉 [https://github.com](https://github.com/)  
（这个你应该已经有了）


### 2️⃣ 在 GitHub 上新建一个仓库（Repository）

- 点击右上角 `+` → `New repository`
- 填：
    - Repository name：`my-project`（随便）
    - Public / Private：新手随意（推荐 Public）
    - ❌ 不要勾选 README（新手更清晰）

创建完成后，**页面先别关**


### 3️⃣ 本地配置 Git（只做一次）

打开 **Git Bash**：

```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub注册邮箱"
```

检查是否成功：

```bash
git config --list
```



## 三、核心实战流程（你以后每天都用的）

下面是**你以后 90% 时间都会重复的流程**。


### 场景：你本地有一个项目目录

假设你的代码在：

```
D:\projects\demo
```

### 1️⃣ 进入项目目录

```bash
cd /d/projects/demo
```



### 2️⃣ 初始化 Git 仓库（只做一次）

```bash
git init
```

你会看到：

```
Initialized empty Git repository...
```

这一步相当于告诉 Git：

> “这个文件夹以后要被版本管理”



### 3️⃣ 关联 GitHub 远程仓库（只做一次）

在 GitHub 页面中，复制仓库地址（HTTPS）：

```text
https://github.com/你的用户名/my-project.git
```

在 Git Bash 中执行：

```bash
git branch -M main
git remote add origin https://github.com/你的用户名/my-project.git
```

验证：

```bash
git remote -v
```


## 四、【重点】日常更新代码的标准流程
每次你改完代码，只做这 3 步

### ✅ 第一步：查看改了什么（非常重要）

```bash
git status
```

你会看到哪些文件被修改、新增、删除。


### ✅ 第二步：加入暂存区

```bash
git add .
```

含义是：

> “这次改动，我准备作为一个版本提交”

（新手阶段直接用 `.` 就好）



### ✅ 第三步：提交本地版本

```bash
git commit -m "简要说明这次做了什么"
```

示例：

```bash
git commit -m "新增数据预处理模块"
```

> ❗ **commit 信息是给未来的你看的，一定要写清楚**



### ✅ 第四步：推送到 GitHub（同步）

优先选这个：
```bash
git push -u origin main
```

⚠️ 如果你的默认分支是 `master`，用：

```bash
git push -u origin master
```

👉 第一次推送会让你登录 GitHub（浏览器弹窗）



## 五、以后你每天只需要记住这一套

> **改代码 → add → commit → push**

```bash
git status
git add .
git commit -m "xxx"
git push
```



## 六、在别的电脑上怎么办？

非常简单：

```bash
git clone https://github.com/你的用户名/my-project.git
```

然后：

```bash
cd my-project
```

你就拿到了**最新完整版本**。



## 七、新手最容易犯的 5 个错误（提前帮你避坑）

### ❌ 1. 不 commit 就 push（不可能成功）

👉 **push 之前一定要 commit**


### ❌ 2. 每改一行就 commit

👉 一个 commit = 一个**有意义的阶段**


### ❌ 3. commit 信息写 “update / test”

👉 以后你会恨自己  
正确示例：

- `修复数据读取路径错误`
- `重构模型训练流程`


### ❌ 4. 把 `.idea`、`venv`、`__pycache__` 提交了

👉 下一步你应该学 `.gitignore`（我可以单独教你）


### ❌ 5. 把 Git 当网盘

👉 Git 不是用来存大文件（视频、模型权重）


## 八、我建议你的学习路线（非常适合你）

你现在适合按这个顺序来：

1️⃣ **单人使用 Git（你现在这个阶段）**  
2️⃣ `.gitignore`  
3️⃣ `git log / git diff`  
4️⃣ 分支（branch）  
5️⃣ 多设备协作 & 回滚版本  
6️⃣ GitHub + 项目规范（README、Issues）
