
## 基本认识
- Git 的核心根本不是 commit，而是 branch。
- 真正的工程化 Git，用的是：**分支来管理“不同的工作状态”**，而不是用 commit 记录代码。
- main 分支 = 永远可运行、可交付、可演示的版本，main 是：  **“成果展示区”**。你真正写代码的地方是：feature 分支。

### 整体工作流
企业通用工作流：

```
main（稳定）
   ↑
merge
   ↑
feature/xxx（开发）
```

### 工程化 Git 工作流
1. 从 main 拉一个分支；
2. 在分支上写代码；
3. 写完测试没问题；
4. 合并回 main；
5. 删除分支。

在真实开发中，一次功能开发，完整流程是：

```bash
① 从 main 拉分支
② 在分支上反复 add / commit
③ push 分支到 GitHub（备份 + 协作）
④ 功能完成
⑤ 合并回 main
⑥ 删除分支
```

逻辑流程：

```bash
main（稳定）
   ↑
merge
   ↑
feature/xxx（开发区）
   ├── add
   ├── commit
   ├── commit
   ├── commit
   └── push
```

你会发现：add / commit / push 只是**分支里的日常操作**，而不是全部。

**add / commit / push 是“写代码的动作”**  
**branch / merge 是“做工程的动作”**

### 不同指令的功能

| 命令                | 在工程里的角色    | 发生在什么时候 |
| ----------------- | ---------- | ------- |
| branch / checkout | 切换“工作空间”   | 开始一个新任务 |
| add               | 选择本次要记录的修改 | 每次小改动   |
| commit            | 记录一个开发步骤   | 频繁发生    |
| push              | 把分支进度备份到远程 | 阶段性发生   |
| merge             | 把成果合并回主干   | 功能完成时   |


## 分支操作
### 定位到当前分支
假设我们需要在当前 `main` 分支上新开一个分支；

### 创建一个分支
- 新建一个分支；

```bash
git checkout -b feature/langchain-prompt-template
```

- 在这一分支上进行代码的修改：`add` 、`commit` 、`push` 等；

### 合并到原分支
- 合并，处理冲突；

```bash
git checkout main
git merge feature/langchain-prompt-template
```

### 删除分支

```bash
git branch -d feature/langchain-prompt-template
```

删除后，留下的只有：一条非常干净、清晰、像教材一样的 main 提交历史。
