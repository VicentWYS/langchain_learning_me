"""
LangChain 1.0 基础教程 - 第一个 LLM 调用
==============================================

本文件演示使用LangChain 1.0 进行基本的 LLM 调用
涵盖以下核心概念：
1. init_chat_model - 初始化聊天模型
2. invoke - 同步调用模型
3. Messages - 消息类型（System, Human, AI）
4. 基本配置和参数

作者：snape
日期：2026-01-14
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# 加载环境变量
# 1. 查找 .env 文件，将其中的内容加载到 os.environ
# 2. 从环境变量中读取密钥，若不存在，则返回None
load_dotenv()
QWEN_API_KEY = os.getenv("QWEN_API_KEY")
QWEN_BASE_URL = os.getenv("QWEN_BASE_URL")


# 校验 QWEN_API_KEY 是否被正确配置
# 1. 防止 .env 未加载导致为 None
# 2. 防止开发者未替换模板中的占位符
# 3. 提前中断程序，避免模型初始化阶段出现难以定位的鉴权错误
if not QWEN_API_KEY or QWEN_API_KEY == "your_qwen_api_key_here":
    raise ValueError(
        "\n请先在 .env 文件中设置有效的 QWEN_API_KEY\n"
        "访问 https://bailian.console.aliyun.com/cn-beijing/?tab=model#/api-key 获取免费秘钥"
    )

if not QWEN_BASE_URL or QWEN_BASE_URL == "your_qwen_base_url_here":
    raise ValueError(
        "\n请先在 .env 文件中设置有效的 QWEN_BASE_URL\n"
        "访问 https://bailian.console.aliyun.com/cn-beijing/?tab=model#/model-market/detail/qwen-plus 获取适配 OpenAI 的 url"
    )


# 初始化模型
# init_chat_model 是langchain 1.0 提供的标准跨厂商统一模型入口工厂函数，是所有模型统一入口
# LangChain 会自动帮你选择对应厂商的 ChatModel 类，并完成实例化
# Qwen 不是 OpenAI 协议直连，需要走 OpenAI-compatible endpoint，这一步很多人会踩坑
# LangChain 1.x 不再关心“你是什么模型”，只关心协议。Qwen 是 OpenAI 协议伪装模型
model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=QWEN_API_KEY,
    base_url=QWEN_BASE_URL,
    temperature=0.8,
)


# ===================================================================================
# 示例1：最简单的 LLM 调用
# ===================================================================================
def example_1_simple_invoke():
    """
    示例1：最简单的模型调用

    核心概念：
    - init_chat_model: 用于初始化聊天模型的统一接口
    - invoke: 同步调用模型的方法
    """
    print("\n" + "=" * 40)
    print("示例1：最简单的模型调用")
    print("=" * 40)

    # 初始化模型
    # 格式：init_chat_model(...)
    # 这里就使用上面初始化的那个 model

    # 使用字符串直接调用模型
    response = model.invoke("你好！请用一句话介绍什么是人工智能")

    print(f"用户输入：你好！请用一句话介绍什么是人工智能")
    print(f"AI 回答：{response.content}")
    print(f"\n返回对象类型：{type(response)}")
    print(f"返回对象：{response}")


# ===================================================================================
# 示例2：使用消息列表进行对话
# ===================================================================================
def example_2_messages():
    """
    示例2：使用消息列表

    核心概念：
    - SystemMessage: 系统消息，用于设定 AI 的角色和行为
    - HumanMessage: 用户消息
    - AIMessage: AI 的回复消息

    消息列表允许你构建多轮对话历史
    """
    print("\n" + "=" * 40)
    print("示例2：使用消息列表进行对话")
    print("=" * 40)

    # 模型已经在开头初始化

    # 构建消息列表
    messages = [
        SystemMessage(
            content="你是一个友好的 Python 编程助手，擅长用简单易懂的方式解释编程概念。 回答字数不超过100字。"
        ),
        HumanMessage(content="什么是 Python 装饰器？"),
    ]

    print("系统提示词：", messages[0].content)
    print("用户提示词：", messages[1].content)

    # 调用模型
    response = model.invoke(messages)

    print(f"\nAI 回复：\n{response.content}")

    # 继续对话：将 AI 的回复添加到对话历史
    messages.append(response)
    messages.append(HumanMessage(content="请给出一个具体示例"))

    print("\n" + "=" * 40)
    print("继续对话...")
    print("用户问题：", messages[-1].content)

    response2 = model.invoke(messages)
    print(f"\nAI 回复：\n{response2.content}")


def main():
    """
    主程序：运行所有实例
    """
    print("\n" + "=" * 80)
    print(" LangChain 1.0 基础教程 - 第一个 LLM 调用")
    print("=" * 80)

    try:
        # 运行所有示例
        example_1_simple_invoke()
        example_2_messages()

        print("\n" + "=" * 80)
        print("所有示例运行完成！")
        print("=" * 80)

    except Exception as e:
        print(f"\n运行出错：{e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
