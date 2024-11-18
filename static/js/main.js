const selectedspan = document.querySelectorAll("span[data-width]");
console.log(selectedspan);
function increaseWidth() {
  setTimeout(() => {
    selectedspan.forEach((span) => {
      const tarw = span.getAttribute("data-width");
      span.style.width = tarw;
    });
  }, 1000);
}
increaseWidth();
