
        const address = 'http://127.0.0.1:5000/api/';

        function createTableFromDicts(data) {
            if (!Array.isArray(data)) {
                if (typeof data === 'object' && data !== null) {
                    data = [data];
                } else {
                    console.error('Неверный тип данных');
                    return;
                }
            }
            if (data.length === 0) {
                console.error('Список словарей пуст.');
                return;
            }
            const existingTable = document.getElementById('dynamicTable');
            if (existingTable) {
                existingTable.remove();
            }
            const table = document.createElement('table');
            table.id = 'dynamicTable';
            table.border = "1";
            const headers = Object.keys(data[0]);
            table.innerHTML = `<tr>${headers.map(header => `<th>${header}</th>`).join('')}</tr>`;
            table.innerHTML += data.map(dict =>
                `<tr>${headers.map(header => `<td>${dict[header] || ''}</td>`).join('')}</tr>`
            ).join('');
            document.body.appendChild(table);
        }


        async function createItem() {
            const id = document.getElementById('itemId').value;
            const name = document.getElementById('itemName').value;
            const value = document.getElementById('itemValue').value;
            const response = await fetch(address + id, {method: 'POST', headers: {'Content-Type': 'application/json'},body: JSON.stringify({ name, value })});
            const result = await response.json();
            console.log('Элемент создан:', result);
        }

        async function updateItem() {
            const id = document.getElementById('itemId').value;
            const name = document.getElementById('itemName').value;
            const value = document.getElementById('itemValue').value;
            const response = await fetch((address + id), {method: 'PUT',headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ name, value })});
            const result = await response.json();
            console.log('Элемент обновлен:', result);
        }

        async function getItem() {
            const id = document.getElementById('itemId').value;
            const response = await fetch((address + id), {method: 'GET',headers: {'Content-Type': 'application/json'}});
            const result = await response.json();
            console.log('Элемент получен:', result);
            createTableFromDicts(result['request']);
        }
        async function getItems() {
            const id = document.getElementById('itemId').value;
            const response = await fetch(address, {method: 'GET', headers: {'Content-Type': 'application/json'}});
            const result = await response.json();
            console.log('Элемент получен:', result);
            createTableFromDicts(result['request']);
        }
        async function deleteItem() {
            const id = document.getElementById('itemId').value;
            const response = await fetch((address + id), {method: 'DELETE'});
            const result = await response.json();
            console.log('Элемент удален:', result);
            }