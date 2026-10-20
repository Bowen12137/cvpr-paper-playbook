# CVPR Paper Playbook

**把研究问题、核心主张、实验和图表连成一条可信的论证。**

面向 CVPR 及相近视觉会议作者的研究、写作与投稿前预审 skill。支持中文讨论、英文稿件和中文转英文。默认先给可用判断或稿件，再按需要展开证据。

> An evidence-first research, writing, and pre-submission review skill for computer vision papers. It offers conditional readiness assessments, not acceptance predictions.

## 能做什么

| 你目前的问题 | 产出 |
|---|---|
| 方向没有同主题 Oral，该学什么？ | 跨领域可迁移的研究与论证方法 |
| 方案有了，但 story 不清楚 | 中心命题、贡献定位、最小判别实验 |
| 四章怎么写？ | Introduction、Background、Method、Experiments 的段落任务与草稿 |
| 实验做了一堆，是否够用？ | 主张—证据矩阵、公平基线、机制消融、泛化与失败处理 |
| Figure 1、pipeline、结果怎么画？ | 逐图职责、面板布局、比较条件与 caption |
| 论文现在能投吗？ | 当前倾向、证据定位、决定性缺口及判断翻转条件 |
| 怎么回复审稿意见？ | 逐条问题追踪、证据对应、回复稿与未解决项 |
| 如何润色、核引用和整理复现材料？ | 忠实改稿、术语一致、来源支持与可用性说明 |

特色是把各环节连起来：**观察 → 设计 → 判别实验 → 有边界的结论**。不要求所有论文都有复杂 pipeline、全面 SOTA、OOD 或真机实验；选择由研究主张决定。

## 快速开始

下载或克隆本仓库后进入目录。安装器仅使用 Python 3.9+ 标准库，不需要 API key，也不会联网或上传材料。

```bash
git clone https://github.com/Bowen12137/cvpr-paper-playbook.git
cd cvpr-paper-playbook
python3 scripts/install.py
```

默认安装到 `~/.agents/skills/cvpr-paper-playbook`。指定宿主已有的技能目录：

```bash
python3 scripts/install.py --dest-dir ~/.codex/skills
```

已有同名目录时默认拒绝覆盖。确认升级时使用以下命令；旧版备份到技能发现目录之外，命令会打印位置：

```bash
python3 scripts/install.py --dest-dir ~/.codex/skills --replace
```

只选择一个已被宿主识别的位置，避免两处安装同名技能。也可手动复制 `skills/cvpr-paper-playbook/` 到项目的 `.agents/skills/`。发现规则及刷新方式见 [官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

在支持技能的 Codex 环境中使用：

```text
使用 $cvpr-paper-playbook，根据我的研究方案，给出中心故事、
Introduction / Background / Method / Experiments 的详细提纲，
并把每条贡献对应到实验和图表。先指出最值得验证的问题。
```

其他助手也可读取 `SKILL.md` 及相关 references 作为工作说明；文件结构兼容性不代表已在所有产品上完成实测。

## 投稿前预审：回答“能不能过”

```text
使用 $cvpr-paper-playbook，对我的论文做作者投稿前预审。
先给当前倾向和信心，再定位最可能影响结果的三项问题。
每项给出稿件证据、最低成本补证和什么结果会改变判断。
请区分论文未做的工作与我尚未提供的材料。
```

预审输出采用四档自定义倾向：**证据不足以判断、当前偏拒、边界状态、具备竞争力**。有明显问题会直接指出；有贡献且证据充分也应明确肯定。它不是官方评分，也不输出未经校准的录用概率。

只有摘要时评估定位；完整主文时检查技术与实验；代码没有运行就不声称复现通过。需要三种评审视角时可以明确要求，它们共享事实底稿，不冒充三个独立审稿人。

本功能用于作者自查和公开论文讨论。正式受托审稿需遵守目标会议当年的保密与 LLM 规则，不能把作者助手当成提交正式 review 的替代品。

## 写作、实验与图表一起改

```text
使用 $cvpr-paper-playbook，检查这份实验表能支持哪些贡献。
给出一张“主张—现有证据—竞争解释—下一步实验—图表”矩阵，
再据此重写 Introduction 的贡献段，不添加未完成的结果。
```

```text
使用 $cvpr-paper-playbook，帮我写 rebuttal。
先按问题编号整理意见，再区分已有证据、已完成修改和计划实验。
输出英文回复及未解决清单，不虚构页码或新增结果。
```

## 吸收了哪些 Nature 系列工作流

吸收证据追踪、术语一致、段落功能、不同评审重点、逐条回复和图表科学任务，并按 CV/ML 场景重写。保留 CVPR 的贡献类型和实验语境，不套用 Nature 的跨学科门槛、CNS 文献限制或期刊修回流程。

本包独立运行，不依赖 Nature 系列技能。详细说明见 [来源与适配](skills/cvpr-paper-playbook/references/provenance.md)。

## 仓库结构

```text
skills/cvpr-paper-playbook/
  SKILL.md                    任务入口与按需路由
  agents/openai.yaml          UI 元信息
  references/
    writing.md                章节与故事
    experiments.md            实验论证
    figures.md                图表设计
    review.md                 作者预审
    rebuttal.md               回复审稿
    revision.md               忠实改稿
    sources-and-reproducibility.md
    learning-from-oral.md
    templates.md
    evidence.md
    provenance.md
examples/                     合成输入及示范判断
scripts/                      安装与结构校验
tests/                        安装测试与行为验收案例
docs/                         贡献与验证说明
```

机器人 benchmark、驾驶 safety-critical、SimReady 资产可以作为独立领域技能搭配，本仓库当前只发布总版，不隐式依赖未打包文件。

## 检查与贡献

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

自动检查覆盖格式、内部链接、可移植性和安装行为。模型行为需要另用 [行为案例](tests/behavioral-cases.md) 验证；结构测试不代表审稿准确率。可直接阅读 [预审示例](examples/pre-review.md) 与 [回复示例](examples/rebuttal.md)。

贡献要求见 [贡献说明](docs/CONTRIBUTING.md)。修改应解决一个可复现问题，并说明适用范围；避免把个人偏好变成所有论文的强制规则。

## 依据和限制

来自选择性的 CVPR 阅读案例与研究方法归纳，**没有完成三年全量论文统计**，也没有真实录用预测校准。仓库不包含论文全文、私有阅读库或实验数据。[案例依据](skills/cvpr-paper-playbook/references/evidence.md) 区分历史记录和实际核验范围。

MIT 许可覆盖本仓库自有代码和文字；外部论文与第三方资源保留各自权利。项目与 IEEE/CVF、CVPR、Nature、OpenAI 无官方隶属或认可关系。
