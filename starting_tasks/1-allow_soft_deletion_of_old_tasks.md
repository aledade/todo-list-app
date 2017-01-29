## Story
As a user, I want to remove some of my tasks. When I remove a task,
I don't want to see the task appear in my list of upcoming tasks.

## Acceptance criteria
- Clicking the "delete" button immediately removes a task from the UI
- Any task that has not yet been completed can be deleted
- Removed tasks should persist in the database; no data should ever be truly deleted
- When refreshing the page, or loading `/tasks/`, we should not see any deleted tasks
- The delete button should not be disabled for any pending task

## Technical notes
Soft-deletion should be done at the database level. The `tasks` table is
already set up to support this method of deletion.
