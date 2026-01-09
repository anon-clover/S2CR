# $S^{2}CR$
A Self-supervised Self-Consistency Reasoning Framework Coupled to Retrieval-Augmented Generation

Overview


Existing approaches to the self-consistency exploration in Large Language Models (LLMs) primarily rely on post-hoc selection, overlooking the inherent logical structures essential for reasoning. To address this gap, we pioneer a new perspective by introducing $S^{2}CR$, a self-supervised reasoning framework that presents the LLM consistency from internal modeling while coupling retrieval‑augmented generation (RAG) for knowledge integration and process supervision. This framework operates in four stages: Information Retrieval patches the parametric knowledge of LLMs and provides factual grounding for evaluation; Response Generation generates multiple candidate responses for input to explore diverse reasoning paths; Consistency Evaluation quantifies logical consistency by aligning extracted triples from both the generated responses and retrieval information; and Duality Synergy Optimization (DSOP) further bolsters the consistency performance through two complementary modules, Introspection-Driven Self-correction Guidance (IDSG) and Fine-Grained Consensus Alignment (FGCA). Experiments conducted on three public datasets POPQA, Biography, and ALCE-ASQA demonstrate that $S^{2}CR$ achieves objective quantification of internal self-consistency and significantly improves performance ranging from 3.19% to 23.49% over $\textit{Baseline}^{\diamond}$ across diverse foundational LLMs, e.g., GPT-3.5-turbo, GPT-4o, and open-source models LLaMA3-8B and LLaMA3-70B.

### Download
Download PopQA, Bio and ALCE-ASQA.

### Retrieval
Run the following command for Self-CRAG data preparation.
```bash
bash run_data_preprocess.sh
```
We follow the instructions at [Self-RAG (Asai et al., 2023)](https://github.com/AkariAsai/self-rag) for the ultimate results.
