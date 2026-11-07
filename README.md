# almat-ai
# Almat AI

**Let multiple AIs debate, refine, and agree, so you get answers that have been challenged before they reach you.**

Almat AI is an app/website where several AI models discuss your prompt with each other. Instead of relying on a single model's first answer, Almat AI puts multiple models in a conversation. They critique, build on, and correct each other's ideas until they reach a conclusion they all consider satisfactory and valid.

---

## Table of Contents

- [How It Works](#how-it-works)
- [Key Features](#key-features)
- [The Consensus System](#the-consensus-system)
- [Example Session](#example-session)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## How It Works

1. **You submit a prompt.** Ask a question, pose a problem, or propose an idea.
2. **The AIs discuss it.** Each participating AI takes turns responding to your prompt and to what the others have said.
3. **They vote on the conclusion.** Any AI can signal that the current conclusion is satisfactory and valid, or object and keep the discussion going.
4. **You get the result.** Once the AIs reach consensus (or hit a limit), Almat AI presents the final conclusion along with the full discussion.

```
        ┌──────────────┐
        │  User Prompt │
        └──────┬───────┘
               ▼
   ┌───────────────────────┐
   │   Discussion Round    │◄────────┐
   │  AI 1 → AI 2 → AI 3   │         │
   └───────────┬───────────┘         │
               ▼                     │
   ┌───────────────────────┐   No    │
   │ Is everyone satisfied │─────────┘
   │ with the conclusion?  │
   └───────────┬───────────┘
               │ Yes
               ▼
     ┌───────────────────┐
     │  Final Conclusion │
     └───────────────────┘
```

---

## Key Features

- **Multi-AI discussion:** Multiple AI models converse with each other, not just with you.
- **Self-evaluated conclusions:** Each AI can declare whether a conclusion is satisfactory and valid.
- **Consensus-driven results:** The discussion ends when the AIs agree, not after a fixed number of replies.
- **Transparent reasoning:** Read the full conversation to see how the conclusion was reached.
- **Safeguards against endless loops:** Configurable round limits and timeouts keep discussions from running forever.
- **Mix and match models:** Choose which AIs take part in the discussion.

---

## The Consensus System

The consensus system is the core of Almat AI. After each round, every participating AI evaluates the current proposed conclusion and responds with a status:

| Status | Meaning |
|--------|---------|
| ✅ **Satisfied** | The AI agrees the conclusion is
