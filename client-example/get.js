const got = require('got')

const apiBaseRoute = 'http://localhost:3000'
const prompt = `Hello world! `

const generateOptions = {
    prompt,
    min_length: 100,
    max_length: 100,
}

const options = {
    headers: {'Content-Type': 'application/json'},
    method: 'POST',
    json: generateOptions,
}

async function go() {
    try {
        const response = await got(apiBaseRoute + '/generate', options)
        console.log(response.body)
    } catch (error) {
        console.log(error)
    }
}

go()
