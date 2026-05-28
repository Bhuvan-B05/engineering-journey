# Day 1

## Completed

* Created engineering workspace structure
* Connected local project with GitHub repository
* Learned Git workflow:

  * git init
  * git add
  * git commit
  * git push
* Built Smart Calculator project
* Added:

  * arithmetic operations
  * unary operations
  * history persistence
  * timestamps
  * exception handling
* Refactored calculator into modular architecture:

  * operations.py
  * parser.py
  * history_manager.py
  * ui.py
  * main.py
* Completed DSA Day 1:

  * Two Sum
  * Maximum Element

---

## Engineering Concepts Learned

* Git staging vs committing
* Repository root structure
* Modularization and separation of concerns
* Parsing architecture
* Defensive programming
* Controlled error handling
* Hashmap optimization
* Time vs space tradeoffs
* Safe initialization
* Traversal vs unnecessary sorting
* Importance of readable variable naming

---

## Bugs / Problems Faced

* Forgot to run `git add` before commit
* Unsaved VS Code file caused confusion during executio
* `factorial` import order issue during modularization
* Duplicate history persistence issue using append mode
* Potential crash using `result.is_integer()` on integers

---

## Mistakes Made

* Assumed sorting was an optimization for max element
* Mixed too many responsibilities inside main loop
* Used vague variable names in parser functions
* Trusted assumptions before reading traceback carefully

---

## Important Realizations

* Simpler solutions can already be optimal
* Hashmaps optimize by avoiding repeated searching
* Refactoring increases architectural pressure
* Good engineering is iterative improvement, not first-try perfection
* Complexity analysis matters more than just working output
* Readable code reduces cognitive overhead
* Debugging is calmer when treating errors as system feedback instead of failure

---

## Questions Still Unclear

* Best practices for larger project modularization
* Circular import prevention strategies
* When to choose memory optimization vs speed optimization
* Better testing strategies beyond manual checking

---

## Tomorrow's Focus

* DSA Day 2:

  * contains duplicate
  * frequency counter
  * valid anagram
* Learn JSON and APIs
* Build small API-based CLI utility
* Start frontend fundamentals:

  * HTML
  * CSS
  * layout basics
