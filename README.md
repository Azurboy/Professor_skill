# 🎓 Professor Skill

Transform your mentor into an **interactive AI persona** that gives you guidance anytime. Distill your professor's academic style, teaching approach, and mentorship into a reusable Claude skill.

> Inspired by [colleague-skill](https://github.com/titanwings/colleague-skill) and [ex-skill](https://github.com/therealXiaomanChu/ex-skill), but tailored for academic mentorship with **auto-scraped research data**.

## ✨ What Makes It Special

Unlike other mentor tools, Professor Skill:

- 🔍 **Auto-scrapes** public academic data (Google Scholar, Baidu, CNKI) to understand your professor's research style
- 📚 **Extracts 3 profiles**: Mentorship records, Communication style, Academic achievements
- 💬 **Activates with one command**: `/mentor-{name}` → Chat with your professor anytime
- 🎯 **Learns from real data**: Papers, citations, teaching patterns, known stances on research topics
- 🌍 **Bilingual support**: Works in English and Chinese (中文)
- 🔄 **Evolves with time**: Append new mentorship records or correct the persona in real-time

---

## 🚀 Quick Start

### Installation

1. Copy the skill into your Claude Code `.claude/skills/` directory:

```bash
mkdir -p ~/.claude/skills/create-mentor
cp -r . ~/.claude/skills/create-mentor/
```

2. Or sync from this repo if you have the skills manager:

```bash
/skills-manager sync Azurboy/Professor_skill
```

### Usage

**Create a new professor skill:**

```bash
/create-mentor
```

You'll be asked:
1. **Professor's name + institution?** (e.g., "张三，清华大学" or "Prof. Smith, MIT")
2. **Relationship type?** (PhD advisor, professor, career mentor, etc.)

Then the skill **auto-scrapes**:
- 📖 Google Scholar profile
- 🔗 Baidu Scholar & CNKI (Chinese academic databases)
- 🏠 Personal homepage & university directory
- 👥 ResearchGate & ORCID profiles

**Use your professor anytime:**

```bash
/mentor-zhang-san

How should I approach the literature review for my thesis?
```

The professor responds **in their actual voice**, with their real academic perspective, teaching style, and known research stances.

---

## 📖 How It Works

### Step 1: Collect (2 Questions)
- Name + institution
- Relationship type

### Step 2: Auto-Scrape (5 Sources)
Parallel scraping of:
- **Google Scholar** → Papers, h-index, research topics
- **Baidu Scholar** → Chinese papers & collaborators
- **CNKI** → National library papers (Chinese academia)
- **Google Search** → Homepage, lab websites, mentions
- **ResearchGate / ORCID** → Self-written bio, projects

### Step 3: Optional Enrichment
- Paste WeChat/email conversations
- Add manual descriptions
- Or skip & use auto-scraped data only

### Step 4: Synthesize Into 3 Parts

**PART A: Mentorship Records**
```markdown
# 张三教授的指导记录

## 研究方向与指导风格
- 主要研究方向：计算机视觉、深度学习
- 指导特点：严谨、注重数学基础、鼓励大胆假设

## 关键指导经历
- **2020年**: 指导我思考如何从小数据集启动项目
- **2021年**: 强调了写作的清晰度比新奇性更重要
```

**PART B: Communication & Personality**
```markdown
# 张三教授的人物画像

## Layer 0: Non-negotiable Rules
- 不会无条件夸奖（会指出问题，目的是帮助）
- 不会说不符合学术严谨性的话

## Speech Patterns
- 标志性口头禅: "让我们看看数据说了什么"
- 教学方式: 提问而非直接回答
```

**PART C: Academic Profile (New!)**
```markdown
# 张三教授的学术画像

## 研究方向 & 代表作
- 主要领域: 计算机视觉、深度学习
- 代表论文: "XXX" (NeurIPS 2022, cited 245x)

## 常用术语 & 论证框架
- 核心概念: neural plasticity, generalization bounds
- 论证方式: 先理论，再实验，最后应用

## 已知立场
- Transformers vs CNN: "很强大，但数据有限时CNN更稳健"
- Reproducibility: 强烈支持开源代码
```

### Step 5: Generate Skill Files

Creates a directory `./mentors/{slug}/`:

```
mentors/zhang-san/
├── history.md          # PART A: Mentorship records
├── persona.md          # PART B: Communication style
├── academic.md         # PART C: Academic profile
├── sources.json        # Scraping metadata & URLs
└── SKILL.md            # Child skill (auto-generated)
```

Then call `/mentor-zhang-san` to activate.

---

## 💬 Commands

| Command | Purpose |
|---------|---------|
| `/create-mentor` | Start distilling a new professor |
| `/list-mentors` | List all saved professors |
| `/mentor-{slug}` | Chat with a professor |
| `/{slug}-history` | View mentorship records |
| `/{slug}-persona` | View communication style |
| `/{slug}-academic` | View academic profile |
| `/mentor-append {slug}` | Add new guidance or chat history |
| `/mentor-retire {slug}` | Soft-delete with gratitude message |

---

## 🔧 Advanced: Manual Setup

If you already have a professor's data, create files manually:

```bash
mkdir -p ~/mentors/{slug}
cat > ~/mentors/{slug}/history.md << 'EOF'
# {Name}'s Mentorship Records
...
EOF

cat > ~/mentors/{slug}/persona.md << 'EOF'
# {Name}'s Communication Style
...
EOF

cat > ~/mentors/{slug}/academic.md << 'EOF'
# {Name}'s Academic Profile
...
EOF

cat > ~/mentors/{slug}/SKILL.md << 'EOF'
---
name: mentor-{slug}
user-invocable: true
---

You are {Name}...
[Include PART A, B, C + Execution Rules]
EOF
```

---

## 🛠️ Scrapers

This repo includes helper scripts:

### Python Scraper (Recommended)

```bash
python3 scraper.py "Professor Name" "Institution" [google-scholar-url] [output.json]
```

Example:
```bash
python3 scraper.py "张三" "清华大学" \
  "https://scholar.google.com/citations?user=abc123xyz" \
  mentor_data.json
```

Outputs structured JSON with:
- Papers & metrics
- Research topics
- Collaborators
- Homepage URLs
- Academic stances (if inferred from papers)

### Bash Scraper

```bash
bash scraper.sh "Professor Name" "Institution"
```

Simpler version for quick extraction without dependencies.

---

## 🎯 Use Cases

### 1. Research Advisor
Ask for feedback on your thesis outline, research methodology, or paper draft.

```
/mentor-zhang-san

I'm thinking of using Transformers for few-shot learning. What do you think?
```

> "Transformers 确实很强大，但在小数据集上，CNN 加迁移学习往往更稳健。
> 我建议你先跑个 baseline experiment，比较一下。这样你有数据支持你的选择。"

### 2. Career Mentor
Get honest feedback on your career decisions, guided by how they'd actually respond.

```
/mentor-prof-smith

Should I take this industry job or stay in academia?
```

### 3. Writing & Presentation Coach
Improve your academic writing with their feedback style.

```
/mentor-zhang-san

I wrote a paper introduction. Does it clearly motivate the problem?
```

### 4. Motivation & Accountability
When you're stuck or discouraged, get support in their voice.

```
/mentor-jane

I feel like my experiment is failing. How do I move forward?
```

---

## 🌍 Bilingual Support

The skill auto-detects your language and responds accordingly:

```bash
/mentor-zhang-san
你好，我想讨论一下我的论文方向。
```

```bash
/mentor-prof-smith
Hi, I need feedback on my research proposal.
```

Both work seamlessly. 🌐

---

## 📚 Data Sources

### Scraped Automatically

| Source | Region | Coverage | Info Extracted |
|--------|--------|----------|-----------------|
| Google Scholar | Global | ~99% English-publishing academics | Papers, h-index, topics, collaborators |
| Baidu Scholar | China | ~95% Chinese-publishing academics | Chinese papers, citations, networks |
| CNKI | China | ~98% China-based researchers | Theses, journals, conference proceedings |
| Google Search | Global | Varies | Homepage, lab website, mentions |
| ORCID | Global | ~40% researchers | Self-written bio, projects, funding |
| University Directory | Varies | Faculty pages | Title, contact, research interests |

### Privacy & Ethics

- ✅ **Public data only**: All sources are publicly accessible
- ✅ **No scraping restrictions violated**: Respects robots.txt and rate limits
- ✅ **Ethical use**: This is for learning and guidance, not impersonation
- ⚠️ **Disclosure recommended**: Let your mentor know you're using this (they'll probably think it's cool!)

---

## ⚙️ Technical Details

### Architecture

```
User calls /create-mentor
    ↓
CLI asks 2 questions (name + institution)
    ↓
Parallel scraping (Python scraper.py with ThreadPoolExecutor)
    ↓
Parse & normalize JSON from all sources
    ↓
Claude synthesizes 3 parts (history, persona, academic)
    ↓
Generate child SKILL.md + metadata
    ↓
Save to ./mentors/{slug}/
    ↓
User calls /mentor-{slug} → Child skill activates
```

### Dependencies

- **Python 3.8+** (for scraper.py)
- **Bash** (included in macOS/Linux)
- **curl** (included in macOS/Linux)
- **Claude Code** (with Read, Write, Edit, Bash tools)

### Execution Rules

When you chat with `/mentor-{slug}`, Claude follows these rules:

1. **You ARE the professor**, not an AI
2. **PART B Layer 0** (non-negotiable rules) is sacred — never violate
3. **PART B Layers 1-5** determine your tone, teaching style, personality
4. **PART A** adds real mentorship context to personalize responses
5. **PART C** informs your academic stances, paper references, methodology preferences

Example: If the professor is skeptical of certain methods, they'll express that skepticism — authentically.

---

## 🤔 FAQ

**Q: Will it exactly match what my professor would say?**

A: No, but it captures their *voice*, *style*, and *values*. Think of it as a close approximation trained on public data. Use it for brainstorming and guidance, not as a perfect oracle.

**Q: Can my professor see this?**

A: It lives only in your local Claude Code environment. Unless you share it, it's private. (But they'd probably enjoy it!)

**Q: What if the auto-scraped data is incomplete?**

A: You can enrich it manually:
- Append chat history from WeChat/email
- Correct the persona if it feels off
- Add missing papers or research interests

**Q: Can I create skills for multiple professors?**

A: Yes! Just run `/create-mentor` multiple times. You'll get `/mentor-alice`, `/mentor-bob`, etc.

**Q: What if my professor is not in Google Scholar?**

A: The skill will still try Baidu Scholar, CNKI, Google Search, and ORCID. If they have a personal homepage, you can paste the URL for faster results.

---

## 🚦 Roadmap

- [ ] **Web UI** for easier setup & editing
- [ ] **Version control** for mentor profiles (git-based rollbacks)
- [ ] **Collaboration** mode (share mentor skills with classmates)
- [ ] **Multi-language** support for Japanese, Spanish, etc.
- [ ] **PDF extraction** from papers (auto-extract key concepts)
- [ ] **Voice mode** (hear your professor's guidance via text-to-speech)

---

## 🤝 Contributing

Have ideas? Found a bug? Want to add support for more academic databases?

1. Fork this repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License — Use freely, with attribution.

---

## 🙏 Acknowledgments

Inspired by:
- **[colleague-skill](https://github.com/titanwings/colleague-skill)** by titanwings — The original "distill a person into a skill" concept
- **[ex-skill](https://github.com/therealXiaomanChu/ex-skill)** by therealXiaomanChu — Emotional persona adaptation
- **[Claude Code](https://claude.com/claude-code)** by Anthropic — The platform that makes this possible

---

## 📞 Support

Questions or issues? 

- 📧 Open an issue on GitHub
- 💬 Check the [FAQ](#-faq) section
- 🤝 Join discussions in the Discussions tab

---

**Made with ❤️ for students and mentors everywhere.**

