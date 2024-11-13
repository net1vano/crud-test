        const address = 'http://127.0.0.1:5000/api/';

        async function createItem() {
            const id = document.getElementById('itemId').value;
            const name = document.getElementById('itemName').value;
            const value = document.getElementById('itemValue').value;

            const response = await fetch(address + id, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, value })
            });

            const result = await response.json();
            console.log('Элемент создан:', result);
        }

        async function updateItem() {
            const id = document.getElementById('itemId').value;
            const name = document.getElementById('itemName').value;
            const value = document.getElementById('itemValue').value;

            const response = await fetch((address + id), {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, value })
            });

            const result = await response.json();
            console.log('Элемент обновлен:', result);
        }

        async function getItem() {
            const id = document.getElementById('itemId').value;

            const response = await fetch((address + id), {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

           async function getItem() {
    const id = document.getElementById('itemId').value;

    const response = await fetch(address + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        const result = await response.json();
        console.log('Полученные данные элемента:', result);
    } else {
        const text = await response.text(); // Если не JSON, прочитать как текст
        console.error('Ошибка при получении данных элемента:', text);
    }
}
        }

        async function getItems() {
            const id = document.getElementById('itemId').value;

            const response = await fetch(address, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            async function getItem() {
    const id = document.getElementById('itemId').value;

    const response = await fetch(address, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        const result = await response.json();
        console.log('Полученные данные элемента:', result);
    } else {
        const text = await response.text(); // Если не JSON, прочитать как текст
        console.error('Ошибка при получении данных элемента:', text);
    }
}
        }

        async function deleteItem() {
            const id = document.getElementById('itemId').value;

            const response = await fetch((address + id), {
                method: 'DELETE'
            });

            async function getItem() {
    const id = document.getElementById('itemId').value;

    const response = await fetch(address + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        const result = await response.json();
        console.log('Полученные данные элемента:', result);
    } else {
        const text = await response.text(); // Если не JSON, прочитать как текст
        console.error('Ошибка при получении данных элемента:', text);
    }
}
        }