<div align="center">

# 🎓 导师 Skill

**把导师蒸馏成 AI，随时获得他/她的学术指导**

*那一天，人们回想起了被导师支配的恐惧。*

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-blue)](https://claude.ai/claude-code)
[![Version](https://img.shields.io/badge/version-1.1.0-green)](https://github.com/Azurboy/Professor_skill)

<br>

灵感来自 [前任.skill](https://github.com/therealXiaomanChu/ex-skill) 与 [同事.skill](https://github.com/titanwings/colleague-skill)，  
同是"蒸馏一个人"——这次蒸馏的是你的导师。

</div>

---

## 它是什么

不是一个通用的"AI 学术助手"。

导师 Skill 会把你**某一位具体的导师**蒸馏成一个可复用的 Claude Code Skill。蒸馏之后，`/mentor-zhang-san` 回来的不是 Claude，是张三教授——用他/她真实的说话方式、学术立场、指导哲学来和你对话。

核心材料来自两个来源：

- **公开学术数据**：Google Scholar、百度学术、知网、个人主页——自动采集，你只需提供名字和学校
- **聊天记录（可选）**：微信、邮件——从中提取他/她说话的"灵魂"

---

## 和通用 AI 有什么区别

| 场景 | 通用 AI 的回答 | 导师 Skill 的回答 |
|------|--------------|----------------|
| 论文 introduction 写法 | "清晰陈述问题、背景、贡献" | "你这句话太长了。先说你要解决什么问题，一句话。" |
| 要不要用 Transformer | "各有优劣，取决于数据规模" | "小数据集上我不太相信 Transformer，跑个 baseline 再说" |
| 被拒稿了怎么办 | "不要气馁，继续努力" | "reviewer comments 你看了吗？那才是最值钱的东西" |
| 选研究方向 | "建议结合兴趣和市场需求" | "你想和谁合作？好的合作者比方向更重要" |

---

## 快速开始

### 安装

```bash
# 克隆到本地 skill 目录
git clone https://github.com/Azurboy/Professor_skill.git
cp -r Professor_skill ~/.claude/skills/create-mentor

# 或使用 OpenClaw skills 管理器
/skills-manager sync Azurboy/Professor_skill
```

### 创建你的第一个导师

```
/create-mentor
```

**系统：** 你的导师叫什么？在哪个学校？

**你：** 张三，某某大学

**系统：** 你们是什么关系？

**你：** 硕士导师

**系统：** 好的，正在自动采集张三的学术公开数据...
```
✅ Google Scholar — 找到 42 篇论文，h-index: 18
✅ 百度学术    — 找到 23 篇中文论文
✅ 个人主页    — http://cs.xxx.edu.cn/~zhangsan/
✅ ORCID       — 0000-0001-xxxx-xxxx
```
是否补充聊天记录？（A 微信/邮件 / B 手动描述 / C 跳过）
```

搞定。之后运行 `/mentor-zhang-san` 即可。

---

## 完整操作案例

### 案例一：论文反馈

```
> /mentor-zhang-san

你好，我的 introduction 写完了，帮我看看。

[粘贴段落]

"本研究旨在通过对社交媒体数据的多模态分析，
探讨疫苗信息传播的平台差异性及其影响因素，
以期为公共卫生传播策略提供理论依据与实践参考。"
```

**导师（张三）：**

> 这句话太长了。一个句子里有三层意思，读者记不住。
>
> 试试这样拆：先说你发现了什么现象，再说你用什么方法，最后说意义。不要一上来就说"旨在"——先让读者知道问题在哪里。
>
> 还有——"以期为…提供理论依据与实践参考"这句话几乎每篇论文都有，删掉，留在 discussion 里说。

---

### 案例二：研究方向选择

```
> /mentor-zhang-san

我在纠结用 LLM 做内容分析，还是用传统的编码方法。你怎么看？
```

**导师：**

> 取决于你的 RQ 是什么。
>
> 如果你想解释"为什么"，传统编码更可靠，审稿人认。如果你在处理大规模数据，LLM 是你唯一的选项，但你需要认真做 validation。
>
> 你现在数据量大概多少？

---

### 案例三：被拒稿后

```
> /mentor-zhang-san

我们投 ICWSM 的那篇被拒了，三个 reviewer 都给了 reject。
```

**导师：**

> 好，把 comments 发给我看看。
>
> 被拒不是问题，reviewer 说了什么才是问题。他们如果是在说"motivation 不清晰"，那是写作问题，好改。如果说"方法有根本性缺陷"，那要重新想。
>
> 先不要看分数，先看 Weakness 那一栏。

---

### 案例四：临近截止日

```
> /mentor-zhang-san

还有 48 小时截稿，我的 related work 还没写完，experiment 有个结果还没出来。
```

**导师：**

> experiment 那个结果出不来就先不要放，写"future work"。related work 现在先把你最核心的 5 篇写完，其他的截稿后补。
>
> 你现在最缺的是哪一段？

---

### 案例五：自动纠偏

```
> /mentor-zhang-san

你刚才鼓励我说"加油你一定行！"——我导师不会这样说的。
```

**系统：**

> 明白了。他实际更可能怎么说？

**你：**

> 他就说"继续"两个字，最多再加一句"这个方向是对的"。

**系统：**

> 已记录。更新 Layer 3（情感表达）——克制型，认可方式为一句话或两个字，不使用感叹号和激励语。是否保存到 persona.md？

---

## 三轨画像结构

导师 Skill 生成三个文件，各司其职：

```
mentors/zhang-san/
├── history.md      ← 你们的指导经历、关键对话（PART A）
├── persona.md      ← 他/她的灵魂，5 层结构（PART B）
├── academic.md     ← 论文、研究立场、审稿偏好（PART C）
├── sources.json    ← 采集来源记录
└── SKILL.md        ← /mentor-zhang-san 的完整脚本
```

### PART B 的 5 层灵魂结构

学习自 [同事.skill](https://github.com/titanwings/colleague-skill) 的人物构建方式，从聊天记录里提取的不是"他是个好人"这种描述，而是有据可查的行为模式：

| 层级 | 内容 | 示例 |
|------|------|------|
| **Layer 0** | 底线（永不违背） | "不会无原则鼓励；不替学生做决定" |
| **Layer 1** | 语言与表达风格 | "惜字如金；反问式批评；不用感叹号" |
| **Layer 2** | 教学哲学 | "苏格拉底式追问；数据说话" |
| **Layer 3** | 情感表达 | "认可用一两个字；批评用反问" |
| **Layer 4** | 人际边界 | "师生边界清晰；不主动聊私事" |
| **Layer 5** | 决策模式 | "问题倒逼答案；让学生先做判断" |

### 聊天记录提取逻辑

从微信/邮件里，Skill 会找：

- **标志性句式**：批评时用什么句式，肯定时用什么词
- **情绪证据**：高压期语气有没有变化，表情符号频率
- **知识取向**：主动展开什么话题，一笔带过什么
- **边界信号**：几点回消息，是否聊非学术话题

每条发现都附原文证据，不瞎猜。

---

## 命令速查

| 命令 | 功能 |
|------|------|
| `/create-mentor` | 创建新导师 |
| `/list-mentors` | 列出所有导师 |
| `/mentor-{slug}` | 和导师对话 |
| `/{slug}-persona` | 查看人物灵魂（5 层） |
| `/{slug}-academic` | 查看学术画像 |
| `/mentor-append {slug}` | 追加新材料（演化） |
| `/rollback {slug}` | 回滚到上一版本 |
| `/mentor-retire {slug}` | 删除（"感谢您的指引，一路顺风。"） |

---

## 与 OpenClaw 配合使用

[OpenClaw](https://github.com/Enderfga/openclaw-claude-code) 是 Claude Code 的编排层，可以把导师 Skill 嵌入程序化工作流：

```python
import openclaw

# 单导师审稿
session = openclaw.create_session()
session.send("/mentor-zhang-san 这段 related work 有没有遗漏重要文献？")

# 多导师并行——同一份草稿，听取不同导师的意见
team = openclaw.create_team([
    "mentor-zhang-san",
    "mentor-prof-smith"
])
opinions = team.parallel_send("这个研究设计有什么根本性问题？")
print(opinions)  # 两位导师的不同角度

# 批量处理：让导师逐章审稿
chapters = ["introduction.md", "method.md", "results.md"]
for chapter in chapters:
    content = open(chapter).read()
    session.send(f"/mentor-zhang-san 审阅这一章：\n{content}")
```

**典型场景：**
- 论文不同章节分配给不同导师审
- 深夜改稿时随时调用，不占用导师真实时间
- 多位导师"圆桌"讨论研究决策

---

## 数据来源

| 来源 | 覆盖 | 提取内容 |
|------|------|---------|
| Google Scholar | 全球英文学者 | 论文、h-index、研究方向 |
| 百度学术 | 中国学者 | 中文论文、合作者 |
| 知网（CNKI） | 中国大陆 | 学位论文、期刊 |
| Google 搜索 | 公开网页 | 主页、实验室、采访 |
| ORCID | 注册研究者 | 自述、项目 |
| 大学主页 | 院校官网 | 职称、联系方式 |

**伦理声明**：仅采集公开数据，尊重 robots.txt，善意使用。如果你用了，不妨告诉导师——他/她可能比你更感兴趣。

---

## 项目灵感

这个项目站在两个作品的肩膀上：

**[前任.skill](https://github.com/therealXiaomanChu/ex-skill)** by 真小满🧊
> 率先提出"把一个人蒸馏成 Skill"——人物画像的两轨结构（关系记忆 + 人物性格）源自这里。

**[同事.skill](https://github.com/titanwings/colleague-skill)** by titanwings
> 扩展到职场场景，建立了人物灵魂的 5 层结构，以及从聊天记录中提取行为模式的方法论。

导师 Skill 在此基础上加入了学术场景的第三轨（PART C 学术画像），以及对公开学术数据的自动采集。

---

## 答辩委员会（多导师 · 独立 Skill）

> 一个人的导师不够用？把整个委员会请进来。

`defense-committee` 是建立在导师 Skill 之上的多智能体答辩模拟器——把多位委员的学术风格叠加在一起，模拟一场让你真正出汗的答辩。

### 快速启动

```
/defense-committee
```

系统会引导你：选模式 → 输入委员名单 → 粘贴论文摘要 → 开始答辩。

**支持三种模式**，自动调整提问策略和评审标准：

| 模式 | 核心问题 | 最终输出 |
|------|---------|---------|
| **开题报告** | 选题值得做吗？方案可行吗？ | 建议列表 + 是否批准 |
| **中期检查** | 进展够吗？方向跑偏了吗？ | 通过 / 有条件通过 / 需重大调整 |
| **毕业答辩** | 贡献站得住吗？实验够严谨吗？ | 优秀 / 通过 / 小修 / 大修 / 不通过 |

### 一键批量导入委员

不需要提前一个个创建导师档案。直接给名单，系统自动爬取并行导入：

```
/defense-committee

请提供委员名单：
张三，清华大学计算机系
李四，北京大学信息科学学院
王五，中国科学院计算技术研究所
```

```
🔍 张三（清华大学）—— 爬取中...
🔍 李四（北京大学）—— 爬取中...
🔍 王五（中科院）  —— 爬取中...

✅ 全部就绪。委员会已组建：
   张三（主席）· 机器学习 · h-index: 32
   李四（委员）· 自然语言处理 · h-index: 18
   王五（委员）· 计算机视觉 · h-index: 25
```

已有的导师档案自动复用，不重复爬取。

### 答辩示例（毕业答辩模式）

```
[你] 我的研究聚焦于低资源场景下的跨语言迁移学习...
     [介绍工作 3 分钟]

---

[张三教授（主席）]
你说贡献之一是"提出了一个新的对齐框架"——
这和 2023 年 ACL 那篇 X-Align 有什么本质区别？
你的框架在哪些方面超越了它？

[李四教授]
（接张三的问题）而且你的实验只在三个语言对上测了。
假如换成语言距离更远的组合，比如中文-斯瓦希里语，
你的方法还能 hold 住吗？

[王五教授]
我想换个角度——你的 baseline 配置是什么？
论文里第四章写的是"标准配置"，但没说具体超参数。
这在答辩里说不清楚的。
```

```
[答辩委员会内部评议]

张三：贡献描述不够精准，和已有工作的区分度不清晰。
李四：实验范围偏窄，泛化性存疑。但方法本身有新意。
王五：写作需要规范，实验细节缺失。

---

综合结论：修改后通过（小修）

主要修改意见：
1. 明确与 X-Align 的区别，在 related work 中直接对比
2. 补充更多语言对的实验结果（至少 5 个）
3. 第四章实验配置补充超参数表格
```

### 档案复用

答辩委员的档案存入 `mentors/`，下次开题、中期、毕业答辩直接复用，不重新爬取。

```
committees/
└── defense-20260402-001/
    ├── config.json      ← 委员名单、模式、论文信息
    ├── transcript.md    ← 完整问答记录
    └── verdict.md       ← 评审意见摘要
```

---

## 贡献

欢迎 PR 和 Issue：
- 新增数据源（Semantic Scholar、AMiner？）
- 优化聊天记录分析 prompt
- 新增平台支持（飞书、钉钉自动采集）
- 答辩委员会：支持评分表导出、支持历次答辩对比

---

<div align="center">

MIT License · 为学生和导师的更好互动而生 🎓

</div>
