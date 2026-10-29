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

**TL;DR:** ReRULE reuses low-reward hard cases through importance-weighted off-policy replay to improve LLM reinforcement unlearning efficiency and retained knowledge quality at modest additional training cost.
</div>
</div>

## 2025
{: .publication-year }

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/sga_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Label Smoothing Improves Gradient Ascent in LLM Unlearning](https://arxiv.org/pdf/2510.22376)

**Zirui Pang**, Hao Zheng, Zhijie Deng, Ling Li, Zixin Zhong, Jiaheng Wei

**TL;DR:** Smoothed Gradient Ascent (SGA) applies label smoothing to stabilize gradient ascent and improve LLM unlearning effectiveness across benchmarks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL26 finding</div><img src="{{ '/images/offside_pipeline_v6.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OFFSIDE: Benchmarking Unlearning Misinformation in Multimodal Large Language Models](https://arxiv.org/abs/2510.22535)

Hao Zheng, **Zirui Pang**, Ling li, Zhijie Deng, Yuhan Pu, Zhaowei Zhu, Xiaobo Xia, Jiaheng Wei

[**Project**](https://github.com/zh121800/OFFSIDE) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

**TL;DR:** OFFSIDE benchmarks multimodal unlearning with real-world football transfer rumors, revealing that current methods struggle to forget visual misinformation and remain vulnerable to recovery and prompt attacks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/guard_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GUARD: Generation-time LLM Unlearning via Adaptive Restriction and Detection](https://arxiv.org/abs/2505.13312)

Zhijie Deng, Chris Yuhao Liu, **Zirui Pang**, Xinlei He, Lei Feng, Qi Xuan, Zhaowei Zhu, Jiaheng Wei

**TL;DR:** GUARD detects forget-related prompts and adaptively blocks forbidden tokens during generation, enabling effective LLM unlearning while preserving model utility.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">under review</div><img src="{{ '/images/reveal_pipeline.png' | relative_url }}" alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[When VLMs Meet Image Classification: Test Sets Renovation via Missing Label Identification](https://arxiv.org/pdf/2505.16149)

**Zirui Pang**, Haosheng Tan, Yuhan Pu, Zhijie Deng, Zhouan Shen, Keyu Hu, Jiaheng Wei

[**Project**](https://github.com/ZiruiPang/REVEAL-label-renovation) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>

**TL;DR:** REVEAL combines multiple vision-language models with human feedback to identify missing and noisy labels and improve image classification test sets with soft labels aligned with human judgments.
</div>
</div>
