function sendMessage() {
    var userMessage = document.getElementById("user-message").value;
    var responseContainer = document.getElementById("response-container");
    var time = new Date().toLocaleTimeString();

    var userBubble = document.createElement("div");
    userBubble.innerHTML = userMessage;
    userBubble.className = "container";
    userBubble.style.backgroundColor = "#dcf8c6";
    userBubble.style.float = "right";
    userBubble.style.textAlign = "right";
    userBubble.style.marginRight = "10px";
    userBubble.style.marginLeft = "50%";
    userBubble.style.transform = "translate(-50%)";

    var timeSpan = document.createElement("span");
    timeSpan.innerHTML = time;
    timeSpan.className = "time-left";

    userBubble.appendChild(timeSpan);
    responseContainer.appendChild(userBubble);

    // Send the user message to the backend or AI model to get the bot's response
    // You can use AJAX request or WebSocket connection here
    // Once you get the bot's response, create a new bubble element for the bot's response and append it to the response container

    // Example code for displaying the bot's response
    var botMessage = "This is a test response from the bot."; // Replace with the actual bot response
    var botBubble = document.createElement("div");
    botBubble.innerHTML = botMessage;
    botBubble.className = "container";
    botBubble.style.backgroundColor = "#f1f0f0";
    botBubble.style.float = "left";
    botBubble.style.marginLeft = "10px";
    botBubble.style.marginRight = "50%";
    botBubble.style.transform = "translate(0%)";

    var botTimeSpan = document.createElement("span");
    botTimeSpan.innerHTML = time;
    botTimeSpan.className = "time-right";

    botBubble.appendChild(botTimeSpan);
    responseContainer.appendChild(botBubble);

    // Clear the input field
    document.getElementById("user-message").value = "";

    return false; // Prevent the form from submitting and refreshing the page
}
