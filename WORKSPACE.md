# 进度
1. test跑通
2. real coding agent w/ gpt-4o
poetry run pytest ./tests/unit/test_sandbox.py

问题不大
集成llm
同时看在哪里



也就是说，每新建一个agent，都要维护一个conversation_id。——重构。
可以重构。

直接用gpt-4会面临网络问题。

答案：先解决网络问题，初步测试。【1天】
然后用conversation_id重构【2-3天】。

再看一下架构。


# 方案
Multi-agent架构
方案：
1. 全部监视：全局输出（包括framework）
2. 局部监视：每个agent的输入输出
