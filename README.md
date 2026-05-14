# Mood-to-Audio Persona Engine 💽

**Applied LLM Content Design & Conversational UI Architecture**

> ⚠️ **Visual Case Study:** [Link to your Notion/PDF 1-Pager Here]

This repository contains the prototype for a local LLM intent engine. It bridges the gap between conversational AI and backend search algorithms by forcing a language model to simultaneously maintain a strict character persona and output structured JSON metadata.

## 🧠 The Concept

Modern audio recommendation systems (like Spotify's AI DJ) require AI to understand abstract human intent. If a user asks for a song to "cry in the rain" to, a standard database search fails. 

This engine solves that by using a two-tier approach:
1. **Conversational Front-End:** The AI responds to the user strictly in the voice of **"The Archivist"**—a gritty, elitist music curator.
2. **Invisible Backend Metadata:** The AI simultaneously extracts the core emotional intent and parses it into strict JSON (`Mood`, `Tempo`, `Genre`) that can be used to query an actual audio database.

## 🛠️ The Tech Stack
* **Language Model:** Local `Llama-3.1-8B-Instruct` (via LM Studio)
* **Structuring Engine:** `Instructor` & `Pydantic`
* **Language:** Python

## 📝 The System Constraints
The core of this project is the Prompt Architecture. The LLM is constrained by strict voice and tone guidelines:
* **Zero-Tolerance for Clichés:** The AI is forbidden from using filler UX phrases like "Sure, here is a playlist!"
* **No Technical Jargon:** The AI cannot say "algorithm," "data," or "streaming."
* **Anti-Hallucination Guardrails:** The AI is explicitly forbidden from naming specific artists or track titles, ensuring it only provides sonic atmosphere parameters for the backend to fulfill.

## 🚀 How to Run Locally

1. **Start your local AI server:**
   Open LM Studio, load `meta-llama-3.1-8b-instruct`, and start the local server on port `1234`.

2. **Install dependencies:**
   ```bash
   pip install openai instructor pydantic
