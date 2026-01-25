
### 安装依赖
- 在 `requirements.txt` 中预先设置版本：`langchain-openai>=0.2.0`
- 终端中输入指令进行安装：

```bash
pip install langchain-openai
```


### .env 配置百炼平台
- `.env` 中添加：

```
QWEN_API_KEY=你的key
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

> 注意：不是 bailian.console 的域名  
> 是 **compatible-mode** 这个地址（这是关键）


### LangChain 1.x 中正确引入该模型

```python fold
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


# 加载环境变量
# 1. 查找 .env 文件，将其中的内容加载到 os.environ
# 2. 从环境变量中读取密钥，若不存在，则返回None
load_dotenv()
QWEN_API_KEY = os.getenv("QWEN_API_KEY")
QWEN_BASE_URL=os.getenv("QWEN_BASE_URL")


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
    temperature=0.8
)


# 测试
resp = model.invoke("介绍一下你自己")
print(resp.content)
```
