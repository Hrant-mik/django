const addTaskButton = document.getElementById("add-task-btn");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");


function addTask() {
    const taskText = taskInput.value.trim();
    
    if (taskText !== "") {
        const li = document.createElement('li');
        li.textContent = taskText;

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.classList.add("btn-danger");
        deleteButton.onclick = function() {
            li.remove();
        };

        li.appendChild(deleteButton);

    
        li.onclick = function() {
            li.classList.toggle("completed");
        };

        
        taskList.appendChild(li);
        
        
        taskInput.value = "";
    }
}


addTaskButton.addEventListener('click', addTask);

taskInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        addTask();
    }
});