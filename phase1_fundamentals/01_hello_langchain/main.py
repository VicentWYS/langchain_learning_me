"""
phase1_fundamentals.01_hello_langchain.main 的 Docstring

本文件演示使用LangChain 1.0 进行基本的 LLM 调用
涵盖以下核心概念：
1. init_chat_model - 初始化聊天模型
2. invoke - 同步调用模型
3. Messages - 消息类型（System, Human, AI）
4. 基本配置和参数

作者：武宇盛
日期：2026-01-14
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 加载环境变量
load_dotenv() # 查找 .env 文件，将其中的内容加载到 os.environ
QWEN_API_KEY=os.getenv("QWEN_API_KEY")

if not QWEN_API_KEY or QWEN_API_KEY == "your_qwen_api_key_here":
    raise ValueError(
        "\n请先在 .env 文件中设置有效的 QWEN_API_KEY\n"
        "访问 https://bailian.console.aliyun.com/cn-beijing/?tab=model#/api-key 获取免费秘钥"
    )

