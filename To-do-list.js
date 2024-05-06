function addTask() {
  var taskInput = document.getElementById("taskInput");
  var taskList = document.getElementById("taskList");

  if (taskInput.value !== "") {
    var task = document.createElement("li");
    task.innerText = taskInput.value;
    task.addEventListener("click", function() {
      task.classList.toggle("completed");
    });
    taskList.appendChild(task);
    taskInput.value = "";
  }
}
