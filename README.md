# 🐾 Dova – A Task-Centric Version Control System

**Dova** is a modern, simplified alternative to Git. Designed with a task-first mindset and a cloud-native foundation, Dova streamlines collaboration and makes version control intuitive—even for beginners.

> ⚠️ Dova is in early development. We're building a better VCS from the ground up—focused, opinionated, and simple.

---

## ✨ Why Dova?

Dova replaces Git’s complexity with a focused, friendly approach:

- ✅ **Task-Based Workflow** – Work directly on real tasks, not abstract branches.
- 🧠 **Intuitive Commands** – Minimal, high-level CLI commands aligned with your workflow.
- ☁️ **Cloud-Native by Default** – Automatic sync and team visibility built in.
- 🐛 **Collaborative Reviews** – Request and approve feedback seamlessly.
- 📸 **Manual Checkpoints** – Save your progress explicitly, like saving in a game.
- 💬 **Helpful Errors** – Get actionable, human-friendly error messages.

---

## 🚀 How It Works

### Core Concepts

- **Tasks**: The core unit of development. You create, begin, work on, and complete tasks.
- **Checkpoints**: Save the current state of your work with a message—like commits, but simpler.
- **Daemon Sync**: A background process syncs your work with the cloud.
- **Collaboration**: Multiple developers can work on a task, with merge tools to resolve overlaps.

### Example Workflow

```bash
# Create a new task
dova task create "Add login flow"

# Start working on the task
dova begin 41

# Save your work
dova save "Implement login form validation"

# Ask for a review
dova review

# Approve a teammate's task
dova approve 41

# Finish the task
dova complete 41
```

---

## 🛠 MVP Feature Set

- [x] Local task creation and management
- [x] Manual checkpoints (full snapshot)
- [x] Automatic daemon sync process
- [x] Simple review/approval CLI flow
- [x] Snapshot history
- [x] Conflict warnings and basic merge resolution

---

## 🧪 Status

Dova is currently in the **prototype** phase. The first release will include:

- A CLI written in Python
- A background daemon for sync
- A lightweight cloud backend for task metadata
- Local-only snapshots for file changes

We're not trying to replace Git (yet), but to create a better VCS for focused teams and individuals.

---

## 🐾 Name and Philosophy

The name "Dova" is inspired by animals—collaborative, intelligent, and lightweight. Dova aims to bring those values into your development workflow.

---

## 📦 Installation (Coming Soon)

Once released, Dova will be installable using [`uv`](https://github.com/astral-sh/uv):

```bash
uv tool install dova
```

---

## 🧠 Vision

We believe version control should follow **your mental model**, not the other way around. Dova is our attempt to rethink the VCS from the ground up—with tasks, not branches.

---

## 🤝 Contributing

We’re in the early stages and would love help!

- Want to help shape the API? Discuss merge strategies? Build out sync logic?
- Open an issue or join the discussion.

---

## 📄 License

To be decided. Likely MIT or a similarly permissive license.

---

## ❤️ Built by developers who think Git is brilliant... but overkill.
