# 🌳 **Daily Reflection Tree (Deterministic Agent)**

A structured, deterministic reflection system that guides end-of-day thinking using a decision tree — built without any AI/LLM at runtime.

---

## 🧠 **Overview**

This project implements a guided reflection tool based on three core psychological axes:

### **1. Locus (Victim vs Victor)**
- Measures perceived control  
- Internal → You take ownership  
- External → You blame situations  

### **2. Orientation (Entitlement vs Contribution)**
- Measures effort mindset  
- Contribution → Focus on what you gave  
- Entitlement → Focus on what you received  

### **3. Radius (Self vs Others)**
- Measures scope of thinking  
- Self → Personal focus  
- Others → Broader/team impact  

---

## ⚙️ **System Characteristics**

- Fully deterministic (same inputs → same outputs)  
- No randomness  
- No AI/LLM usage  
- Fixed-option inputs only  
- CLI-based interaction  

---

## 🚀 **Key Features**

- Deterministic decision tree engine  
- Structured branching logic  
- Signal tracking across 3 axes  
- Reflection generation at each stage  
- Final summary output  
- Lightweight CLI agent  

---

## 🌲 **Decision Tree Structure**
START
├── Q1: What happened today?
│ ├── Option A → External (Victim)
│ └── Option B → Internal (Victor)
│
├── Reflection (Locus Insight)
│
├── Q2: How did you respond?
│ ├── Option A → Entitlement
│ └── Option B → Contribution
│
├── Reflection (Orientation Insight)
│
├── Q3: Who did it impact?
│ ├── Option A → Self
│ └── Option B → Others
│
├── Reflection (Radius Insight)
│
└── SUMMARY
├── Axis 1 → Internal / External
├── Axis 2 → Contribution / Entitlement
└── Axis 3 → Self / Others


---

## 📁 **Project Structure**
/tree/
reflection-tree.json # Core decision tree (MAIN deliverable)
tree-diagram.png # Visual representation

/agent/
main.py # Entry point
engine.py # Traversal logic
tree_loader.py # Loader + validation

/transcripts/
persona1.md # Weak mindset path
persona2.md # Strong mindset path

write-up.md # Design explanation
README.md # Project overview


---

## ▶️ **How It Works**

1. Load decision tree from JSON  
2. Start from `START` node  
3. Traverse nodes based on type:

- **Question** → User selects an option  
- **Decision** → Routes flow  
- **Reflection** → Shows insight  
- **Bridge** → Moves between axes  
- **Summary** → Final output  

4. Track signals:
- Axis 1 → Internal vs External  
- Axis 2 → Contribution vs Entitlement  
- Axis 3 → Self vs Others  

5. Generate final reflection summary  

---

## ▶️ **How to Run**

```bash
cd agent
python main.py


🧪 Example Paths
Persona 1 (External / Entitlement / Self)
Blames situation
Expects recognition
Focuses on self

Result: Encourages awareness of control and contribution

Persona 2 (Internal / Contribution / Others)
Takes responsibility
Helps others
Thinks about team

Result: Reinforces positive behavior patterns

🧩 Design Decisions
Fixed options used to ensure determinism
Signal counting instead of complex scoring
Non-judgmental reflection outputs
Structured conversational flow (not survey-like)
🧠 Psychological Foundations
Locus of Control — Julian Rotter
Growth Mindset — Carol Dweck
Organizational Citizenship Behavior — Organ
Self-Transcendence — Abraham Maslow
⚠️ Constraints Followed
No AI/LLM usage at runtime
Fully deterministic logic
No free-text inputs
Same inputs always produce same outputs
📈 Future Improvements
Persistent user sessions
Reflection history tracking
Web-based UI
More granular decision branches
🎯 Goal

To demonstrate how psychological frameworks can be transformed into structured, deterministic systems that guide human reflection.



