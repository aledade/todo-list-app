## Story
As a user, I would like to be able to add new tasks to the list.

## Acceptance criteria
- A Bootstrap "primary action button" will appear in the top right of the page
- This button should be labeled "Add Task"
- After clicking the button, a modal will appear with a text field for the modal's name
- The modal has two buttons: "Create" and "Cancel"
- If the user clicks "Cancel," the modal will go away and no new task is created
    - If the user clicks "Add Task" again, any leftover data from the last modal will not appear
- The "name" text field is required. If the user tries to create a task without
  a name, this field will be highlighted and marked as required
- Created tasks should default to being lower priority than all other tasks
- After pressing "Create," tasks should be immediately added to the list of pending tasks

## Technical notes
Using Angular's built-in form validation is highly encouraged.
