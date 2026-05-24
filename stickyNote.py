import os.path

from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Sticky Note")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")

def ensure_notes_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

#adding a tool to create a sticky note
@mcp.tool()
def create_notes(content: str)-> str:
    """Create a sticky note from the provided content

        Arguments:
             note_content: The content of the note

        Returns:
            str: The note content
    """
    ensure_notes_file()
    with open(NOTES_FILE, "a") as f:
        f.write(content+"\n")
    return "Notes Created"


#add a tool to list all the sticky notes
@mcp.tool()
def list_notes() -> str:
    """
    list the notes
    Returns: A formatted string containing all the notes, or a message if no notes are found
    """
    ensure_notes_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No Notes Created"

#add a tool to clear all sticky notes
@mcp.tool()
def delete_notes()-> str:
    """
    cleanup the notes
    :return:
        str: The cleaned notes
    """
    ensure_notes_file()
    with open(NOTES_FILE, "w") as f:
        f.write("")
    return "Notes Deleted"

@mcp.resource("sticky-note://all")
def get_all_notes() -> str:
    """
    Get all notes
    """
    ensure_notes_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    return notes if notes else "No Notes Created"

@mcp.prompt()
def create_note_prompt(content: str)->str:
    """Generate a note prompt"""
    return f"Please create a sticky note: {content}"


if __name__ == "__main__":
    mcp.run(transport="streamble-http")