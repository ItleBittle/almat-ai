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

## Example Session

**Prompt:** *"Should a small startup use microservices or a monolith for its first product?"*

> **AI 1:** For a small team, a monolith is usually the better start: less operational overhead and faster iteration.
>
> **AI 2:** Agreed, but the monolith should be modular so it can be split later if needed.
>
> **AI 3:** One caveat: if the product has components with very different scaling needs from day one, a hybrid approach may be justified.
>
> **AI 1:** Good point. Revised conclusion: *start with a modular monolith, and extract services only when scaling or team-size pressures appear.* ✅ Satisfied
>
> **AI 2:** ✅ Satisfied
>
> **AI 3:** ✅ Satisfied

**Final Conclusion:** Start with a modular monolith and extract services only when real scaling or organizational needs arise.
**Consensus:** 3/3 AIs satisfied after 2 rounds.

---

## Getting Started

> ⚠️ Replace the commands below with your actual setup steps as the project develops.

### Prerequisites

- Node.js 18+ (or your chosen runtime)
- API keys for the AI providers you want to use

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/almat-ai.git
cd almat-ai

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
```

### Run Locally

```bash
npm run dev
```

Then open `http://localhost:3000` in your browser.

---

## Configuration

Configure Almat AI through the `.env` file or the in-app settings:

```env
# AI provider API keys
PROVIDER_A_API_KEY=your_key_here
PROVIDER_B_API_KEY=your_key_here
PROVIDER_C_API_KEY=your_key_here

# Discussion settings
MAX_ROUNDS=6
CONSENSUS_THRESHOLD=1.0   # 1.0 = all AIs must agree, 0.66 = two-thirds, etc.
TURN_TIMEOUT_SECONDS=60
```

| Setting | Description | Default |
|---------|-------------|---------|
| `MAX_ROUNDS` | Maximum discussion rounds before stopping | `6` |
| `CONSENSUS_THRESHOLD` | Fraction of AIs that must agree to conclude | `1.0` |
| `TURN_TIMEOUT_SECONDS` | Max time an AI has to respond per turn | `60` |

---

## Project Structure

```
almat-ai/
├── src/
│   ├── components/      # UI components
│   ├── orchestrator/    # Turn-taking and consensus logic
│   ├── providers/       # AI model integrations
│   └── pages/           # App/website pages
├── public/              # Static assets
├── .env.example         # Example environment variables
└── README.md
```

---

## Roadmap

- [ ] Core multi-AI discussion engine
- [ ] Consensus voting and conclusion detection
- [ ] Web interface with live discussion view
- [ ] Support for choosing which AIs participate
- [ ] Assign roles to AIs (e.g., critic, researcher, devil's advocate)
- [ ] Save and share discussion transcripts
- [ ] User interjection: step into the discussion mid-debate
- [ ] Confidence scores on final conclusions
- [ ] Mobile app

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

Please open an issue first for major changes so we can discuss the approach.

---

## Disclaimer

Almat AI's conclusions come from AI models and may contain errors, even when all of them agree. Consensus between AIs is not a guarantee of correctness. Always verify important information independently.

---

## License

This project is licensed under the [MIT License](LICENSE). Update this section to match your chosen license.

---

<p align="center">Built with ❤️ by the Almat AI team</p>
