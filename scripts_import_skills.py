#!/usr/bin/env python3
import json, re, pathlib

SRC = pathlib.Path('/tmp/pmprompt/database/data/skills.json')
DEST = pathlib.Path('/home/forge/.openclaw/workspace/skills-repo/skills')

skills = json.loads(SRC.read_text())
DEST.mkdir(parents=True, exist_ok=True)

created = []

name_re = re.compile(r"^name:\s*([a-z0-9][a-z0-9\-]*)\s*$", re.M)

for s in skills:
    content = s.get('skill_content') or ''
    m = name_re.search(content)
    if not m:
        # fallback: slugify title
        title = (s.get('title') or 'skill').strip().lower()
        slug = re.sub(r'[^a-z0-9]+','-', title).strip('-')
        skill_name = slug[:64] if slug else 'skill'
    else:
        skill_name = m.group(1)

    folder = DEST / skill_name
    folder.mkdir(parents=True, exist_ok=True)
    out = folder / 'SKILL.md'
    out.write_text(content.strip() + "\n")
    created.append(skill_name)

print(f"Wrote {len(created)} skills")
for n in created[:30]:
    print(' -', n)
if len(created) > 30:
    print(f"... +{len(created)-30} more")
