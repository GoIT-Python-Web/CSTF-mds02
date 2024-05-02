console.log('Hello world!')

const ws = new WebSocket('ws://localhost:8080')

formChat.addEventListener('submit', (e) => {
  e.preventDefault()
  ws.send(textField.value) // message
  textField.value = null
})

ws.onopen = (e) => {
  console.log('Hello WebSocket!')
}

// ws.onmessage = (e) => {
//   console.log(e.data)
//   text = e.data

//   const elMsg = document.createElement('div')
//   elMsg.textContent = text
//   subscribe.appendChild(elMsg)
// }

ws.addEventListener('message', (e) => {
  console.log(e.data)
  text = e.data

  const elMsg = document.createElement('div')
  elMsg.textContent = text
  subscribe.appendChild(elMsg)
})
