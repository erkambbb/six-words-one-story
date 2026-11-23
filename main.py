"""Six Words, One Story: writes the entry to /output/entry.txt."""
from pathlib import Path

STORY = "She forgot me. I proposed again."
assert len(STORY.split()) == 6, "story must be exactly six words"

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(STORY, encoding="utf-8")
