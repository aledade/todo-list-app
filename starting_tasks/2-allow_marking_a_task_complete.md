## Story
I would like the ability to mark my tasks as completed.
Once completed, a task should not appear in my list of pending tasks.

## Acceptance criteria
1. There will be a "complete" button appearing just left of the Delete button
2. The button should have Bootstrap's green "success" styling
3. Clicking the button immediately removes the task from the "Pending tasks" list

## Technical notes
The `tasks` table is already equipped to handle this feature. You'll just need to 
modify the routes and Angular to complete the story.
