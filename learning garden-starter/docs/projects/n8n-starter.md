# n8n 工作流基本知识及操作方法

 ## 本地部署 n8n 工作流
- 资料和数据保护
- 客制化
- 工作流深度嵌入系统内部

## 节点分类
- 触发型节点
- 资料传输节点
- 命令执行节点
- 逻辑节点

## 工作流搭建
- 首先需要一个触发节点 ( add trigger )
  1. 手动触发：when clicking 'Test workflow'
  2. on app event: 非常多选择
  3. 时间触发 ( on a schedule ) : 设置触发的时间
  4. webhook : runs the flow on reciving an HTTP request
  5. on form submission :  generate webforms in n8n and pass their respones to the workflow ( 填写体质表格 + 基础病史之后参与智能体输出 )
  6. when executed by another workflow ( 由别的工作流来呼叫本工作流 )
  7. on chat message
