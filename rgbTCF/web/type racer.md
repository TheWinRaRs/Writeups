# type racer
```javascript
console.log(Array.from(document.getElementById('Ym9iYmF0ZWEh').children).sort((a, b) => parseInt(a.style.order) -
parseInt(b.style.order)).map(x => x.innerHTML).join('').replace(/&nbsp;/g, ' '))
```
and then pyautogui to type it
