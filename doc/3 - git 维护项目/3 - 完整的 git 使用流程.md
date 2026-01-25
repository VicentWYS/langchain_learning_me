
太好了。你现在要的不是“会几条命令”，而是**一条完整、可反复执行的 Git 工程闭环**。

下面这套流程，是**公司真实日常**，你以后每做一个功能，都可以机械地按这个来。

> 场景：你要开发一个新功能  
> 例子：`PromptTemplate 示例模块`



# 全流程总览（先有地图）

```
① 同步 main
② 从 main 拉 feature 分支
③ 在分支上开发（add / commit）
④ push 分支到远程
⑤ 在 GitHub 开 PR
⑥ Review 通过 → 合并到 main
⑦ 本地同步 main
⑧ 删除本地分支
⑨ 删除远程分支
⑩ 清理远程分支缓存
```

这 10 步 = 一个完整 Git 闭环。

## 1. 切到 main，并拉最新代码（起点）

```bash
git checkout main
git pull origin main
```

**目的：**  
保证你是从团队最新稳定代码开始。

## 2. 从 main 创建功能分支（真正开始工作）

分支命名规范：

```bash
git checkout -b feature/langchain-prompt-template
```

从现在开始：

> ❗你再也不在 main 上写代码

## 3. 在分支上开发（你熟悉的操作开始登场）

写代码 → 多次提交：

```bash
git add .
git commit -m "feat: add basic PromptTemplate example"

git add .
git commit -m "feat: add partial variables example"

git add .
git commit -m "feat: add error handling"
```

这些 commit **全在 feature 分支**。

## 4. 阶段性 push 到远程（非常关键的工程习惯）

```bash
git push -u origin feature/langchain-prompt-template
```

作用：

- 云端备份
- 为 PR 做准备
- 让远程出现这个分支

## 5. 去 GitHub 开 PR（核心步骤）

在 GitHub：

> Compare & Pull Request

选择：

```
base: main
compare: feature/langchain-prompt-template
```

写清楚 PR 说明，然后：

> Create Pull Request

## 6. PR 审查通过 → 点击 Merge

此时发生的事：

> GitHub 帮你把 feature 分支合并进 main（远程）

注意：**你本地 main 还没更新！**

## 7. 回到本地，同步远程 main（很多人忘这步）

```bash
git checkout main
git pull origin main
```

现在你本地 main 才拥有刚才的成果。

## 8. 删除本地 feature 分支（保持本地干净）

```bash
git branch -d feature/langchain-prompt-template
```

## 9. 删除远程 feature 分支（保持远程干净）

```bash
git push origin --delete feature/langchain-prompt-template
```

这是**非常标准的公司操作**。

## 10. 清理本地对远程分支的缓存（VSCode 会立刻干净）

```bash
git fetch -p
```


# ✅ 此时仓库回到“初始干净态”

```
本地：
  main

远程：
  main
```

像什么都没发生过，但历史全部保留。


# 🧠 这个流程背后的工程思想

|     阶段     | 本质       |
| :--------: | :-------: |
|    main    | 永远稳定、可交付 |
| feature 分支 | 实验区、开发区  |
|    push    | 备份 + 协作  |
|     PR     | 审查机制     |
|   merge    | 成果入库     |
|    删除分支    | 保持仓库整洁   |


# 🪄 以后你每学一个 LangChain 知识点，都完整走一遍这 10 步

3 周后，你对 Git 的熟练度会超过绝大多数工作 3 年的程序员。


# 🧾 最后给你一份“肌肉记忆清单”

每次开发新功能，直接照抄：

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

这就是**完整、标准、公司级 Git 使用闭环**。