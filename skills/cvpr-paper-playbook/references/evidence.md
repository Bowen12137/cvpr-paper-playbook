# 案例依据与使用边界

这是既有阅读记录中的作者式经验提炼，供理解建议来源；发布版沿用这些记录，未在本次打包时逐篇重新核验页码和哈希。不是对1,613篇的完成声明，不提供总体频率、显著性或录用保证。建议是分析者归纳，论文只提供具体案例证据；不要把建议措辞伪装成作者原话。

## 4D-DRESS（CVPR 2024 Highlight）

正式PDF：https://openaccess.thecvf.com/content/CVPR2024/papers/Wang_4D-DRESS_A_4D_Dataset_of_Real-World_Human_Clothing_With_Semantic_CVPR_2024_paper.pdf

- pp1–2 / Figure1、Table1：用真实扫描、语义衣物、参数人体及能力对比表达数据的独特组合；不是简单追求最大帧数。
- pp4–6 / Figure2、Table2：先解释并验证数据生产机制，再讨论下游用途。图中保留人工反馈环节。
- pp6–8：既有仿真和重建方法在真实松散衣物上暴露局限，数据论文可通过揭示困难建立价值。
- 独立补充S6–7：HOOD*冻结网络并用每衣全部六序列拟合材料。此证据支持逆向拟合用途，不能直接支持未见运动泛化。
- 主文Table6：Vid2Avatar outer的CD/NC变差但IoU上升，是“困难条件下所有指标都下降”的反例。

主文SHA256：3e2e2410c34320e2b8f43a9b1f6066d9a43421c84956e49076ea10a2b3586d28。

## AIpparel（CVPR 2025 Highlight）

正式PDF：https://openaccess.thecvf.com/content/CVPR2025/papers/Nakayama_AIpparel_A_Multimodal_Foundation_Model_for_Digital_Garments_CVPR_2025_paper.pdf

- pp1–4：引言提出多模态数据不足与编码效率两项障碍；数据和表示设计分别回应，Figure2解释几何对象与token/回归的关系。
- pp5–8：图像任务→多模态任务→编辑→同骨干消融；既建立旧任务可比性，也解释新任务能力。
- p8 / Table5：同骨干比较表示和回归，较跨异构模型榜单更适合支持机制判断。
- pp6–7：多模态基线经外部模型翻译输入；比较包含信息链差异，不能把全部差值归因某个模块。
- p6指标定义/p8限制：panel与edge组合准确率不是整衣制造成功率；真实制作是未来工作。Figure1的渲染用途展示不能跨越此边界。

主文SHA256：f66cfe66167d138d1be4d21c5f4084da473c973d81158e5224835b133f8b4591。创建skill时补充尚未审读，不据此断言补充中没有人类研究或额外实验。

## 其他已读记录提供的反例

- CUT3R：主文p7的revisit利用全序列结束后的状态；它与首次在线预测应区分。并非所有指标都优于所有基线。
- Learning Eigenstructures of Unstructured Data Manifolds：由理论和可解释小例子组织叙述，主文实验逐步扩到几何和高维特征；说明应用画廊和先放总榜不是唯一组织方式。补充未完整核验，不能替代定理条件的详细审查。

这些案例用于选择写作、实验与视觉表达方式，不要求使用skill时逐篇重新下载和阅读。需要引用精确数值或做具体论文批评时，重新定位对应原文。
