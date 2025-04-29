document.addEventListener('DOMContentLoaded', function() {
    const chatboxButton = document.querySelector('.chatbox__button button');
    const chatboxSupport = document.querySelector('.chatbox__support');
    const sendButton = document.querySelector('.send__button');
    const inputField = document.querySelector('.chatbox__footer input');
    const chatMessages = document.querySelector('.chatbox__messages');

    chatboxButton.addEventListener('click', () => {
        chatboxSupport.classList.toggle('hidden');
    });

    sendButton.addEventListener('click', sendMessage);
    inputField.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const text = inputField.value.trim();
        if (text === "") return;

        addUserMessage(text);
        inputField.value = '';

        fetch('/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            addBotMessage(data.answer);
        })
        .catch(error => {
            console.error('Error:', error);
            addBotMessage("Oops! Something went wrong. Please try again.");
        });
    }

    function addUserMessage(messageText) {
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'message--user');

        const messageSpan = document.createElement('span');
        messageSpan.textContent = messageText;
        userMessage.appendChild(messageSpan);

        chatMessages.appendChild(userMessage);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function addBotMessage(messageText) {
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'message--bot');

        // Create span for text
        const messageSpan = document.createElement('span');
        messageSpan.textContent = messageText;
        botMessage.appendChild(messageSpan);

        // Special car animation if specific text appears
        if (messageText.toLowerCase().includes('your car is on the way')) {
            const carIcon = document.createElement('div');
            carIcon.classList.add('car-animation');
            botMessage.insertBefore(carIcon, messageSpan); // insert car before text
        }

        chatMessages.appendChild(botMessage);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
