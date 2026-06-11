#!/usr/bin/env python3
"""Search Codyssey reference Markdown files and print grounded snippets."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"


@dataclass
class Chunk:
    file: Path
    location: str
    text: str
    score: int


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"\s+", "", text)
    return re.sub(r"[^\w가-힣]+", "", text)


def query_terms(query: str) -> list[str]:
    suffixes = (
        "으로",
        "에서",
        "에게",
        "인가",
        "은",
        "는",
        "이",
        "가",
        "을",
        "를",
        "에",
        "로",
        "와",
        "과",
        "도",
        "만",
        "요",
    )
    terms = []
    for raw in re.findall(r"[A-Za-z0-9가-힣]+", query.lower()):
        if len(raw) >= 2:
            terms.append(raw)
        if re.search(r"[가-힣]", raw):
            for suffix in suffixes:
                if raw.endswith(suffix) and len(raw) - len(suffix) >= 2:
                    terms.append(raw[: -len(suffix)])
                    break
    compact = normalize(query)
    if compact and compact not in terms:
        terms.append(compact)
    return list(dict.fromkeys(terms))


def split_chunks(path: Path) -> list[Chunk]:
    chunks: list[Chunk] = []
    current_heading = path.name
    buffer: list[str] = []

    def flush() -> None:
        nonlocal buffer
        text = " ".join(line.strip() for line in buffer if line.strip())
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            chunks.append(Chunk(path, current_heading, text, 0))
        buffer = []

    for line in path.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            flush()
            current_heading = heading.group(2).strip()
            continue
        if line.strip():
            buffer.append(line)
        else:
            flush()

    flush()
    return chunks


def score_chunk(chunk: Chunk, terms: list[str], compact_query: str) -> int:
    text_lower = chunk.text.lower()
    compact_text = normalize(chunk.text)
    score = 0
    if compact_query and compact_query in compact_text:
        score += 100
    for term in terms:
        if term in text_lower:
            score += 10
        normalized_term = normalize(term)
        if normalized_term and normalized_term in compact_text:
            score += 8
    return score


def excerpt(text: str, terms: list[str], width: int) -> str:
    compact_terms = [normalize(term) for term in terms if normalize(term)]
    match_index = 0
    for term in terms:
        found = text.lower().find(term.lower())
        if found >= 0:
            match_index = found
            break
    else:
        compact_text = normalize(text)
        for term in compact_terms:
            found = compact_text.find(term)
            if found >= 0:
                match_index = 0
                break

    start = max(0, match_index - width // 3)
    end = min(len(text), start + width)
    snippet = text[start:end].strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet += "..."
    return snippet


def search(query: str, limit: int, width: int) -> list[Chunk]:
    terms = query_terms(query)
    compact_query = normalize(query)
    results: list[Chunk] = []
    for path in sorted(REFERENCES.glob("*.md")):
        for chunk in split_chunks(path):
            chunk.score = score_chunk(chunk, terms, compact_query)
            if chunk.score > 0:
                chunk.text = excerpt(chunk.text, terms, width)
                results.append(chunk)
    results.sort(key=lambda item: (-item.score, item.file.name, item.location))
    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Codyssey reference Markdown files.")
    parser.add_argument("query", nargs="+", help="Question or search keywords")
    parser.add_argument("--limit", type=int, default=8, help="Maximum results to print")
    parser.add_argument("--width", type=int, default=260, help="Snippet width")
    args = parser.parse_args()

    query = " ".join(args.query)
    results = search(query, args.limit, args.width)
    if not results:
        print("No matching Codyssey references found.")
        return 1

    for index, item in enumerate(results, start=1):
        print(f"{index}. {item.file.name} - {item.location} (score {item.score})")
        print(f"   {item.text}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
