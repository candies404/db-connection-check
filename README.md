# 数据库连接检查 Action

这个 GitHub Action 用于检查数据库连接并返回连接是否成功的结果。它支持通过提供的数据库 URI 来测试连接。

## 功能

- 支持通过 URI 连接到数据库
- 检查数据库连接是否成功
- 输出连接测试结果

## 使用方法

要使用这个 Action，请在你的工作流文件（`.github/workflows/your-workflow.yml`）中添加以下步骤：

```yaml
steps:
  - name: 检查数据库连接
    uses: candies404/db-connection-check@v1
    with:
      database_uri: ${{ secrets.DATABASE_URI }}
```

### 输入

| 参数           | 描述                 | 是否必需 |
| -------------- | -------------------- | -------- |
| `database_uri` | 用于连接的数据库 URI | 是       |

### 输出

| 参数      | 描述                             |
| --------- | -------------------------------- |
| `success` | 数据库连接是否成功（true/false） |

## 示例

以下是一个完整的工作流示例，演示如何使用此 Action：

```yaml
name: 数据库连接测试

on:
  workflow_dispatch:

jobs:
  test-db-connection:
    runs-on: ubuntu-latest
    steps:
      - name: 检出代码
        uses: actions/checkout@v4

      - name: 数据库连接检查
        id: db-check
        uses: candies404/db-connection-check@v1
        with:
          database_uri: ${{ secrets.DATABASE_URI }}

      - name: 输出结果
        run: echo "数据库连接测试结果：${{ steps.db-check.outputs.success }}"
```

## 注意事项

- 确保在仓库的 Secrets 中设置了 `DATABASE_URI`。
- 数据库 URI 应该包含所有必要的连接信息，格式如下：
  `mysql://username:password@host:port/database`
- 此 Action 目前支持 MySQL 数据库。如需支持其他数据库类型，请查看未来更新或提交 issue。

## 贡献

欢迎贡献！如果你有任何建议或改进，请提交 issue 或 pull request。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](https://github.com/candies404/db-connection-check/blob/main/LICENSE) 文件。

## 联系方式
如果您有任何问题或需要支持，请通过以下方式联系我们：

- 在 GitHub 上提交 issue
- 发送邮件至：sugar404@qq.com

感谢您使用 DingTalk Notification Action！
