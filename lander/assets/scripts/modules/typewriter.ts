export const typeWriter = (element: HTMLElement, text: string, i: number = 0, fnCallback: any = null) => {

  // check if text isn't finished yet
  if (i < (text.length)) {
    // add next character to h1
   element.innerHTML = text.substring(0, i + 1) +
     '<span aria-hidden="true"></span>';

    // wait for a while and call this function again for next character
    setTimeout(function() {
      typeWriter(element, text, i + 1, fnCallback)
    }, 120);
  }

  // text finished, call callback if there is a callback function
  else if (typeof fnCallback == 'function') {
    // call callback after timeout
    setTimeout(fnCallback, 700);
  }

};