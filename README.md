# agent_forge
A FastAPI + LangGraph powered agent framework with modular tools for building intelligent automation workflows.

Agent Forge is a modular, extensible automation framework built using FastAPI, LangGraph, and a custom tool ecosystem.
It provides a clean architecture for building intelligent agent workflows that can execute tasks, call external tools

# This repository contains:
⚡ FastAPI backend for workflow execution and API exposure
🧠 LangGraph-powered agent engine with node-based orchestration
🛠️ Custom Tooling System including calculator, weather reporter, and more
🏗️ Graph builder for constructing agents, tools, and runtime graph structures (work in progess)
🔌 Extendable tool architecture under core/tools
📦 Production-ready project structure with proper routing (/api/v1), services, and utilities
🔐 .env support for API keys & secrets
🧪 Ready to integrate with LangChain models, Gemini, OpenAI, and other LLM providers

## 🚀 Setup
1. Install all required dependencies:
   ### pip install -r requirements.txt
   
2. Create a `.env` file in the project root and add all required API keys and configuration values.

## ▶️ Run the Application
Start the FastAPI server using Uvicorn:
 ### uvicorn app.main:app --reload
