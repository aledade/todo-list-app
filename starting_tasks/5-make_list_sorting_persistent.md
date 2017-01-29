## Story
As a user with limited bandwidth to complete my tasks, I'd like the ability to
identify the most high-priority tasks.

## Acceptance criteria
- When loading the page, tasks will appear with the highest priority tasks at top
- When dragging tasks to reorder, the new order is assigned immediately
- After reloading the page, the last assigned order should persist

## Technical notes
- The page already supports reordering tasks on the front end, but nothing will
  happen on the back end after you've ordered tasks.
- You will need to modify the `tasks` table in order to support this behavior.
- See the README for notes on how to write an Alembic migration.
- The directive that currently supports dragging and dropping tasks has
  built-in callbacks that can be leveraged to support this.
