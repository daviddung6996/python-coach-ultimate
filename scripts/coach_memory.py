#!/usr/bin/env python3
"""
Memory manager for python-coach-ultimate.
Lightweight JSON store for progress + weak_topics + monetization level.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MEMORY_ROOT = SCRIPT_DIR.parent.parent / "references" / "memory"
PROGRESS_FILE = "progress.json"


def now_local() -> str:
 return datetime.now().astimezone().isoformat(timespec="seconds")


def ensure_memory_paths(root: Path) -> Path:
 root.mkdir(parents=True, exist_ok=True)
 return root / PROGRESS_FILE


def load_progress(root: Path) -> dict:
 path = ensure_memory_paths(root)
 if not path.exists():
  progress = {
   "current_lesson": 1,
   "completed_lessons": [],
   "exercise_attempts": {},
   "weak_topics": [],
   "next_recommendation": None,
   "monetization_level": 0,
   "completed_projects": [],
   "project_details": {},
   "has_retainer_client": False,
   "created_at": now_local(),
   "last_updated": now_local(),
  }
  save_progress(root, progress)
  return progress
 with path.open("r", encoding="utf-8") as f:
  progress = json.load(f)
 # Backward compatibility: add missing fields
 if "completed_projects" not in progress:
  progress["completed_projects"] = []
 if "project_details" not in progress:
  progress["project_details"] = {}
 if "has_retainer_client" not in progress:
  progress["has_retainer_client"] = False
 return progress


def save_progress(root: Path, progress: dict) -> None:
 path = ensure_memory_paths(root)
 progress["last_updated"] = now_local()
 with path.open("w", encoding="utf-8") as f:
  json.dump(progress, f, indent=2, ensure_ascii=False)
  f.write("\n")


def cmd_init(root: Path) -> None:
 progress = load_progress(root)
 save_progress(root, progress)
 print(f"Initialized progress: {root / PROGRESS_FILE}")
 print(f"Current lesson: {progress['current_lesson']}")
 print(f"Completed: {progress['completed_lessons']}")
 print(f"Monetization level: {progress['monetization_level']}")
 print(f"Completed projects: {progress.get('completed_projects', [])}")


def cmd_snapshot(root: Path) -> None:
 progress = load_progress(root)
 print("# Python Coach Ultimate Progress")
 print(f"- Current lesson: {progress['current_lesson']}")
 print(f"- Completed lessons: {progress['completed_lessons']}")
 print(f"- Weak topics: {progress['weak_topics']}")
 print(f"- Next recommendation: {progress.get('next_recommendation')}")
 print(f"- Monetization level: {progress.get('monetization_level')}")
 print(f"- Completed projects: {progress.get('completed_projects', [])}")
 print(f"- Has retainer client: {progress.get('has_retainer_client', False)}")
 print(f"- Last updated: {progress['last_updated']}")


def cmd_record_attempt(root: Path, lesson: int, correct: bool, notes: str = "") -> None:
 progress = load_progress(root)
 attempts = progress["exercise_attempts"].setdefault(str(lesson), [])
 attempts.append({
  "timestamp": now_local(),
  "correct": correct,
  "notes": notes,
 })
 if correct and lesson not in progress["completed_lessons"]:
  progress["completed_lessons"].append(lesson)
  progress["current_lesson"] = lesson + 1
 save_progress(root, progress)
 print(f"Recorded attempt: lesson {lesson}, correct={correct}")
 print(f"Next lesson: {progress['current_lesson']}")


def cmd_set_lesson(root: Path, lesson: int) -> None:
 progress = load_progress(root)
 progress["current_lesson"] = lesson
 save_progress(root, progress)
 print(f"Set current lesson to {lesson}")


def cmd_weak_topic(root: Path, topic: str) -> None:
 progress = load_progress(root)
 if topic not in progress["weak_topics"]:
  progress["weak_topics"].append(topic)
 save_progress(root, progress)
 print(f"Added weak topic: {topic}")


def cmd_set_monetization(root: Path, level: int) -> None:
 progress = load_progress(root)
 progress["monetization_level"] = level
 save_progress(root, progress)
 print(f"Set monetization level to {level}")


def cmd_add_project(root: Path, project_name: str, details: str = "") -> None:
 progress = load_progress(root)
 if project_name not in progress["completed_projects"]:
  progress["completed_projects"].append(project_name)
 progress["project_details"][project_name] = {
  "date_completed": now_local(),
  "deliverables": [],
  "notes": details,
 }
 # Auto-calculate monetization level
 level = progress["monetization_level"]
 num_projects = len(progress["completed_projects"])
 lesson = progress["current_lesson"]
 
 # Calculate new level
 new_level = 0
 if lesson >= 35 and num_projects >= 4 and progress.get("has_retainer_client", False):
  new_level = 4
 elif lesson >= 26 and num_projects >= 3:
  new_level = 3
 elif lesson >= 16 and num_projects >= 2:
  new_level = 2
 elif lesson >= 7 and num_projects >= 1:
  new_level = 1
 
 if new_level > level:
  progress["monetization_level"] = new_level
  print(f"Monetization level upgraded: {level} -> {new_level}")
 
 save_progress(root, progress)
 print(f"Added project: {project_name}")
 print(f"Completed projects: {progress['completed_projects']}")
 print(f"Monetization level: {progress['monetization_level']}")


def cmd_set_retainer(root: Path, has_retainer: bool) -> None:
 progress = load_progress(root)
 progress["has_retainer_client"] = has_retainer
 # Recalculate level
 num_projects = len(progress["completed_projects"])
 lesson = progress["current_lesson"]
 level = progress["monetization_level"]
 
 new_level = 0
 if lesson >= 35 and num_projects >= 4 and has_retainer:
  new_level = 4
 elif lesson >= 26 and num_projects >= 3:
  new_level = 3
 elif lesson >= 16 and num_projects >= 2:
  new_level = 2
 elif lesson >= 7 and num_projects >= 1:
  new_level = 1
 
 if new_level > level:
  progress["monetization_level"] = new_level
  print(f"Monetization level upgraded: {level} -> {new_level}")
 
 save_progress(root, progress)
 print(f"Set retainer client: {has_retainer}")
 print(f"Monetization level: {progress['monetization_level']}")


def build_parser() -> argparse.ArgumentParser:
 parser = argparse.ArgumentParser(description="Memory manager for python-coach-ultimate.")
 parser.add_argument(
  "--root",
  type=Path,
  default=DEFAULT_MEMORY_ROOT,
  help=f"Memory root directory (default: {DEFAULT_MEMORY_ROOT})",
 )
 subparsers = parser.add_subparsers(dest="command", required=True)
 subparsers.add_parser("init", help="Initialize progress file.")
 subparsers.add_parser("snapshot", help="Show current progress.")
 record = subparsers.add_parser("record", help="Record exercise attempt.")
 record.add_argument("--lesson", type=int, required=True)
 record.add_argument("--correct", type=lambda x: x.lower() == "true", required=True)
 record.add_argument("--notes", default="", help="Optional notes about attempt.")
 setl = subparsers.add_parser("set-lesson", help="Set current lesson number.")
 setl.add_argument("--lesson", type=int, required=True)
 weak = subparsers.add_parser("weak-topic", help="Add a weak topic to review.")
 weak.add_argument("--topic", required=True)
 setmon = subparsers.add_parser("set-monetization", help="Set monetization level (0-4).")
 setmon.add_argument("--level", type=int, required=True, choices=[0,1,2,3,4])
 addproj = subparsers.add_parser("add-project", help="Add a completed project.")
 addproj.add_argument("--name", type=str, required=True, help="Project name (e.g., merge_orders.py)")
 addproj.add_argument("--details", type=str, default="", help="Optional project details.")
 setret = subparsers.add_parser("set-retainer", help="Set retainer client status.")
 setret.add_argument("--has-retainer", type=lambda x: x.lower() == "true", required=True)
 return parser


def main() -> None:
 parser = build_parser()
 args = parser.parse_args()
 root = args.root.resolve()

 if args.command == "init":
  cmd_init(root)
 elif args.command == "snapshot":
  cmd_snapshot(root)
 elif args.command == "record":
  cmd_record_attempt(root, args.lesson, args.correct, args.notes)
 elif args.command == "set-lesson":
  cmd_set_lesson(root, args.lesson)
 elif args.command == "weak-topic":
  cmd_weak_topic(root, args.topic)
 elif args.command == "set-monetization":
  cmd_set_monetization(root, args.level)
 elif args.command == "add-project":
  cmd_add_project(root, args.name, args.details)
 elif args.command == "set-retainer":
  cmd_set_retainer(root, args.has_retainer)
 else:
  raise ValueError(f"Unknown command: {args.command}")


if __name__ == "__main__":
 main()
