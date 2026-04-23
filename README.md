Daily Reflection Tree (Deterministic Agent)

A structured, deterministic reflection system designed to guide end-of-day thinking using a decision tree without any AI or LLM at runtime.

Overview

This project implements a reflection tool that walks a user through a guided conversation based on three psychological axes:

Locus (Victim vs Victor)
Do you see control within yourself or outside?
Orientation (Entitlement vs Contribution)
Did you focus on what you got or what you gave?
Radius (Self vs Others)
Were you focused only on yourself or on a broader impact?

The system is fully deterministic:

Same inputs produce the same outputs
No randomness
No AI usage in the final product
Key Features
Deterministic decision tree engine
Fixed-option questions (no free text input)
Structured branching logic
Signal tracking across three axes
Reflection and summary generation
CLI-based agent for simplicity
Project Structure
/tree/
  reflection-tree.json   # Core decision tree (MAIN deliverable)
  tree-diagram.png      # Visual flow of the tree

/agent/
  main.py               # Entry point
  engine.py             # Tree traversal logic
  tree_loader.py        # Loader and validation

/transcripts/
  persona1.md           # Weak mindset path
  persona2.md           # Strong mindset path

write-up.md             # Design explanation
README.md               # Project overview
How It Works
Loads the decision tree from JSON
Starts from the START node
Traverses nodes based on type:
Question → user selects an option
Decision → routes based on answer
Reflection → displays insight
Bridge → transitions between axes
Summary → final output
Tracks signals such as:
Axis 1: internal vs external
Axis 2: contribution vs entitlement
Axis 3: self vs others
Generates a final reflection summary
How to Run (Part B)
cd agent
python main.py
Example Paths

Persona 1 (External / Entitlement / Self)

Blames the situation
Expects recognition
Focuses on self
Outcome: Reflection encourages awareness of control and contribution

Persona 2 (Internal / Contribution / Others)

Adapts quickly
Helps others
Thinks about the team
Outcome: Reflection reinforces positive patterns
Design Decisions
Used fixed options to ensure determinism
Used signal counting instead of complex scoring
Designed reflections to be non-judgmental
Structured flow as a conversation rather than a survey
Psychological Foundations
Locus of Control — Julian Rotter
Growth Mindset — Carol Dweck
Organizational Citizenship Behavior — Organ
Self-Transcendence — Abraham Maslow
Constraints Followed
No LLM usage at runtime
Fully deterministic system
No free-text inputs
Same answers always produce the same results
Future Improvements
Persistent session tracking
Personalized reflection history
Web-based UI
More granular branching
Goal

To demonstrate how psychological frameworks can be transformed into structured, deterministic systems that guide human reflection.
