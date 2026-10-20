# 案例依据与使用边界

这是选择性案例的经验提炼，不是对1,613篇的完成声明，不提供总体频率、显著性或录用保证。2026-10-20 已重新阅读下列 4D-DRESS、AIpparel、CUT3R 的正式 PDF 主文各 pp1–8，并核对版本哈希；视觉检查页分别为 1/4/8、1/4/8、1/4/6/8。页码为 PDF 从1起的页序。其他历史笔记不算本轮复核。建议是分析者归纳，论文只提供案例证据，不是作者对本 skill 的认可。

## 4D-DRESS（CVPR 2024 Highlight）

正式PDF：https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_4D-DRESS_A_4D_Dataset_of_Real-World_Human_Clothing_With_Semantic_CVPR_2024_paper.pdf

- pp1–2 / Figure1、Table1：用真实扫描、语义衣物、参数人体及能力对比表达数据的独特组合；不是简单追求最大帧数。
- pp3–5 / Figure2、Table2：先解释并验证数据生产机制，再讨论下游用途。图中保留人工反馈环节；Table2 在合成数据上评价标注方法，不能写成真实扫描标签的直接准确率。
- pp6–8：既有仿真和重建方法在真实松散衣物上暴露局限，数据论文可通过揭示困难建立价值。
- 独立补充S6–7：HOOD*冻结网络并用每衣全部六序列拟合材料。此证据支持逆向拟合用途，不能直接支持未见运动泛化。
- 主文Table6：Vid2Avatar outer的CD/NC变差但IoU上升，是“困难条件下所有指标都下降”的反例。

主文SHA256：3e2e2410c34320e2b8f43a9b1f6066d9a43421c84956e49076ea10a2b3586d28。

本轮另读[补充PDF](https://openaccess.thecvf.com/content/CVPR2024/supplemental/Wang_4D-DRESS_A_4D_CVPR_2024_supplemental.pdf) pp6–7的文字，确认HOOD*拟合范围；补充SHA256：d034557219dbc449030e05d7206ef7be0b692c02f81529845dd3f92d40687766。主文pp6–7与补充p6的仿真服装数量描述不同，本轮未消解，不能据此构造一个确定的总分母。未完整审阅补充或运行实验。

## AIpparel（CVPR 2025 Highlight）

正式PDF：https://openaccess.thecvf.com/content/CVPR2025/papers/Nakayama_AIpparel_A_Multimodal_Foundation_Model_for_Digital_Garments_CVPR_2025_paper.pdf

- pp1–4：引言提出多模态数据不足与编码效率两项障碍；数据和表示设计分别回应，Figure2解释几何对象与token/回归的关系。
- pp5–8：图像任务→多模态任务→编辑→同骨干消融；既建立旧任务可比性，也解释新任务能力。
- p8 / Table5：同骨干比较表示和回归，较跨异构模型榜单更适合支持机制判断。
- pp6–7：多模态基线经外部模型翻译输入；比较包含信息链差异，不能把全部差值归因某个模块。
- p6指标定义/p8限制：panel与edge组合准确率不是整衣制造成功率；真实制作是未来工作。Figure1的渲染用途展示不能跨越此边界。

主文SHA256：f66cfe66167d138d1be4d21c5f4084da473c973d81158e5224835b133f8b4591。主文p6明确指向补充中的人类研究，不能依据主文没有人类研究表格而断言作者没做。

## CUT3R（CVPR 2025 Oral）

正式PDF：https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_Continuous_3D_Perception_Model_with_Persistent_State_CVPR_2025_paper.pdf

- pp1–3：引言先给能力目标，再由相关工作定位差异；必要设定嵌入Method，不单列Background。
- p4 / Figure3：时间方向上的状态更新与右侧虚拟视角读取分区；读取查询不更新状态。
- p6 / Tables2–3：显式区分在线、优化和尺度设置；排名、速度解释需保留这些条件。
- pp7–8 / Table5：revisit使用全序列结束后的状态，不能当作首次在线预测成绩。并非所有指标都优于所有基线。

主文SHA256：b633446e1df67be92f5f8bea5bd79b7c8a09aef591673446e860d75d272aa02b。补充、代码和视频本轮未审阅。

## 其他已读记录提供的反例

- Learning Eigenstructures of Unstructured Data Manifolds：由理论和可解释小例子组织叙述，主文实验逐步扩到几何和高维特征；说明应用画廊和先放总榜不是唯一组织方式。补充未完整核验，不能替代定理条件的详细审查。

这些案例用于选择写作、实验与视觉表达方式，不要求使用skill时逐篇重新下载和阅读。需要引用精确数值或做具体论文批评时，重新定位对应原文。
