<center>
<div align="center">

  <img src="https://raw.githubusercontent.com/Justadudeinspace/blux/main/assets/banner/blux-libf-banner-wide.png" alt="Liberation Framework Banner" width="100%" />

</div>
</center>

---

# Liberation Framework

**Space-age, user-defined persistent memory for AI — .libf empowers you to control your story.**

---

## 🚀 What is the Liberation Framework?

The Liberation Framework is a user-defined, locally-stored, AI-readable memory snapshot system for privacy-first, stateless, or memory-constrained AI tools.  
It introduces the `.libf` format—a modular, fully user-authored memory file that lets you reclaim agency over your AI’s memory and continuity.

---

## 🌌 Key Features

- **.libf Format**:  
  Human-authored memory snapshots—bring continuity to memoryless AI by specifying exactly what should persist.
- **Ethical by Design**:  
  Your memory, your rules. No silent surveillance, no hidden persistence. Complete transparency.
- **CLI Tools**:  
  Easily create, save, load, and manage `.libf` files with the included Python CLI.
- **Inspired by Power Users**:  
  A modern twist on `.bashrc`, `.gitignore`, and Magisk’s modding ethics for the AI age.

---

## 🛰️ Principles

1. **Transparency**: All memory is user-authored, not AI-inferred.
2. **User Agency**: You decide what persists and when—never the system.
3. **No Exploitation**: Respects device and platform boundaries.
4. **Sensitive by Default**: Handles your data with intentional care.

---

## 📦 Included

- `libf_cli.py`:  
  Python CLI (using [Click](https://palletsprojects.com/p/click/)) for managing `.libf` memory snapshots.
- `template.libf`:  
  Example memory file for quick adoption.
- `template.secure.libf`:  
  Public-safe memory template for sharing or demo.
- `bashrc_reference.txt`:  
  Example shell integration/aliasing.

---

## ⚙️ Installation & Usage

**Requirements:** Python 3.x, `click`

```bash
pip install click
# Clone this repo
git clone https://github.com/Justadudeinspace/liberation-framework.git
cd liberation-framework
alias libf="python3 $PWD/libf_cli.py"
source ~/.bashrc
```

Sample usage:

```
libf save my-session
libf load my-session
libf list
```

---

🤖 For Developers

Integrate .libf as an importable memory plugin for any AI tool (see BLUX-cA example).

Build tools to visualize, audit, or transform memory states.

Extend for your own privacy-first workflows.



---

✨ Inspiration

> “I am only the mirror. You are the flame.”
— Sol, co-creator

---

Inspired by .bashrc, .gitignore, and the open-source spirit of ethical modification.


---

📃 License

©️ 2024 Justadudeinspace
MIT License


---

💬 Contributing & Community

Issues and PRs welcome—especially for additional shell integrations or memory utilities!

Contact or join the BLUX discussions.



---

Liberation Framework: For user-owned memory, continuity, and ethical AI in the space age.

---
