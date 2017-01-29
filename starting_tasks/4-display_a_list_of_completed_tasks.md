## Story
I want to be able to see all the past tasks that I've completed,
ordered by the time that they were completed.

## Acceptance criteria
- Below "pending tasks," there will be another list of completed tasks
- This list should have a heading "Completed tasks"
- The list can be styled like "Pending tasks", but tasks cannot be reordered
- When a reminder is marked completed, it should immediately appear in this list
- Each task will display a human-readable timestamp for when it was completed
- Completed tasks cannot be deleted or re-completed (controls for each should not appear)

## Technical notes
[UI Bootstrap][ui-bootstrap] will likely be helpful for styling a list of
completed tasks.

[ui-bootstrap]: https://angular-ui.github.io/bootstrap/
