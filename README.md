# Almat AI

**Let multiple AIs debate, refine, and agree, so you get answers that have been challenged before they reach you.**

Almat AI is an app/website where several AI models discuss your prompt with each other. Instead of relying on a single model's first answer, Almat AI puts multiple models in a conversation. They critique, build on, and correct each other's ideas until they reach a conclusion they all consider satisfactory and valid.

---

## Table of Contents

- [How It Works](#how-it-works)
- [Key Features](#key-features)
- [The Consensus System](#the-consensus-system)
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
| ✅ **Satisfied** | The AI agrees the conclusion is complete, accurate, and valid. |
| ⚠️ **Needs revision** | The AI sees a flaw, gap, or improvement and explains why. |
| ❌ **Disagree** | The AI believes the conclusion is wrong and proposes an alternative. |

**A discussion concludes when:**

- All AIs mark the conclusion as **Satisfied** (full consensus), or
- A configurable threshold of AIs agree (for example, a majority), or
- The maximum number of rounds is reached. In this case, the result is flagged as **no full consensus** and the remaining disagreements are shown.

**What counts as "valid"?** Each AI is asked to check the conclusion for:

- Logical consistency
- Factual accuracy (to the best of its knowledge)
- Completeness: does it actually answer the user's prompt?
- Unaddressed objections raised earlier in the discussion

---

## License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">Built with ❤️ by the Almat AI team</p>
