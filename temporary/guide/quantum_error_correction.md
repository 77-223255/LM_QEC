# 量子纠错 (Quantum Error Correction)

> 从 Shor 码到 GKP 码，从稳定子码到表面码阈值突破。
> 这是当前主要的研究方向。

---

## 1985–1999：奠基时代

### 1985 — 可逆逻辑与量子计算机 `[F]`
- **Asher Peres**
- 早期量子计算理论雏形，讨论可逆逻辑与量子计算的关系
- [origin/papers/1985_Reversible_Logic_and_Quantum_Computers.pdf](../origin/papers/1985_Reversible_Logic_and_Quantum_Computers.pdf)

### 1995 — Shor 码与大数因子分解 `[F]`
- **Peter Shor**
- 提出 Shor 算法和 9 比特量子纠错码，量子纠错领域原点
- [origin/papers/1995_Polynomial_Time_Algorithms_for_Prime_Factorization_and_Discrete_Logarithms.pdf](../origin/papers/1995_Polynomial_Time_Algorithms_for_Prime_Factorization_and_Discrete_Logarithms.pdf)

### 1996 — 达到 Hamming 边界的量子纠错码 `[F]`
- **Daniel Gottesman**
- 构造了一类达到量子 Hamming 边界的纠错码
- [origin/papers/1996_Class_of_QEC_Codes_Saturating_the_Quantum_Hamming_Bound.pdf](../origin/papers/1996_Class_of_QEC_Codes_Saturating_the_Quantum_Hamming_Bound.pdf)

### 1997 — 稳定子码与量子纠错（博士论文）`[F]`
- **Daniel Gottesman**
- 系统建立了稳定子码（Stabilizer Code）理论框架，QEC 的基石
- [origin/papers/1997_Stabilizer_Codes_and_Quantum_Error_Correction.pdf](../origin/papers/1997_Stabilizer_Codes_and_Quantum_Error_Correction.pdf)

### 1997 — 任意子容错量子计算 `[F]`
- **Alexei Kitaev**
- 提出任意子（Anyon）用于容错量子计算的方案，拓扑量子计算起源
- [origin/papers/1997_Fault_Tolerant_Quantum_Computation_by_Anyons.pdf](../origin/papers/1997_Fault_Tolerant_Quantum_Computation_by_Anyons.pdf)

---

## 2000–2009：拓扑码与 GKP 码

### 2001 — GKP 码：在谐振子中编码量子比特 `[F]`
- **Gottesman, Kitaev, Preskill**
- 提出玻色子 GKP 量子纠错码，将量子比特编码在谐振子中
- [origin/papers/2001_Encoding_a_Qubit_in_an_Oscillator.pdf](../origin/papers/2001_Encoding_a_Qubit_in_an_Oscillator.pdf)

### 2002 — 拓扑量子记忆 `[F]`
- **Dennis, Kitaev, Landahl, Preskill**
- 系统分析表面码的拓扑量子记忆性质，奠定表面码理论基础
- [origin/papers/2002_Topological_Quantum_Memory.pdf](../origin/papers/2002_Topological_Quantum_Memory.pdf)

---

## 2010–2019：表面码时代

### 2012 — 表面码匹配解码阈值证明 `[F]`
- **Austin G. Fowler**
- 证明表面码最小权重完美匹配（MWPM）解码的有限阈值
- [origin/papers/2012_Proof_of_Finite_Surface_Code_Threshold_for_Matching.pdf](../origin/papers/2012_Proof_of_Finite_Surface_Code_Threshold_for_Matching.pdf)

---

## 2020–2026：突破与大实验时代

### 2023 — 扩展表面码逻辑量子比特抑制错误 `[B]` `[E]`
- **Google Quantum AI**
- Nature：首次实验证明表面码逻辑量子比特的误差随规模增长而指数抑制
- [origin/papers/2023_Suppressing_Quantum_Errors_by_Scaling_a_Surface_Code_Logical_Qubit.pdf](../origin/papers/2023_Suppressing_Quantum_Errors_by_Scaling_a_Surface_Code_Logical_Qubit.pdf)

### 2023 — GKP 码进展综述 `[R]`
- **Brady et al.**
- GKP 码的理论、工程与应用的全面综述
- [origin/papers/2023_Advances_in_Bosonic_Quantum_Error_Correction_with_GKP_Codes.pdf](../origin/papers/2023_Advances_in_Bosonic_Quantum_Error_Correction_with_GKP_Codes.pdf)

### 2024 — 表面码阈值突破 `[B]` `[E]`
- **Google Quantum AI**
- Nature：首次实验实现表面码低于阈值的量子纠错
- [origin/papers/2024_Quantum_Error_Correction_Below_the_Surface_Code_Threshold.pdf](../origin/papers/2024_Quantum_Error_Correction_Below_the_Surface_Code_Threshold.pdf)

### 2024 — 可重构原子阵列逻辑量子处理器 `[B]` `[E]`
- **Dolev Bluvstein et al. (Harvard)**
- Nature 封面：中性原子阵列实现逻辑量子处理器
- [origin/papers/2024_Logical_Quantum_Processor_Based_on_Reconfigurable_Atom_Arrays.pdf](../origin/papers/2024_Logical_Quantum_Processor_Based_on_Reconfigurable_Atom_Arrays.pdf)

### 2025 — 集成光子 GKP 量子比特源 `[E]`
- **M. V. Larsen et al. (Xanadu)**
- 集成光子芯片上产生 GKP 量子比特
- [origin/papers/2025_Integrated_Photonic_Source_of_Gottesman_Kitaev_Preskill_Qubits.pdf](../origin/papers/2025_Integrated_Photonic_Source_of_Gottesman_Kitaev_Preskill_Qubits.pdf)

### 2026 — AI 表面码预解码器
- **Christopher Chamberland et al. (NVIDIA)**
- 基于 AI 的表面码快速预处理解码器
- [origin/papers/2026_Fast_and_Accurate_AI_Based_Pre_Decoders_for_Surface_Codes.pdf](../origin/papers/2026_Fast_and_Accurate_AI_Based_Pre_Decoders_for_Surface_Codes.pdf)

### 2026 — 离子阱 Walking Cat 架构 `[E]`
- **Felix Tripier et al. (IonQ)**
- IonQ 的容错量子计算机架构方案
- [origin/papers/2026_Fault_Tolerant_Quantum_Computing_with_Trapped_Ions_Walking_Cat_Architecture.pdf](../origin/papers/2026_Fault_Tolerant_Quantum_Computing_with_Trapped_Ions_Walking_Cat_Architecture.pdf)

---

## 讲义 / 教程

### 2025 — 量子纠错导论 (PHY265) `[L]`
- **A. C. Quillen (Toronto)**
- 系统性的 QEC 课程讲义
- [origin/lectures/2025_Introducing_Quantum_Error_Correction_Lecture_Notes.pdf](../origin/lectures/2025_Introducing_Quantum_Error_Correction_Lecture_Notes.pdf)

### 2026 — Quantum Computer in a Classical World `[L]`
- **Daniel Gottesman (Perimeter)**
- 量子计算机如何在经典世界中"生存"的生动讲义
- [origin/lectures/2026_Surviving_as_a_Quantum_Computer_in_a_Classical_World.pdf](../origin/lectures/2026_Surviving_as_a_Quantum_Computer_in_a_Classical_World.pdf)

### 2023 — QEC For Dummies `[L]`
- **Avimita Chatterjee, Koustubh Phalak, Swaroop Ghosh (Penn State)**
- 面向初学者的量子纠错入门教程
- [origin/papers/2023_Quantum_Error_Correction_For_Dummies.pdf](../origin/papers/2023_Quantum_Error_Correction_For_Dummies.pdf)
