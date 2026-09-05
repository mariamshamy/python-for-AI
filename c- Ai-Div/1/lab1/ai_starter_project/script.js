const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const searchInput = document.getElementById("searchInput");
const taskList = document.getElementById("taskList");
const taskCount = document.getElementById("taskCount");

let count = 0;

addBtn.addEventListener("click", function () {
    const task = taskInput.value.trim();

    if (task === "") {
        return;
    }

    const li = document.createElement("li");

    const text = document.createElement("span");
    text.textContent = task;

    const deleteBtn = document.createElement("button");
    deleteBtn.type = "button";
    deleteBtn.textContent = "Delete";
    deleteBtn.className = "deleteBtn";
    deleteBtn.addEventListener("click", function () {
        li.remove();
        count--;
        taskCount.textContent = count;
    });

    li.appendChild(text);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);

    count++;
    taskCount.textContent = count;

    // Clear the input after adding the task
    taskInput.value = "";
    applySearchFilter();
});

function applySearchFilter() {
    const query = searchInput.value.trim().toLowerCase();
    const items = taskList.querySelectorAll("li");

    items.forEach(function (li) {
        const taskText = li.querySelector("span").textContent.toLowerCase();
        const matches = query === "" || taskText.includes(query);
        li.style.display = matches ? "" : "none";
    });
}

searchInput.addEventListener("input", applySearchFilter);

function resetTasks(){
    taskList.innerHTML = "";
    count = 0;
    taskCount.textContent = count;
}

clearBtn.addEventListener("click", resetTasks);

clearBtn.addEventListener("click", function () {
    taskInput.value = "";
});