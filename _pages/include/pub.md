# Publications
{: .section-title }

<div class="publication-search" hidden>
  <label for="publication-query">Search publications</label>
  <div class="publication-search-controls">
    <input id="publication-query" type="search" placeholder="Search by title, author, year, or keyword…" autocomplete="off" aria-controls="publication-results" aria-describedby="publication-search-status">
    <button id="publication-search-clear" type="button" hidden>Clear</button>
  </div>
  <p id="publication-search-status" role="status" aria-live="polite" aria-atomic="true"></p>
</div>
<p id="publication-search-empty" hidden>No matching publications. Try another keyword.</p>

## 2026
{: .publication-year }

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/rerule_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Replay What Matters: Off-Policy Replay for Efficient LLM Reinforcement Unlearning](https://arxiv.org/abs/2606.15333)

**Zirui Pang**, Chenlong Zhang, Haosheng Tan, Zhuoran Jin, Jiaheng Wei, Zixin Zhong

**TL;DR:** We propose ReRULE, which improves RULE by replaying hard cases for more efficient and effective unlearning.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/cameo_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[CAMEO: A Conditional and Quality-Aware Multi-Agent Image Editing Orchestrator](https://arxiv.org/abs/2604.03156)

Yuhan Pu, Hao Zheng, Ziqian Mo, **Zirui Pang**, Hill Zhang, Tianyi Fan, Shuhong Wu, Jiaheng Wei

**TL;DR:** We propose CAMEO, a structured multi-agent framework that reframes conditional image editing as a quality-aware, feedback-driven process and improves average win rate by 20% over state-of-the-art models.
</div>
</div>

## 2025
{: .publication-year }

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/sga_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Label Smoothing Improves Gradient Ascent in LLM Unlearning](https://arxiv.org/pdf/2510.22376)

**Zirui Pang**, Hao Zheng, Zhijie Deng, Ling Li, Zixin Zhong, Jiaheng Wei

**TL;DR:** We propose Smoothed Gradient Ascent (SGA), a Gradient Ascent method improved with generalized label smoothing, which achieves both strong forgetting quality and high model utility in LLM unlearning tasks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL26 finding</div><img src="{{ '/images/offside_pipeline_v6.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OFFSIDE: Benchmarking Unlearning Misinformation in Multimodal Large Language Models](https://arxiv.org/abs/2510.22535)

Hao Zheng, **Zirui Pang**, Ling Li, Zhijie Deng, Yuhan Pu, Zhaowei Zhu, Xiaobo Xia, Jiaheng Wei

[**Project**](https://github.com/zh121800/OFFSIDE){% assign offside_paper = site.data.scholar.papers | where: "id", "L9GRttsAAAAJ:qjMakFHDy7sC" | first %}{% if offside_paper and offside_paper.citations > 0 %} <strong>| Citations: {{ offside_paper.citations }}</strong>{% endif %}

**TL;DR:** OFFSIDE benchmarks multimodal unlearning with real-world football transfer rumors, revealing that current methods struggle to forget visual misinformation and remain vulnerable to recovery and prompt attacks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025 Workshop</div><img src="{{ '/images/guard_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GUARD: Generation-time LLM Unlearning via Adaptive Restriction and Detection](https://arxiv.org/abs/2505.13312)

Zhijie Deng, Chris Yuhao Liu, **Zirui Pang**, Xinlei He, Lei Feng, Qi Xuan, Zhaowei Zhu, Jiaheng Wei

**TL;DR:** We propose Generation-time Unlearning via Adaptive Restriction and Detection (GUARD), a framework that enables dynamic unlearning during LLM generation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/reveal_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[When VLMs Meet Image Classification: Test Sets Renovation via Missing Label Identification](https://arxiv.org/pdf/2505.16149)

**Zirui Pang**, Haosheng Tan, Yuhan Pu, Zhijie Deng, Zhouan Shen, Keyu Hu, Jiaheng Wei

[**Project**](https://github.com/ZiruiPang/REVEAL-label-renovation){% assign reveal_paper = site.data.scholar.papers | where: "id", "L9GRttsAAAAJ:u-x6o8ySG0sC" | first %}{% if reveal_paper and reveal_paper.citations > 0 %} <strong>| Citations: {{ reveal_paper.citations }}</strong>{% endif %}

**TL;DR:** We investigate the limitations of VLM in image classification task, and propose a VLM-based test-data renovation pipeline that detects potential label errors and missing labels.
</div>
</div>
