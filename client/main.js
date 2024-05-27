// ! получать данные с сервера
const getData = async (url) => {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Ошибка по адресу url`);
    } else {
        return await response.json();
    }
};

const postData = async (url, data) => {
    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: new Headers({
            'Content-Type': 'application/json'
        })
    });
    if (!response.ok) {
        throw new Error(`Ошибка по адресу url`);
    } else {
        return await response.json();
    };

};

const deleteData = async (url) => {
    const response = await fetch(url, {
        method: 'DELETE'
    });
    if (!response.ok) {
        throw new Error(`Ошибка по адресу url`);
    } else {
        return await response.json();
    };

};


getData('http://127.0.0.1:5000/api/items')
    .then((data) => {
        console.log(data);
    })