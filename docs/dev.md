## 计划

### v0.1

- 第一个版本只需要有编程语言的对比即可，其他显示为待定
- 页面具有的交互包括
  - 悬浮对比对象内容后的实际例子显示
  - 悬浮对比内容时的行突出显示，ok
- 颜色的匹配，ok
- 表格宽度的适配，ok
- 支持弹出窗口

### v0.2

- 支持选择对比的一些

## 开发

### 数据录入问题的解决

- 因为更新频率非常低，且降低初版难度，建议通过本地数据来定义内容。
- 这种复杂数据结构，最适合还是前端直接编辑，然后后台直接存储，而不是用各种模型来束缚。
- 但是如果是表单式编辑，容易出现对列编辑的错误，例如添加错误的列。
- 因此，是否可以有一种数据集的数据结构，其允许对某一个单元格进行修改。

数据形式大概是：
```json
{
    "table_name":
    "records":[
        {
            "category":
            "content":
            "detail":
            "compares":[
                {
                    "name":"Python",
                    "syntax":
                    "sample":
                }
            ]
        }
    ]
}
```

```json
{
    "name":""
    "columns":["A","B","C","D","E"]
    "values":[
        ["1","2","3","4","5"]
    ]
}
```