# journal — 组会 & 学习记录

用于记录组会汇报、学习心得、问题讨论等。

(PPT 文件已规范命名为 `2026_量子纠错导论.pptx`)

## 2026-05-22

### 今日内容
- 量子光学课程期末作业汇报
- [2026_QEC.pptx](./2026_QEC.pptx) + [2026_量子纠错.pdf](./2026_量子纠错.pdf) — 量子纠错综述
- 从 Shor 码到表面码阈值突破，涵盖稳定子框架、GKP 码与混合级联架构

### 架构理解
通过对于 GKP 的理解，目前的框架是稳定子框架之后有了离散码和连续码的认知。


## 2026-05-13

### 今日内容
- [2026_量子纠错导论.pptx](./2026_量子纠错导论.pptx) — 先介绍 Shor 码，接着讲述量子纠错码的定义、线性性质、QECC 充分条件及简并码概念

### 当前困难
部分表达式细节理解不深，如 QECC 条件证明中关于秩的概念的描述。

### 架构理解
之前的整体框架无需修改。在此前基本码理解的基础上，增加了对量子纠错码概念本身的数学化描述：定义及其性质、实现纠错操作的条件，以及为这些概念服务的附加概念。

### 下一步计划
- 继续学习 [Surviving_as_a_Quantum_Computer_in_a_Classical_World.pdf](../reading/origin/lectures/2026_Surviving_as_a_Quantum_Computer_in_a_Classical_World.pdf) 第 2–3 章衔接部分
- 启动稳定子框架的具体学习
- 为解决细节不清问题，引入 Python 代码从零搭建纠错码，确保细节清晰
- 目标：完成第三章开头 Shor 码的介绍，并至少进入稳定子框架

## 2026-05-06

### 今日内容
- [2026_量子纠错导论.pptx](./2026_量子纠错导论.pptx) — 引言部分 & 三量子比特纠错码（比特翻转、相位翻转）

### 当前困难
[2025_Introducing_Quantum_Error_Correction_Lecture_Notes.pdf](../reading/origin/lectures/2025_Introducing_Quantum_Error_Correction_Lecture_Notes.pdf) 从基本电路框架直接跳入稳定子框架，中间衔接不足，理解困难。

### 架构理解

量子纠错的理解框架目前梳理为三层：

1. **第一层 — 基本码**：如 3-bit 码、Shor 码等。在稳定子引入之前即被提出，具有强经典引入特性，人为直接构造。重点在于理解各码本身的特点。
2. **第二层 — 稳定子框架**：在第一层基础上提炼，通过引入稳定子形式化实现。
3. **第三层 — 框架扩展**：稳定子框架建立后涌现的各类纠错码。

AI/大模型与量子纠错的结合点主要在**解码阶段**（症状 → 物理错误映射）。因此至少需要理解稳定子框架搭建后各类纠错码的具体形式及其输入输出。

### 下一步计划
- 学习 [Surviving_as_a_Quantum_Computer_in_a_Classical_World.pdf](../reading/origin/lectures/2026_Surviving_as_a_Quantum_Computer_in_a_Classical_World.pdf) 第 2–3 章衔接部分，梳理从基本纠错到稳定子形式化的逻辑主线
- 目标：下周汇报前完成稳定子衔接部分的学习
