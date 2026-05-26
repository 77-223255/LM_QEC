# Changelog

## 2026-05-06

### Added
- `[reading/](./reading/)` — 论文、教材等阅读资料归档
  - `Solving_Quantum_Many_Body_with_Neural_Networks.pdf`
  - `Fault_Tolerant_QC_Trapped_Ions_Walking_Cat.pdf`
  - `Artificial_Intelligence_for_Quantum_Computing.pdf`
  - `QCalEval_Benchmarking_Vision-Language_Models.pdf`
  - `Logical_Quantum_Processor_Reconfigurable_Atom_Arrays.pdf`
  - `QI_E_Lecture_Notes_Intro_QEC.pdf`
  - `Topological_Quantum_Compiling_with_RL.pdf`
  - `[Gottesman/](./reading/Gottesman/)`
    - `Class_of_QEC_Codes_Saturating_Hamming_Bound.pdf`
    - `Stabilizer_Codes_and_QEC.pdf`
    - `Surviving_as_Quantum_Computer_Classical_World.pdf`
  - `[lin/](./reading/lin/)`
    - `Quantum_Adiabatic_Algorithm_Design_with_RL.pdf`
    - `Quantum_Adiabatic_Doping_Incommensurate_Lattices.pdf`
    - `Quantum_Adiabatic_Doping_Fermi_Hubbard.pdf`
    - `Universal_Quantum_Optimization_Cold_Atoms.pdf`
    - `Adaptive_Quantum_Optimization_Algorithms.pdf`
    - `Efficient_Preparation_Fermionic_Superfluids.pdf`
    - `Hard_Instance_Learning_Quantum_Adiabatic_Factorization.pdf`
- `[what_i_learn/](./what_i_learn/)` — 学习笔记

### Changed
- 清空仓库，仅保留 README，重新组织为资料归档结构

### Removed
- `QI_E.pdf`, `QI_E_learn.py` — 已迁移至 `reading/`

## 2026-05-26

### Changed
- `[reading/](./reading/)` 重构：清空旧散乱文件，搬入 `origin/`（`papers/` + `lectures/`）和 `guide/`（4 条路线 MD）
- `[what_i_learn/](./what_i_learn/)` 合并 `my_works/`，新增期末作业说明
- 所有论文统一命名格式为 `年份_标题.pdf`

### Added
- `[reading/origin/papers/](./reading/origin/papers/)` — 所有论文平铺（30 篇）
- `[reading/origin/lectures/](./reading/origin/lectures/)` — 讲义/书（3 份）
- `[reading/guide/](./reading/guide/)` — 知识脉络梳理
  - `quantum_error_correction.md` — 量子纠错主线
  - `quantum_optimization.md` — 量子优化与绝热算法
  - `ai_for_quantum.md` — AI+量子计算
  - `topological_and_architecture.md` — 拓扑量子计算与物理架构
- `[what_i_learn/](./what_i_learn/)` — `2026_QEC.pptx` + `2026_量子纠错.pdf`（量子光学期末作业）
- `[what_i_learn/journal.md](./what_i_learn/journal.md)` — 新增 2026-05-22 学习记录

### Removed
- `[reading/](./reading/)` 旧散列 PDF 及 `Gottesman/`、`lin/` 子目录
- `collection/` 作者分类目录
- 所有 `:Zone.Identifier` Windows 残留文件

### Fixed
- `量子纠错导论.pptx` 年份修正：2024 → 2026

## 2026-05-26 (后续)

### Removed
- `[temporary/](./temporary/)` 移出仓库，仅保留为本地工作副本
