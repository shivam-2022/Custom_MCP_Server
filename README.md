# Sticky Note MCP Server

A simple custom MCP (Model Context Protocol) server built using the Python MCP SDK.

This server allows you to:
- Create sticky notes
- List all notes
- Delete notes
- Access notes as MCP resources
- Use MCP prompts

---

# Features

## Tools

### create_notes
Create a sticky note.

### list_notes
List all existing notes.

### delete_notes
Delete all notes.

---

# Resources

### sticky-note://all
Fetch all saved notes.

---  

# Prompts

### create_note_prompt
Generate a prompt for note creation.

---

# Project Structure

```text
Custom_MCP_Server/
│
├── .venv/
├── stickyNote.py
├── notes.txt
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
