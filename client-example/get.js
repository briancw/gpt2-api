const got = require('got')

const generateOptions = {
    text: 'Hello!',
    min_length: 10,
    max_length: 100,
}

const options = {
    headers: {'Content-Type': 'application/json'},
    method: 'POST',
    json: generateOptions,
}

async function go() {
    try {
        const response = await got('http://192.168.86.85:3000/generate', options)
        console.log(response.body)
    } catch (error) {
        console.log(error)
    }
}

go()
