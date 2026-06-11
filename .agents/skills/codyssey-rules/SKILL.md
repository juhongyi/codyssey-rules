---
name: codyssey-rules
description: Answer questions about Codyssey official rules, regulations, peer evaluation, facility usage, scholarship requirements, learner setup guides, GitHub/Discord connection, password changes, Korean input setup, and Neito media generation. Use when the user invokes /codyssey-rules or asks for Codyssey course rules or official-policy guidance that must be grounded in the bundled references.
---

# Codyssey Rules

Use this skill to answer Codyssey learner questions from the bundled official documents.

## Required Workflow

1. Search `references/` before answering. Use `scripts/search_references.py` when a keyword search helps:

```bash
python .agents/skills/codyssey-rules/scripts/search_references.py "<user question>"
```

2. Open the most relevant reference files and inspect the surrounding section or page text. Do not answer from memory.
3. Answer in Korean by default unless the user asks for another language.
4. Include a `근거` section in every answer.

## Evidence Rules

- Cite the reference filename and the most specific available location, such as a heading or `Page N`.
- Include a short excerpt from the source text for each material claim.
- If multiple documents are relevant, cite all of them.
- If sources conflict, present the conflicting excerpts and say confirmation is required.
- If the bundled references do not answer the question, say: `제공된 공식 문서 기준으로는 확인할 수 없습니다.`
- Do not infer hidden policy, eligibility, exceptions, deadlines, or penalties beyond the text.

## Bundled References

- `references/codyssey-regulations.md`: Codyssey operating regulations, academic management, learning management, scholarship, facility and space usage, governance.
- `references/codyssey-peer-evaluation-rules.md`: Peer evaluation procedure, in-person evaluation requirements, forbidden conduct, feedback rules, Q&A.
- `references/neito-now-supports-image-video-and-voice-tts-generation.md`: Neito media generation features and token usage guidance.
- `references/github-discord-integration-manual.md`: GitHub basics, Codyssey connection, Discord connection.
- `references/imac-macos-sequoia-korean-input-guide.md`: iMac Korean input setup and keyboard shortcut guidance.
- `references/password-change-guide.md`: iMac password change steps, password policy, keychain caveats.

`codyssey-learner-user-manual.pdf` is intentionally excluded because the provided PDF is image-based and was not converted.

## Answer Format

Use this structure unless a shorter answer is clearly better:

```markdown
답변:
...

근거:
- `reference-file.md` - Section or Page N: "short excerpt"
```
